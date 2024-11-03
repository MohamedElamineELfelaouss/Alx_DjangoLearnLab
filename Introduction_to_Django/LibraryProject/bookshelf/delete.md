
### 4. `delete.md`

```markdown
# Delete Operation

Command:
```python
from bookshelf.models import Book
book = Book.objects.get(id=book.id)
book.delete()

# Confirm deletion by checking all books
Book.objects.all()
