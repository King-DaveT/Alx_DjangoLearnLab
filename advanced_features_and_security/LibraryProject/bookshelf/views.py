# views.py
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import ExampleForm

from django.shortcuts import render

def example_form_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process form data (for demonstration, we can just print it)
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            print(name, email)
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})


@permission_required('relationship_app.can_view', raise_exception=True)
def view_books(request):
    books = Book.objects.all()
    return render(request, 'books/view_books.html', {'books': books})

@permission_required('relationship_app.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        Book.objects.create(title=title, author=author)
        return redirect('view_books')
    return render(request, 'books/create_book.html')
    'book_list'

@permission_required('relationship_app.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.save()
        return redirect('view_books')
    return render(request, 'books/edit_book.html', {'book': book})

@permission_required('relationship_app.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('view_books')
    
Book.objects.filter(title__icontains=user_input)

form = MyForm(request.POST)
if form.is_valid():
    # process data safely
