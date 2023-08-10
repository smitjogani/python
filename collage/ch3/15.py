# write program to check the object type to know whether the method exists in the object or not

class Dog:
    def bark(self):
        print("Bow, wow !")
    
class Duck:
    def talk(self):
        print("Quark, quack!")

class Human:
    def talk(self):
        print("Hii, hello!")

def call_talk(obj):
    if hasattr(obj, 'talk'):
        obj.talk()
    elif hasattr(obj, 'bark'):
        obj.bark()
    else:
        print("Wrong object is passed...")

x = Duck()
call_talk(x)

x = Human()
call_talk(x)

x = Dog()
call_talk(x)