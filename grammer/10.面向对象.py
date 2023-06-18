'''
Python3 面向对象技术简介

    类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
    类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
    数据成员：类变量或者实例变量用于处理类及其实例对象的相关的数据。
    方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
    局部变量：定义在方法中的变量，只作用于当前实例的类。
    实例变量：在类的声明中，属性是用变量来表示的。这种变量就称为实例变量，是在类声明的内部但是在类的其他成员方法之外声明的。
    继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个 Dog 类型的对象派生自 Animal 类，这是模拟"是一个（is-a）"关系（例图，Dog 是一个 Animal）。
    实例化：创建一个类的实例，类的具体对象。
    方法：类中定义的函数。
    对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。
'''

# class 类(大小驼峰)
class Person:
    # 基本属性
    name = ''
    age = 0
    # 私有属性
    __id = 30
    # 构造方法
    def __init__(self, name='user', age=0) -> None:
        self.name = name
        self.age = age
    def say(self):
        # return 'my name is ' + self.name
        print('i am %s, %d years old now' %(self.name, self.age))

# p1 = Person('zhangsan', 18)
# p1.say()

# 继承
class Child(Person):
    hunger = 0
    def __init__(self, name='user', age=0, hunger=0):
        super().__init__(name, age)
        self.hunger = hunger
    def shout(self):
        if(self.hunger):
            print('crying crying ...')
        else:
            print('ha ha ha...')
# child1 = Child('lilie', 6, 1)
# child1.shout()

# 多继承 
# class Baby(Person, Child):

# 私有方法 
# def __myFn(self)

# 专有方法
'''
__init__ : 构造函数，在生成对象时调用
__del__ : 析构函数，释放对象时使用
__repr__ : 打印，转换
__setitem__ : 按照索引赋值
__getitem__: 按照索引获取值
__len__: 获得长度
__cmp__: 比较运算
__call__: 函数调用
__add__: 加运算
__sub__: 减运算
__mul__: 乘运算
__div__: 除运算
__mod__: 求余运算
__pow__: 乘方
'''

# 运算符重载
class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b

   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)
   
   def __add__(self,other):
      return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)
print (v1 + v2) # =》 Vector(7,8)