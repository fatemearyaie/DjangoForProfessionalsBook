from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.db.models import Q




# Create your views here.
class BookListView(LoginRequiredMixin,ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'book_list'

class BookDetailView(LoginRequiredMixin,PermissionRequiredMixin, DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'
    permission_required = "books.special_status"
    queryset = Book.objects.all().prefetch_related('reviews__author',)
    

class SearchResultListView(ListView):
    model = Book
    template_name = 'books/search_results.html'
    context_object_name = 'book_list'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        return Book.objects.filter(Q(title__icontains=query)|Q(author__icontains=query))
    
    