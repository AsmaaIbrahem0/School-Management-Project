# In[]: Import Pacakges

from .person import Person

# In[]: Import Pacakges


class Student(Person):
    """
    A class to represent a student, derived from the Person class.
    Attributes:
        name (str): The name of the student.
        age (int): The age of the student.
        student_id (str): The ID of the student.
        attendance (int): The number of days the student has attended.
    Methods:
        introduce(): Returns a string introducing the student.
        mark_attendance(): Increments the attendance count.
        get_attendance(): Returns the attendance count.
    """

    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.attendance = 0

    def introduce(self):
        """Introduce the student."""
        return f"{super().introduce()} and I am a Student and my ID is: {self.student_id}"

    def mark_attendance(self):
        """Increment the student's attendance count."""
        self.attendance =  self.attendance+ 1

    def get_attendance(self):
        """Return the student's attendance count."""
        return self.attendance
