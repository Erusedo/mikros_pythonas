class Student:    #this is a class, to define what a student is
    
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name 
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer