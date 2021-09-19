from practice_exercise import Fraction, Book, Product, Circle, SalesPerson, Employee, Stack,Course, VideoCourse, PdfCourse

def main_Fraction():
	f1 = Fraction(4, 6)
	f2 = Fraction(2, 4)
	f3 = f1.multiply(f2)
	f3.show()

def main_Book():

	book1 = Book('957-4-36-547417-1', 'Learn Physics','Stephen', 'CBC', 350, 200,10) # instance  object
	book2 = Book('652-6-86-748413-3', 'Learn Chemistry','Jack', 'CBC', 400, 220,20)
	book3 = Book('957-7-39-347216-2', 'Learn Maths','John', 'XYZ', 500, 300,5)
	book4 = Book('957-7-39-347216-2', 'Learn Biology','Jack', 'XYZ', 400, 200,6)

	books = [book1, book2, book3, book4]

	for book in books:
		book.display()

	jack_titles = [book.title for book in books if (book.author == "Jack")]
def main_Product():
	p1 = Product('X879', 400, 6)
	p2 = Product('A234', 600, 5)
	p3 = Product('B987', 990, 4)
	p4 = Product('H456', 800, 6)

	products = [p1, p2 , p3, p4]

	for product in products:
		print(f'{product.id}:{product.selling_price}')

	p2.discount = 10
	print(p2.id, p2.selling_price)

def main_Circle():
	c1 = Circle(7)
	print( c1.radius, c1.diameter, c1.circumference, c1.area() )

def main_SalesPerson():
	s1 = SalesPerson('Bob', 25)
	s2 = SalesPerson('Ted', 22)
	s3 = SalesPerson('Jack', 27)
	s1.make_sale(1000)
	s1.make_sale(1200)
	s2.make_sale(5000)
	s3.make_sale(3000)
	s3.make_sale(8000)
def main_Employee():
	e1 = Employee('John','john@gmail.com')
	e2 = Employee('Jack','jack@yahoo.com')
	e3 = Employee('Jill','jill@outlook.com')
	e4 = Employee('Ted','ted@yahoo.com')
	e5 = Employee('Tim','tim@gmail.com')
	e6 = Employee('Mike','mike@yahoo.com')
	print(Employee.domains)
	print(e1.email)
	print(e1.display())
	e1.email = "nam@gmail.com"
	print(e1.email)

def main_Stack():
	st = Stack()
	st.push(5)
	st.push(10)
	st.push(14)
	st.display()
	st.pop()
	st.display()
	st.push(5)
	st.push(10)
	st.push(14)
	st.display()
	st.push(14)
	st.display()
def main_course():
	vc = VideoCourse('Learn C++', 'Jack', 30, 50, 10)
	vc.new_user_enrolled('Allen')
	vc.new_user_enrolled('Max')
	vc.new_user_enrolled('Tom')
	vc.received_a_rating(3)
	vc.received_a_rating(5)
	vc.received_a_rating(4)
if __name__ == "__main__":
	main_course()

