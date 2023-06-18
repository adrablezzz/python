# 温度转换
def exchange():
  c = eval(input('请输入摄氏度'))
  f = 9/5 * c + 32
  print(c,"摄氏度的华氏温度是：",f,"华氏度")

# exchange()

def fn1():
  # print("不换行", end=" ")
  print("换行", end="\n")
  print(3 + 2)

# fn1()

def fn2():
  name = input("请输入名字：")
  print("你是",name)

# fn2()

def fn3():
  name, age = "张三", 18
  print(name,age,"岁了")

# fn3()

def fn4():
  # x = eval(input("请输入本金"))
  for i in range(0):
    # x *= 1 + 0.2
    print("hi")
  # print(x)

# fn4()

import math
# ax^2 + bx + c = 0
def fn5():
  a = float(input("a:"))
  b = float(input("b:"))
  c = float(input("c:"))
  t = math.sqrt(b**2 - 4*a*c)
  root1 = (-b + t) / 2*a
  root2 = (-b - t) / 2*a
  print("该方程在此处的两个解为：",root1,root2)

fn5()