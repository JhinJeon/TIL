from pydoc_data.topics import topics
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .models import Topic
from .forms import TopicForm

# Create your views here.

def index(request):
    topics = Topic.objects.all()
    context = {
        'topics':topics
    }
    return render(request, 'either/index.html', context)


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topics = form.save(commit=False)
            topics.user = request.user
            topics.save()
            return redirect('topics:detail', topics.pk)
    else:
        form = TopicForm()
    context = {
        'form': form,
    }
    return render(request, 'either/create.html', context)

def detail(request):
    return