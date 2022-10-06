from django.shortcuts import render
from django.views.decorators.http import (
    require_http_methods,
    require_POST,
    require_safe,
)
from django.contrib.auth.decorators import login_required
from .models import Todo
from .forms import TodoForm
from django.shortcuts import render, redirect

# Create your views here.


@require_safe
def index(request):
    todo = Todo.objects.all()
    context = {'todo': todo}
    return render(request, 'todo/index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def new(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('todo:index')
    else:
        form = TodoForm()
    context = {
        'form': form,
    }
    return render(request, 'todo/new.html', context)


@require_POST
def delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    if request.user.is_authenticated:
        if request.user == todo.user:
            todo.delete()
            return redirect('todo:index')
    return redirect('todo:index')
