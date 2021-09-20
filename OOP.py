import logging
import os


def create_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler("Demo.log", mode= "w")
    file_handler.setFormatter(logging.Formatter(('%(asctime)s - %(filename)s - %(levelname)s - %(funcName)s - %(message)s')))
    logger.addHandler(file_handler)
    return logger

logger = create_logger()
logger.info("Starting Program")

class NameisNotValid(Exception):
    def __init__(self, message, name):
        self.message = message
        self.name = name
class AgeisnotNegative(Exception):
    def __init__(self, message, age):
        self.message = message
        self.age = age

class Person:
    species = "Human"
    count_person = 0
    def __init__(self, name= None, age= None, address= None, phone= None):
        self.name = name # instance variable name
        self.age = age # instance variable age
        self.address = address # instance variable address
        self.phone = phone# instance variable phone
        Person.count_person += 1
    @property
    def get_name(self):
        logger.debug("get name successfully !!")
        return self.name
    @get_name.setter
    def set_name(self, new_name):
        if self.name_check(new_name) is not True:
            raise NameisNotValid("Name is not valid", new_name)
        else:
            self.name = new_name
            logger.debug("set name successfully !!")

    @property
    def get_age(self):
        logger.debug("get age successfully !!")
        return self.age
    @get_age.setter
    def set_age(self, new_age):
        if new_age <= 0:
            raise AgeisnotNegative("Age is negative", new_age)
        else:
            logger.debug("set age successfully !!")
            self.age = new_age

    def display(self):
        logger.debug(f"Name: {self.get_name}\nAge: {self.get_age}\nAddress: {self.address}\nPhone: {self.phone}")
    
    @classmethod
    # if you want to only use class variable , you can make a class method 
    def display_species_of_Person(cls):
        logger.debug(f"Species is {cls.species}")
        logger.debug(f"The created person is {cls.count_person}")
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
        logger(f"Adult: {age > 18}")

    def name_check(self, name):
        if os.path.exists('data.txt'):
            with open('data.txt', mode= 'r') as readFile:
                for line in readFile:
                    if line.lower().startswith(f'name: {self.get_name.lower()}'):
                        logger.error(f'Name: "{self.get_name}" already exists')
                        return False
                if len(self.get_name) == 0:
                    logger.critical(f'Name cannot be blank')
                    return False
                elif not self.get_name.isalpha():
                    logger.critical(f'Name must be an alphabet')
                    return False
                else:
                    logger.debug('Check successfully')
                    return True
        else:
            logger.debug("no data found !!!")
            return True

    def SavetoFile(self, name, age):
        logger.debug(f'saving detals of {self.get_name} ...')
        with open('data.txt', mode= 'a') as appendFile:
            appendFile.writelines(f'Name: {self.get_name} - Age: {self.get_age}\n')
            logger.debug('Details saved successfully !!')

class Employee(Person):
    
    def __init__(self,name, age, address, phone, salary= None, office_address= None, office_phone= None):
        super().__init__(name, age, address, phone)
        self.salary = salary
        self.office_address = office_address
        self.office_phone = office_phone
    def contact_details(self):
        Person.display(self)
        # super().display()
        logger(f'salary: {self.salary}\noffice_address: {self.office_address}\noffice_phone: {self.office_phone}')


logger.info('Ending program !')



# if __name__ == '__main__':
#     # main_person()
#     main_Employee()

#     logger.info("Starting Program")

# e1 = Employee('Jam', 'Smith', 1990, 6000) #  Employee object
# # we will create  a class method name from_employe
# p5 = Person.from_employee(e1)
# p5.display()

# so we could create a Person Object from an Employee object
# to make  a method that needs to access instance variables  ---> insance method
# to make a method that needs to use only class variables --->  class method
# to make a method that needs to use nether instance variable nor class variable ---> static method


