import json

from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView

from .models import Todo

class AddTodoView(CreateView):
    model = Todo
    fields = ['done', 'text']

    def post(self, request, *args, **kwargs):
        print(request.POST)
        text = request.POST.get('text')
        if text:
            Todo(text=text, done=False).save()
        return HttpResponseRedirect(TodoListView.get_url())


class TodoListView(ListView):
    model = Todo
    template_name = 'todo/todo_list.html'

    def dispatch(self, request, *args, **kwargs):
        print(self.get_queryset().last().done)
        return super(TodoListView, self).dispatch(request, *args, **kwargs)

    def get_url(self=None):
        return reverse('todo:todo_list')

    def post(self, request, *args, **kwargs):
        print(request.POST)
        for todo in self.get_queryset():
            todo.done = bool(request.POST.get(str(todo.id), False))
            todo.save()

        return HttpResponseRedirect(self.get_url())
