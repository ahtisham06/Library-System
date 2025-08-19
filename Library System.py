class Book:
  def __init__(self, title, author):
      self.title = title
      self.author = author
      self.is_borrowed = False

  def __str__(self):
      return f"{self.title} by {self.author}"

class Library:
  def __init__(self, name):
      self.name = name
      self.books = []

  def add_book(self, book):
      self.books.append(book)
      print(f"Book '{book.title}' added to library.")

  def display_books(self):
      if not self.books:
          print("No books in the library.")
      else:
          print(f"\nAvailable books in {self.name}:")
          for book in self.books:
              status = "Borrowed" if book.is_borrowed else "Available"
              print(f"- {book} [{status}]")

  def borrow_book(self, title):
      for book in self.books:
          if book.title.lower() == title.lower():
              if not book.is_borrowed:
                  book.is_borrowed = True
                  print(f"You have borrowed '{book.title}'.")
                  return
              else:
                  print(f"'{book.title}' is already borrowed.")
                  return
      print("Book not found in the library.")

  def return_book(self, title):
      for book in self.books:
          if book.title.lower() == title.lower():
              if book.is_borrowed:
                  book.is_borrowed = False
                  print(f"You have returned '{book.title}'.")
                  return
              else:
                  print(f"'{book.title}' was not borrowed.")
                  return
      print("Book not found in the library.")

def main():
  my_library = Library("City Library")

  while True:
      print("\n--- Library Menu ---")
      print("1. Add Book")
      print("2. Display Books")
      print("3. Borrow Book")
      print("4. Return Book")
      print("5. Exit")
      choice = input("Enter your choice (1-5): ")

      if choice == '1':
          title = input("Enter book title: ")
          author = input("Enter book author: ")
          new_book = Book(title, author)
          my_library.add_book(new_book)

      elif choice == '2':
          my_library.display_books()

      elif choice == '3':
          title = input("Enter title of the book to borrow: ")
          my_library.borrow_book(title)

      elif choice == '4':
          title = input("Enter title of the book to return: ")
          my_library.return_book(title)

      elif choice == '5':
          print("Exiting the Library System. Goodbye!")
          break

      else:
          print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()



















