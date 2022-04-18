"""
File: student.py
Resources to manage a student's name and test scores.

Added three new methods to compare alphabetical ordering of student names.

Added shuffle and sort list.
"""
import random

class Student(object):
    """Represents a student."""
    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        self.grade = number
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name
  
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]
   
    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self._scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)

    def isNameEqual(self, comparisonStudent):
        """Returns true if the names of the two students are equal."""
        return self.name == comparisonStudent.name

    def isNameLessThan(self, comparisonStudent):
        """Returns true if the student's name is less than the comparison student."""
        return self.name < comparisonStudent.name

    def isNameGreaterThanEqualto(self,comparisonStudent):
        """Returns true if the student's name is greater than or equal to the comparison student."""
        return self.name >= comparisonStudent.name

    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))

def main():
    StudentList = []

    # Define two student objects with similar names.
    Student1 = Student("Bernoulli Jacob", 5)
    Student2 = Student("Bernoulli Johann", 5)

    # Perform comparison.
    print(Student1.name + " comparison with " + Student2.name)
    print("Equal?: " + str(Student1.isNameEqual(Student2)))
    print("Less than?: " + str(Student1.isNameLessThan(Student2)))
    print("Greater than or equal?: " + str(Student1.isNameGreaterThanEqualto(Student2)))

    # Adding Students to the list.
    StudentList.append(Student1)
    StudentList.append(Student2)

    # Showing the shuffled list before sorting.
    random.shuffle(StudentList)

    print("\nAlso,\nShuffled Student list:\n")
    for student in StudentList:
        print(student.name + " - " + str(student.grade))

    #Showcasing the sorted list
    StudentList = sorted(StudentList, key=lambda x: x.name)
    
    print("\nSorted Student list:\n")
    for student in StudentList:
        print(student.name + " - " + str(student.grade))


if __name__ == "__main__":
    main()