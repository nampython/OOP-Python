import logging
from OOP import Person, Employee


def create_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler("main.log", mode= "w")
    file_handler.setFormatter(logging.Formatter(('%(asctime)s - %(levelname)s - %(message)s')))
    logger.addHandler(file_handler)
    return logger
logger = create_logger()
logger.info('Starting main.py')


def main_person():
    person_1 = Person("Nam", 21, "Quang binh", "0395371244") # Person Object
    person_2 = Person("Thin", 50, "Ho Chi Minh", "0395323123")
    person_3 = Person("Quang", 9, "Quang binh", "0395337211")
    # we can  make a class method to create  a Person object from this type of dictionary
    person_4 = Person.from_str("Quan, 10")
    person_5 = Person.from_dict({"name": "Hai", "age": 30})
    person_list = [person_1, person_2, person_3, person_4, person_5]
    return person_list

def main_Employee():
    employee1 = Employee("nam", 21, "Hcm", "0395337211", '7.000.000', "New York", '133' )
    employee1.contact_details()
    print(employee1.get_name)

def AddintoFile(person_list):
    for person in person_list:
        if person.name_check(person.get_name) is True:
            person.SavetoFile(person.get_name, person.get_age)
        else:
            logger.critical("Person check fail")

    

if __name__ == "__main__":
    AddintoFile(main_person())


logger.info('Ending main.py')