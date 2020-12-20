from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

from .models import Book


def home(request):
    context = {
        'posts': Book.objects.all()
    }
    return render(request, 'blog/home.html', context)

class BookListView(ListView):
    model = Book
    template_name = 'blog/home.html'
    context_object_name = 'books'
    ordering = ['-date_posted']
    paginate_by = 3


class UserBookListView(ListView):
    model = Book
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Book.objects.filter(author=user).order_by('-date_posted')




class BookDetailView(DetailView,LoginRequiredMixin):
    model = Book


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'subtitle', 'content',  'book_id', 'price', 'writer']

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)


class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Book
    fields = ['title', 'subtitle', 'content',  'book_id', 'price', 'writer']

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Book
    success_url = '/'

    def test_func(self):
        book = self.get_object()
        if self.request.user == book.author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})
# Create your views here.
