class Person():
    species = "Human"
    count_person = 0
    def __init__(self, name, age, address= None, phone= None):
        self.name = name # instance variable name
        self.age = age # instance variable age
        self.address = address # instance variable address
        self.phone = phone# instance variable phone
        Person.count_person += 1
    def display(self):
        print(f"I'm {self.name} \nI'm {self.age} year olds\nPhone: {self.phone}\nAddress: {self.address}")
    
    @classmethod
    # if you want to only use class variable , you can make a class method 
    def display_species_of_Person(cls):
        print("--------class method----------")
        print(f"Species is {cls.species}")
        print(f"The created person is {cls.count_person}")
        print("-----------------------------")
    @classmethod
    def from_str(cls, s):
        name, age = s.split(",")
        return cls(name, int(age))
    @classmethod
    def from_dict(cls, d):
        return cls(d['name'], d['age'])
    # @classmethod
	# def from_employee(cls,emp):
	# 	name = emp.first_name + emp.last_name
	# 	age = datetime.today().year - emp.birth_year
	# 	return cls(name, age)
    @staticmethod
    #we can see that unlike  instance method and class methods, a static method does not have any special frist paramter.
    def isAdult(age):
        print("--------static method----------")
        print(f"Adult: {age > 18}")
        print("-----------------------------")

if __name__ == '__main__':
    person_1 = Person("Nam", 21, "Quang binh", "0395371244") # Person Object
    person_2 = Person("Thin", 50, "Ho Chi Minh", "0395323123")
    person_3 = Person("Quang", 9, "Quang binh", "0395337211")
    # we can  make a class method to create  a Person object from this type of dictionary
    person_4 = Person.from_str("Quan, 10")
    person_5 = Person.from_dict({"name": "Hai", "age": 30})
    
    person_1.display()
    person_1.display_species_of_Person()
    person_1.isAdult(21)
    person_4.display()
    person_5.display()


# e1 = Employee('Jam', 'Smith', 1990, 6000) #  Employee object
# # we will create  a class method name from_employe
# p5 = Person.from_employee(e1)
# p5.display()

# so we could create a Person Object from an Employee object
# to make  a method that needs to access instance variables  ---> insance method
# to make a method that needs to use only class variables --->  class method
# to make a method that needs to use nether instance variable nor class variable ---> static method