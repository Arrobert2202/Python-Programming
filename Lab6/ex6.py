class LibraryItem():
  def __init__(self, title, available = False):
    self.title = title
    self.available = available
    
  def check_out(self):
    if self.available:
      print(f"{self.title} - checked out")
      self.available = False
    else:
      print(f"{self.title} is not available")

  def return_item(self):
    if self.available:
      print(f"{self.title} is already available")
    else:
      print(f"{self.title} is returned")
      self.available = True

  def display_info(self):
    print(f"Title: {self.title} - {'Available' if self.available else 'Not Available'}")

class Book(LibraryItem):
  def __init__(self, title, author, genre, available = False):
    super().__init__(title, available)
    self.author = author
    self.genre = genre

  def display_info(self):
    super().display_info()
    print(f"Author: {self.author}")
    print(f"Genre: {self.genre}")

class DVD(LibraryItem):
  def __init__(self, title, director, genre, available=False):
    super().__init__(title, available)
    self.director = director
    self.genre = genre
  
  def display_info(self):
    super().display_info()
    print(f"Director: {self.director}")
    print(f"Genre: {self.genre}")
  
class Magazine(LibraryItem):
  def __init__(self, title, editor, type, available=False):
    super().__init__(title, available)
    self.editor = editor
    self.type = type
  
  def display_info(self):
    super().display_info()
    print(f"Editor: {self.editor}")
    print(f"Type: {self.type}")

book = Book("Amintiri idn copilarie", "Ion Creanga", "Memories", True)

book.display_info()
book.check_out()
book.display_info()
book.return_item()
book.display_info()
print()

dvd = DVD("Fast and Furious", "Justin Lin", "Action", True)

dvd.display_info()
dvd.check_out()
dvd.display_info()
dvd.return_item()
dvd.display_info()
print()

magazine = Magazine("Time Square", "John", "Weekly")

magazine.display_info()
magazine.check_out()
magazine.display_info()
magazine.return_item()
magazine.display_info()