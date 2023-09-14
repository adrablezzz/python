# class 类

class Person:
    def __init__(self, name) -> None:
        self.name = name

    def say_name(self):
        print(self.name)

    @staticmethod
    def say_hello():
        print('hello')
    
    def __say_yes(self):
        print('yes')


# zs = Person('zs')
# zs.say_name()
# zs.say_hello()
# zs.__say_yes()

# 解析

def foo1():
    return 1,2

a,b = foo1()
print(b)