from django.urls import path

from . import views

app_name = 'catalog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('book/<int:pk>/', views.BookDetailsView.as_view(), name="book-details"),
    path('author/<int:pk>/', views.AuthorDetailsView.as_view(), name="author-details"),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('borrowed/', views.BorrowedListView.as_view(), name='borrowed'),

]





# =============================================================================================
# Passing additional options in your URL maps:
#
# This approach can be useful if you want to use the same view for multiple resources, and pass data to configure its
#  behaviour in each case (below we supply a different template in each case).
# =============================================================================================

# path('url/', views.my_reused_view, {'my_template_name': 'some_path'}, name='aurl'),
# path('anotherurl/', views.my_reused_view, {'my_template_name': 'another_path'}, name='anotherurl'),

