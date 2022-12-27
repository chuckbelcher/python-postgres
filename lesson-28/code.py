# Non-ObjectOriented
student = {"name": "Rolf", "grandes": (90,89,93,78,90)}

def average(sequence):
    return sum(sequence) / len(sequence)

print(average(student["grandes"]))

#Object Oriented
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f"{self.name}, has an average grade of {self.average()}"
    
    def __repr__(self):
        return f"<Student '{self.name}', {self.grades}>"
  

bob = Student("Bob", (90,89,93,78,90))
rolf = Student("Rolf", (90,93,93,81,90))
print(bob.name)
print(bob.average())
print(rolf.name)
print(rolf.average())
print(bob)
