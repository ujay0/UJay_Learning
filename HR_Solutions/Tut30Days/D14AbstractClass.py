"""
Abstract classes are classes that contain one or more abstract methods. An abstract method is a method that is declared, but contains no implementation. Abstract classes cannot be instantiated, and require subclasses to provide implementations for the abstract methods.
In Python, we can use the abc module to create abstract classes. The abc module provides the ABCMeta class and the abstractmethod decorator to define abstract classes and methods.
In this challenge, we are given an abstract class Book and a concrete class MyBook that inherits
from Book. The Book class has an abstract method display() that we need to implement in the MyBook class. The MyBook class should have a constructor that takes three parameters: title, author, and price. The display() method should print the title, author, and price of the book in a specific format.
"""

from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

#Write MyBook class
class MyBook(Book):
    def __init__(self,title,author, price):
        super().__init__(title,author)
        self.price= price
        
    def display(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: {self.price}")

if __name__ == '__main__':    
    title=input()
    author=input()
    price=int(input())
    new_novel=MyBook(title,author,price)
    new_novel.display()