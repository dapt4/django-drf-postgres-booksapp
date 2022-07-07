from django.urls import path
from . import views

urlpatterns = [
    path('author/', views.authors_list),
    path('author/<int:id>', views.get_one_author),
    path('author/new', views.new_author),
    path('author/update/<int:id>', views.edit_author),
    path('author/delete/<int:id>', views.delete_author),
    path('book', views.book_list),
    path('book/new', views.new_book),
    path('book/new/many', views.many_books),
    path('book/<int:id>', views.get_one_book),
    path('book/delete/<int:id>', views.delete_book),
    path('book/update/<int:id>', views.edit_book)
]
