#!/usr/bin/python3
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def saludar(self):
        print(f"hola mi nombre es {self.name} y tengo {self.age}")
    
class Estudiante(Person):
    def __init__(self, name, age, curso):
        super().__init__(name, age)
        self.curso = curso
    def presentarse(self):
        print(f"Hola, mi nombre es {self.name}, tengo {self.age} años y estoy en el curso de {self.curso}")
    
class Estudiante1(Estudiante):
    def presentarse(self):
        super().presentarse()

p = Estudiante1("juan", 10, "progra")
p.presentarse()