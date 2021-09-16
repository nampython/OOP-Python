class Book:
    def __init__(self, isbn, title, author, publisher, pages, price, copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.pages = pages
        self.price = price
        self.copies = copies

    def display(self):
        print(f"{self.isbn}: {self.title}: {self.price}: {self.copies}")

    def in_stock(self):
        if (self.copies > 0):
            return True
        else:
            return False

    def sell(self):
        if self.in_stock():
            self.copies -= 1
        else:
            print("the book is out of stock")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if 50 <= new_price <= 1000	:
            self._price = new_price
        else:
            raise ValueError("Price cannot be less than 50 or more than 1000")


class Fraction:
    def __init__(self, nr, dr=1):
        self.nr = nr
        self.dr = dr
        if self.dr < 0:
            self.nr *= -1
            self.dr *= -1
        self._reduce()

    def show(self):
        print(f'{self.nr}/{self.dr}')

    def multiply(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        f = Fraction(self.nr * other.nr, self.dr * other.dr)
        f._reduce()
        return f

    def add(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        f = Fraction(self.nr * other.dr + self.dr *
                     other.nr, other.dr * self.dr)
        f._reduce()
        return f

    @staticmethod
    def hcf(x, y):
        x = abs(x)
        y = abs(y)
        smaller = y if x > y else x
        s = smaller
        while s > 0:
            if x % s == 0 and y % s == 0:
                break
            s -= 1
        return s

    def _reduce(self):
        h = Fraction.hcf(self.nr, self.dr)
        if h == 0:
            return
        self.nr //= h

        self.dr //= h


class Product:
    def __init__(self, id, marked_price, discount):
        self.id = id
        self.marked_price = marked_price
        self._discount = discount

    def display(self):
        print(self.id, self.marked_price, self.discount)

    @property
    def selling_price(self):
        return self.marked_price - self.marked_price * self.discount * 0.01

    @property
    def discount(self):
        if self.marked_price > 500:
            return self._discount + 2
        else:
            return self._discount

    @discount.setter
    def discount(self, new_discout):
        self._discount = new_discout


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, new_radius):
        if new_radius > 0:
            self._radius = new_radius
        else:
            raise ValueError('Radius should be positive')

    @property
    def diameter(self):
        return self._radius * 2

    @property
    def circumference(self):
        return 2 * 3.14 * self._radius

    def area(self):
        return 3.14 * self._radius * self._radius


class SalesPerson:
    total_revenue = 0
    names = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.sales_amount = 0
        SalesPerson.names.append(self.name)

    def make_sale(self, money):
        self.sales_amount += money
        SalesPerson.total_revenue += money

    def show(self):
        print(self.name, self.age, self.sales_amount)


class Employee:
    domains = set()
    allowed_domains = {'yahoo.com', 'gmail.com', 'outlook.com'}

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Employee.domains.add(email[email.index('@') + 1:])

    def display(self):
        print(self.name, self.email)

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_emails):
        domain = new_emails[new_emails.index('@') + 1:]
        if domain in Employee.allowed_domains:
            self._email = new_emails
        else:
            raise RuntimeError(f'Domain {domain} is not allowed')


class Stack:
    MAX_SIZE = 5

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def push(self, item):
        if (self.size() == Stack.MAX_SIZE):
            raise RuntimeError("Stack fulled")
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise RuntimeError("Stack is empty")
        return self.items.pop()

    def display(self):
        print(self.items)


class BankAccount:
	bank_name = 'ABC bank, XYZ Street, New Delhi'
	def __init__(self, name, balance=0, bank = bank_name):
		self.name = name
		self.balance = balance
		self.bank = bank
	def display(self):
		print(self.name, self.balance)
	def withdraw(self, amount):
		self.balance -= amount
	def deposit(self, amount):
		self.balance += amount
    
class Course:
    def __init__(self, title, instructor, price, lectures):
        self.title = title
        self.instructor = instructor
        self.price = price
        self.lectures = lectures
        self.users = []
        self.ratings = 0
        self.avg_rating = 0

    def __str__(self):
        return f'{self.title}:{self.instructor}'
    def new_user_enrolled(self, user):
        self.users.append(user)

    def received_a_rating(self, new_rating):
        self.avg_rating = (self.avg_rating * self.ratings + new_rating)/(self.ratings + 1)
        self.ratings+=1
    def show_details(self):
        print('Course Title : ', self.title)
        print('Intructor : ', self.instructor)
        print('Price : ', self.price)
        print('Number of Lectures : ', self.lectures)
        print('Users : ', self.users)
        print('Average rating : ', self.avg_rating)

class VideoCourse(Course):
    def __init__(self, title, instructor, price, lectures, length_video):
        super().__init__(title, instructor, price, lectures)
        self.length_video = length_video
    def show_details(self):
        super().show_details()
        print("video length: ", self.length_video)

class PdfCourse(Course):
    def __init__(self, title, instructor, price, lectures, pages):
        super().__init__(title, instructor, price, lectures)
        self.pages = pages
    def show_details(self):
        super().show_details()
        print('Number of pages : ',  self.pages)



