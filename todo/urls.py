from django.urls import path
from todo import views

urlpatterns = [
    path('tasklist/',views.get_tasks),
    path('create/',views.create_task),
    path('task/<int:pk>/',views.get_task),
    path('delete/<int:pk>/',views.delete_task),
    path('update/<int:pk>/',views.update),
]
