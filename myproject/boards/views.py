from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.contrib.auth.models import User
from .models import Board, Topic, Post

def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})

def board_topics(request, pk): # pk is sent from the url request and has the board id to get
    board = get_object_or_404(Board, pk=pk) 
    return render(request, 'topics.html', {'board':board})

def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)

    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']

        user = User.objects.first() # TODO: get the currently logged in user

        topic = Topic.objects.create(
                subject = subject,
                board = board,
                starter = user
            )

        post = Post.objects.create(
                message = message,
                topic = topic,
                created_by = user

            )

        return redirect('board_topics', pk=board.pk) #TODO: redirect to the created topic page


    return render(request, 'new_topic.html', {'board':board})
