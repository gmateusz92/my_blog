from django.shortcuts import render, reverse, redirect
from .models import Topics
from .forms import TopicForm, CommentForm

def home(request):
    topics = Topics.objects.all()
    context = {
        'topics': topics
    }
    return render(request, 'home.html',  context)

def topic(request, topic_id):
    topic = Topics.objects.get(id=topic_id)
    comments = topic.comment_set.order_by('created_at') #_set tworzymy na podstawie foreignkey
    return render(request, 'topic.html', {'topic': topic, 'comments': comments})

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
    #topic =Topics.objects.get(id=topic_id)) moze byc w instance albo jako zmienna Topic
    if request.method == 'POST':
        form = TopicForm(data=request.POST, instance=Topics.objects.get(id=topic_id))# zeby formularz byl wypelniony wpisem danym
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TopicForm(instance=Topics.objects.get(id=topic_id))
    return render(request, 'edit_topic.html', {'form': form})# 'topic': topic})

def add_comment(request, topic_id):
    topic = Topics.objects.get(id=topic_id)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)# a metody save() dołączamy argument commit=False (patrz wiersz ), aby nakazać Django utworzenie nowego obiektu wpisu i jego przechowywanie w zmiennej new_entry, ale jeszcze bez zapisywania w bazie danych
            comment.topic = topic #Atrybutowi new_entry egzemplarza topic przypisujemy temat pobrany z bazydanych na początku kodu funkcji (patrz wiersz ), a następnie wywołujemysave() bez argumentów. W ten sposób wpis zostanie zapisany w bazie danychwraz z przypisanym mu prawidłowym tematem
            comment.save()
            return redirect('topic', topic_id=topic_id)
    return render(request, 'add_comment.html', {'form': form, 'topic': topic})

