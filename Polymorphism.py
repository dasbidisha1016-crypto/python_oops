#polymorphism
#run-time
'''class Animal:
    def sound(self):
        print("Animal sound")
class Dog(Animal):
    def sound(self):
        print("Bark")
class Cat(Animal):
    def sound(self):
        print("Meow")

for s in [Dog(),Cat()]:
    s.sound()'''

#compile-time
class Siri:
    def sound(self,voice=None,year=None):
        if voice and year:
            print(f"SIRI says {voice} in the year {year}")
        elif voice:
            print(f"SIRI says {voice}")
        else:
            print("SIRI !!")

s =Siri()
s.sound()
s.sound("Hello")
s.sound("Hello",2026)


