from django.urls import path

from . import views

urlpatterns = [
    path('', views.TodoListView.as_view(), name='todo_list'),
    path('add/', views.AddTodoView.as_view(), name='add_todo'),
]