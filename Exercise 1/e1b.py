# Exercise 1(b)

class Toy:
    def __init__(self):
        pass

    def play(self):
        return "Squeak!\n"


class Dog:
    def __init__(self, name):
        self.name = name

    def call(self, shout):
        return shout == "Here, " + self.name + "!"

    def play(self, toy, n):
        return ("Yip! " + toy.play()) * n

    
