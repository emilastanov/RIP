from django import forms
from .models import Tasks, Events

class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ('title', 'description','created')


class EventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ('title', 'description', 'term','event')