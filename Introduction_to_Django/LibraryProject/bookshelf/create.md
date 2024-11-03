# Create a Book instance

```python
from bookshelf.models import Book

# Creating a book instance with title “1984”, author “George Orwell”, and publication year 1949
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

<Book: Book object (1)>  # This indicates that the book instance was created successfully.
