from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TaskForm, EventForm
from unidecode import unidecode
from .models import Tasks, Events
from django.http import Http404
from django.http import JsonResponse


class MainView(LoginRequiredMixin, CreateView, ListView):
    template_name = 'main/main.html'
    form_class = TaskForm
    success_url = reverse_lazy('main:home')
    model = Tasks
    paginate_by = 3

    def get_queryset(self):
        return list(reversed(super().get_queryset().filter(user=self.request.user)))

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.slug = slugify(unidecode(form.instance.title))
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Мой список дел | Главная'

        return context


class TaskDetailView(LoginRequiredMixin, DetailView, CreateView):
    template_name = 'main/task_detail.html'
    form_class = EventForm
    success_url = '/'
    paginate_by = 3

    def get_queryset(self):
        return Tasks.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.object.user == self.request.user:
            context['task'] = self.object
            context['events'] = reversed(Events.objects.filter(event=self.object))
            context['title'] = 'Мой список дел | {}'.format(self.object.title)
            context['progress'] = {'all':len(Events.objects.filter(event=self.object.id)),
                                   'success': len(Events.objects.filter(event=self.object.id, status=True)),
                                   'len': int((len(Events.objects.filter(event=self.object.id, status=True))/len(Events.objects.filter(event=self.object.id)))*100)
                                   }
            return context
        else:
            raise Http404

    def form_valid(self, form):
        form.instance.slug = slugify(unidecode(form.instance.title))
        self.success_url = self.request.GET.get('next')
        return super().form_valid(form)


class AddEventView(LoginRequiredMixin, CreateView):
    template_name = 'main/main.html'
    success_url = reverse_lazy('main:home')
    form_class = EventForm

    def form_valid(self, form):
        form.instance.slug = slugify(unidecode(form.instance.title))
        form.instance.event = self.request.attr.get('event')
        return super().form_valid(form)


def success_event(request,id):
    ev = Events.objects.get(pk = id)
    ev.status = True
    ev.save(update_fields=['status'])
    return redirect(request.GET.get('next'))


