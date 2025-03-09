# In[]: Import Pacakges

from .student import Student
from .teacher import Teacher

# In[]:


class School:
    """
    A class to represent a school.
    Attributes:
        name (str): The name of the school.
        people (list): A list of people (students and teachers) in the school.
    Methods:
        add_person(person): Adds a person to the school.
        show_all_people(): Prints introductions of all people in the school.
        mark_attendance(name): Marks attendance for a specific person by name.
        generate_report(): Generates a report of all people in the school, including their name, age, role, and attendance.
    """

    def __init__(self, name):
        self.name = name
        self.people = []

    def add_person(self, person):
        """Add a person to the school."""
        print(f"{person.name} was added")
        self.people.append(person)

    def show_all_people(self):
        """Print introductions of all people in the school."""
        for person  in self.people:
            print(person.introduce())

    def mark_attendance(self, name):
        """Mark attendance for a specific person by name."""
        for person in self.people:
            if self.name == name:
                person.mark_attendance()
                print(f"Attendance for {name} has been marked. Total: {person.get_attendance} day(s).")
                return
    def generate_report(self):
        """Generate a report of all people in the school."""
        print("Name            Age          Role         Attendence ")
        print("-" * 55)
        for person in self.people:
            role = person.__class__.__name__
            print(f"{person.name}           {person.age}         {role}          {person.get_attendance()}")
