from django.shortcuts import render
from django.views import generic
from . import models

# Create your views here.


class Home(generic.ListView):
    template_name = 'books/home.html'
    context_object_name = 'book_list'

    def get_queryset(self):
        return models.Book.objects.all()

class Detail(generic.DetailView):
    model = models.Book
    template_name = 'books/detail.html'