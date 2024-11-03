
### 4. Delete the Book Instance
In `delete.md`:

```markdown
# Delete the Book instance

```python
# Deleting the book instance
book.delete()
(1, {'bookshelf.Book': 1})  # Indicates that one Book instance was deleted.
# Trying to retrieve the book again should result in an error if it was successfully deleted.
Book.objects.get(title="Nineteen Eighty-Four")
DoesNotExist: Book matching query does not exist.
