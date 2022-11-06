from django.shortcuts import render, reverse, redirect
from .models import Topics
from .forms import TopicForm

def home(request):
    topics = Topics.objects.all()
    context = {
        'topics': topics
    }
    return render(request, 'home.html',  context)

def topic(request, topic_id):
    topic = Topics.objects.get(id=topic_id)
    return render(request, 'topic.html', {'topic': topic})

def add_topic(request):
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TopicForm()
    return render(request, 'add_topic.html', {'form': form})



def edit_topic(request, topic_id):
    #topic =
    if request.method == 'POST':
        form = TopicForm(data=request.POST, instance=Topics.objects.get(id=topic_id))
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TopicForm(instance=Topics.objects.get(id=topic_id))
    return render(request, 'edit_topic.html', {'form': form})# 'topic': topic})
