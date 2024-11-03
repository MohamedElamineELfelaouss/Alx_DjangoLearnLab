
### 3. Update the Book Title
In `update.md`:

```markdown
# Update the Book instance

```python
# Updating the title of the book from “1984” to “Nineteen Eighty-Four”
book.title = "Nineteen Eighty-Four"
book.save()
# The save method does not output anything in the shell.
# To confirm, retrieve the updated title:
print(book.title)  # Output should now show "Nineteen Eighty-Four"
Nineteen Eighty-Four
