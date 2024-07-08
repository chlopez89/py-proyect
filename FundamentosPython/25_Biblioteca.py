class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
            
    def borrow(self):
        if self.available:
            self.available = False
            print(f"El libro {self.title} ha sido prestado")
        else:
            print(f"El libro {self.title} no está disponible")

    def return_book(self):
        self.available = True
        print(f"El libro {self.title} ha sido devuelto")
        
class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []
        
    def borrow_book(self, book):
        if book.available:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f"El Libro {book.title} No esta disponibl")
        
    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f"El libro {book.title} No esta en la lista de prestados.")

class Library:
    def __init__(self):
        self.books = []
        self.users = []
    
    def add_book(self, book):
        self.books.append(book)
        print(f"El libro {book.title} ha sido agregado")
        
    def register_user(self, user):
        self.users.append(user)
        print(f"El Usuario {user.name} ha sido registrado")
        
    def show_available_books(self):
        print(f"Los libros disponibles:")
        contador_libros = 0
        for book in self.books:
            contador_libros+=1
            if book.available:
                print(f"{contador_libros}.- {book.title} por {book.author}")

# Creacion de los Libros.              
book_1 = Book("Las Historias de un programador",  "Christian López")
book_2 = Book("Maquiavelo", "Manitas")
book_3 = Book("Las mil sombras del Codigo libre", "OpenIA")
book_4 = Book("El Limpiador del Codigo", "Anderzon Estrada")

# Creación de los Usuarios.
user_1 = User("Chlopez", "001")
user_2 = User("Wadalupe", "002")
user_3 = User("Carmelo", "003")

# Crear Biblioteca.
library_1 = Library()
library_1.add_book(book_1)
library_1.add_book(book_2)
library_1.add_book(book_3)
library_1.add_book(book_4)
library_1.register_user(user_1)
library_1.register_user(user_2)
library_1.register_user(user_3)

# Mostrar libros.
print("# Mostrar libros.")
library_1.show_available_books()

# Realizar prestamo.
print("# Realizar prestamo.")
user_1.borrow_book(book_1)

# Mostrar libros.
print("# Mostrar libros.")
library_1.show_available_books()

# Devolver libro
print("# Devolver libro")
user_1.return_book(book_1)

# Mostrar libros.
print("# Mostrar libros.")
library_1.show_available_books()
