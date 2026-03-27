"""
Inheritance
In this challenge, we practice using inheritance. Check the attached tutorial for more details.
Task
You are given two classes, Person and Student, where Person is the base class and Student is
the derived class. Completed code for Person and a declaration for Student are provided in the editor. Observe that Student inherits all the properties of Person.
Complete the Student class by writing the following:
A Student class constructor, which has 4 parameters:
A string, firstName.
A string, lastName.
An integer, id.
An integer array (or vector) of test scores, scores.
A char calculate() method that calculates a Student object's average and returns the grade character representative of their average score:
O for 90 <= average <= 100
E for 80 <= average < 90
A for 70 <= average < 80
P for 55 <= average < 70
D for 40 <= average < 55
T for average < 40
Input Format
The locked stub code in your editor reads input from stdin and passes it to the Student class constructor. It also calls the calculate method and prints the grade returned.
The first line contains firstName, lastName, and id, separated by a space. The second line contains the number of test scores. The third line of input contains the space-separated test scores.
Constraints
1 <= |firstName|, |lastName| <= 10
1 <= id <= 10^7
0 <= scores[i] <= 100
Output Format
Output is handled by the locked stub code in the editor. Your output will be correct if your Student class constructor and calculate() method are properly implemented.
Sample Input
Heraldo Memelli 8135627
2
100 80
Sample Output
Name: Memelli, Heraldo
ID: 8135627
Hence Grade: O
Explanation
The student has two test scores: 100 and 80. The average is (100 + 80) / 2 = 90. Since 90 is between 90 and 100, the grade is O.

"""
class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    # Write your function here
    def calculate(self):
        avg = sum(self.scores) / len(self.scores)
        print("So Avg: " , avg)
        if avg >= 90 and avg <= 100:
            return 'O'
        elif avg >= 80 and avg < 90:
            return 'E'
        elif avg >= 70 and avg < 80:
            return 'A'
        elif avg >= 55 and avg < 70:
            return 'P'
        elif avg >= 40 and avg < 55:
            return 'D'
        else:
            return 'T'

if __name__ == '__main__':
    line = input().split()
    firstName = line[0]
    lastName = line[1]
    idNum = line[2]
    numScores = int(input()) # not needed for Python
    scores = list( map(int, input().split()) )
    s = Student(firstName, lastName, idNum, scores)
    s.printPerson()
    print("Hence Grade:", s.calculate())