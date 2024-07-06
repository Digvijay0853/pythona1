def square(x):
    return x*x
# print(square(12))

class Duck:

    def talk(self):
        print( 'Quack,Quack .....')
    def walk(self):
        print( 'every duck can walk')

class Dog:

    def talk(self):
        print( 'woof,woof....')

    def walk(self):
        print('every dog can walk')

def execute(obj):
    '''non python way'''
    if type(obj) == Duck:
        obj.talk()
        obj.walk()
    else:
        print('entered object is not a duck object')
#python way
def speak(obj):
    obj.talk()
    obj.walk()


du = Duck()
d = Dog()
speak(du)
speak(d)