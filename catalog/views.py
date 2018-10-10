from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
from django.views import View, generic


class IndexView(View):

    def get(self, request):
        # welcome = "Welcome to index page"
        # return HttpResponse(welcome)

        num_books = Book.objects.all().count()
        num_instances = BookInstance.objects.all().count()
        num_instances_available = BookInstance.objects.filter(status__exact='a').count()
        num_authors = Author.objects.count()  # The 'all()' is implied by default.
        num_genres = Genre.objects.count()  # The 'all()' is implied by default.
        num_books_Guide = Book.objects.filter(title__icontains='Guide').count()
        context = {
            'num_books': num_books,
            'num_instances': num_instances,
            'num_instances_available': num_instances_available,
            'num_authors': num_authors,
            'num_genres': num_genres,
            'num_books_Guide': num_books_Guide,
        }
        return render(request, 'catalog/index.html', context)


class BookListView(generic.ListView):
    model = Book
    paginate_by = 1

    # =============================================================================================
    # Within the template you can access the list of books with the template variable named object
    # list OR book_list (i.e. generically "the_model_name_list").
    #  ===============================================================================

    # template_name = 'catalog/book_list.html'
    # ===============================================================================
    # book_list.html is a default template when you specify generic ListView template
    # ===============================================================================

    # context_object_name = 'my_book_list'
    # ===============================================================================
    #     default is "the_model_name_list", if you want you can specify urs by overriding
    # ===============================================================================

    # queryset = Book.objects.all()

    # ==================================================================================
    # we can override the  get_queryset() method to change the list of records returned. This is more flexible than
    # just setting the queryset attribute
    # ==================================================================================

    def get_queryset(self):
        # original qs
        qs = super().get_queryset()
        # filter by a variable captured from url, for example
        return qs

    # def get_context_data(self, **kwargs):
    #     context = super(BookListView, self).get_context_data(**kwargs)
    #     return context


class AuthorListView(generic.ListView):
    model = Author


class BookDetailsView(generic.DetailView):
    model = Book
    # ===============================================================================
    # Within the template you can access the model of book with the
    # template variable named "object" OR "book" (i.e. generically "the_model_name").
    # ===============================================================================

    # ===============================================================================
    # If a requested record does not exist then the generic class-based detail view will raise an Http404 exception
    # for you automatically
    # ===============================================================================

    # template_name = "catalog/book_detail.html"
    # ===============================================================================
    # book_detail.html is a default template when you specify generic DetailView template
    # ===============================================================================


class AuthorDetailsView(generic.DetailView):
    model = Author


class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')


class BorrowedListView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    permission_required = 'catalog.can_mark_returned'
    model = BookInstance
    template_name = 'catalog/list_of_all_borrowers.html'

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='o').order_by('due_back')
