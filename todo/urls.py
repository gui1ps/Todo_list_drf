from django.urls import path
from todo import views

urlpatterns = [
    path('tasklist/',views.get_tasks),
    path('create/',views.create_task),
]
