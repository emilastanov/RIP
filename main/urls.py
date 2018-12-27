from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.MainView.as_view(), name='home'),
    path('<int:pk>/<slug:slug>/', views.TaskDetailView.as_view(), name='task_detail'),

    path('addevent/', views.AddEventView.as_view(), name='addevent'),

    path('success-event/<int:id>/', views.success_event, name='success-event')
]