from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Board

def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})

def board_topics(request, pk): # pk is sent from the url request and has the board id to get
    board = get_object_or_404(Board, pk=pk) 
    return render(request, 'topics.html', {'board':board})

