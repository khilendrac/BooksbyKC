
from django.shortcuts import render
from django.http import HttpResponse

from .forms import AddForm, SnippetForm
from .models import Book

from .models import Book
# Create your views here.

#This function responses for the books page
def Books(request) :
    ob= Book.objects.all()
    return render(request, 'BooksApp/Books.html',{'allbooks': ob})

#This function responses for addBooks page
def AddBooks(request) :
    if request.method == 'POST' :
        form = AddForm(request.POST)

        if form.is_valid() :

            form.save()

    form = AddForm()
    return render(request, 'BooksApp/AddBooks.html', {'form' : form})

#This function was used for demo purpose
def snippet_detail(request) :
    if request.method == 'POST' :
        form = SnippetForm(request.POST)
        if form.is_valid() :
            form.save()

    form = SnippetForm()
    return render(request, 'BooksApp/AddBooks.html', {'form' : form})

