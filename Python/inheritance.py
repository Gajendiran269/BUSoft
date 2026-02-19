class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def get_info(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"


class Book1(Book):
    def __init__(self, title, author, pages, file_format):
        super().__init__(title, author, pages)
        self.file_format = file_format
    
    def get_info(self):
        return super().get_info() + f", Format: {self.file_format}"


class Book2(Book):
    def __init__(self, title, author, pages, duration_hours):
        super().__init__(title, author, pages)
        self.duration_hours = duration_hours
    
    def get_info(self):
        return super().get_info() + f", Duration: {self.duration_hours} hours"


book = Book("Python Basics", "John Doe", 300)
print(book.get_info())

book1 = Book1("Python Advanced", "Jane Smith", 400, "PDF")
print(book1.get_info())

book2 = Book2("Python Tips", "Bob Johnson", 250, 12)
print(book2.get_info())