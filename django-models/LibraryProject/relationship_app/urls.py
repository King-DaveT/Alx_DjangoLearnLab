from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='book-list'),  # FBV
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),  # CBV
]

# relationship_app/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register_view, name='register'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('admin-area/', views.admin_view, name='admin_view'),
    path('librarian-area/', views.librarian_view, name='librarian_view'),
    path('member-area/', views.member_view, name='member_view'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('books/add/', views.add_book, name='add_book'),
    path('books/<int:pk>/edit/', views.edit_book, name='edit_book'),
    path('books/<int:pk>/delete/', views.delete_book, name='delete_book'),
]
