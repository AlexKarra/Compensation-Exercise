# 1
def calc_average(numbers: list) -> float:
    try:
        average = sum(numbers) / len(numbers)
        return average
    except (TypeError, ZeroDivisionError):
        raise ValueError('Invalid value in the list')

# Example usage:
numbers = [6, 18, 38, 42, 53]
print(calc_average(numbers))


# 2
def print_pyramid(rows):
    try:
        rows = int(rows)
    except ValueError:
        raise ValueError('Invalid value for rows')

    if rows <= 0:
        raise ValueError('Invalid value for rows')

    for line in range(rows):
        print(" " * (rows - line - 1) + '*' * (2 * line + 1))

# Example usage:
print_pyramid(24)


# 3
def clean_string(my_string: str) -> str:
    cleaned_string = ''
    for char_or_dig in my_string:
        if ('a' <= char_or_dig <= 'z') or ('A' <= char_or_dig <= 'Z') or char_or_dig == ' ':
            cleaned_string += char_or_dig
    return cleaned_string

# Example usage:
cleaned_string = clean_string("783He4l#$%47l43((^%#))734o3843 98wo*(rld")
print(cleaned_string)


# 4
def  count_special_char(my_string: str) -> str:
    special_chars = 0
    for char_or_dig in my_string:
        if not (('a' <= char_or_dig <= 'z') or ('A' <= char_or_dig <= 'Z') or char_or_dig == ' '):
            special_chars += 1
    return special_chars

# Example usage:
special_chars = count_special_char("#$^&Hello*768576576*&")
print(special_chars)


# 5
def dict_to_list(dictionary: dict) -> list:
    return list(dictionary.values())

# Example usage:
dict = {'Tomas': 12, 'Anna': 46, 'Conrad': 48}
list = dict_to_list(dict)
print(list)


# 6
def list_to_dict(key_list: list, value_list: list) -> dict:
    if len(key_list) < len(value_list) or len(key_list) > len(value_list):
        raise ValueError('Lists must be of the same length')

    dictionary = {}
    for element in range(len(key_list)):
        dictionary[key_list[element]] = value_list[element]

    return dictionary


# Example usage:
key_list = ['Category', 1000, 'Name', "Year"]
value_list = [1, "ECTS points", "Alex", 2023]
result_dict = list_to_dict(key_list, value_list)
print(result_dict)


# 7
def chunk_list(my_list: list, chunks: int) -> list:
    if not my_list:
        raise ValueError('The list must not be empty')

    if len(my_list) // chunks * chunks == len(my_list):
        chunk_size = len(my_list) // chunks
        result = [my_list[i:i+chunk_size] for i in range(0, len(my_list), chunk_size)]
        return result
    else:
        raise ValueError('The list length must be divisible by chunk size')

# Example usage:
my_list = ["Banana", "Apple", "Mango", "Pineapple", "Lemon", "Lime"]
chunks = 2
print(chunk_list(my_list, chunks))


# 8
class Book:
    def __init__(self, name: str, author: str, genre: str, borrowed: bool = False):
        self.name = name
        self.author = author
        self.genre = genre
        self.borrowed = borrowed

    def __str__(self):
        book_info = f"{self.name}, {self.author}"
        if self.borrowed:
            book_info += ", borrowed"
        return book_info

# Example usage 1:
my_book1 = Book("1984", "George Orwell", "Fiction")
print(my_book1)

# Example usage 2:
my_book2 = Book("Moby Dick", "Herman Melville", "Adventure", True)
print(my_book2)


# 9
class Library:
    def __init__(self):
        self.book_list = []

# 9a
    def add_book(self, book):
        if type(book) == Book:
            self.book_list.append(book)

#9b
    def get_all_books(self):
        return self.book_list

#9c
    def borrow_book(self, book):
        if book in self.book_list:
            if book.borrowed:
                print('Book already borrowed')
            else:
                book.borrowed = True
        else:
            print('Book does not exist')

#9d
    def return_book(self, book):
        if book in self.book_list:
            if not book.borrowed:
                print('Book has not been borrowed')
            else:
                book.borrowed = False
        else:
            print('Book does not exist')

#Example usage:

# Create Library object
my_library = Library()

# Add books
my_library.add_book(my_book1)
my_library.add_book(my_book2)

# Get all books
all_books = my_library.get_all_books()
print(all_books)

# Borrow a book
my_library.borrow_book(my_book1)
my_library.borrow_book(my_book2)

# Return a book
my_library.return_book(my_book1)
my_library.return_book(my_book2)


# 10

class BookStack:
    def __init__(self):
        self.stack = []

#10a
    def push(self, book):
        if type(book) == Book:
            self.stack.append(book)

#10b
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()

#10c
    def top(self):
        if self.size() > 0:
            return self.stack[-1]

#10d
    def size(self):
        return len(self.stack)

# Create BookStack object
my_stack = BookStack()

# Push books onto the stack
my_stack.push(my_book1)
my_stack.push(my_book2)

# Get the top book
print(my_stack.top())

# Pop a book from the stack
print(my_stack.pop())

# Get the size of the stack
print(my_stack.size())


# 11

def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            word_count = len(content.split())
            return word_count
    except FileNotFoundError:
        print("File not found")
    except IOError:
        print("Error reading the file")

# Example usage:
print(count_words("C:/Users/AlexKarra/Desktop/text.txt"))

# 12

def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            line_count = len(lines)
            return line_count
    except FileNotFoundError:
        print("File not found")
    except IOError:
        print("Error reading the file")

# Example usage:
print(count_lines("C:/Users/AlexKarra/Desktop/text.txt"))


# 13

def write_even(input_file_path, output_file_path):
    try:
        with open(input_file_path, 'r') as input_file:
            lines = input_file.readlines()
            even_lines = lines[1::2]

        with open(output_file_path, 'w') as output_file:
            output_file.writelines(even_lines)

    except FileNotFoundError:
        print("Input file not found")
    except IOError:
        print("Error reading or writing the file")

# Example usage:
input_file_path = "C:/Users/AlexKarra/Desktop/input_file.txt"
output_file_path = "C:/Users/AlexKarra/Desktop/output_file.txt"
write_even(input_file_path, output_file_path)
