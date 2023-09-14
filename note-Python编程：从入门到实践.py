# 1. 数据结构
'''
 布尔 True False
 字符串 str
 数字 int float
 列表 [] list
 元组 () tuple
 字典 {} dict
'''

# 1.1 字符串
a = 'hello world'
# 1.1.1 字符串方法
# 首字母大小
a.title()
# 全大/小写
a.upper()
a.lower()
# 合并 +
# 制表符 \t
# 去除开头结尾空白
a.rstrip()

# 1.2 数字
# 1.2.1 整型 int
# + - * / % // ** # //整除向下取整
# 1.2.2 浮点型 float
# 数字转字符 str(1)

# 1.3 列表 []
list1 = ['zs', 'ls', 'ww', 'ab']
# 1.3.1 访问列表
list1[0]  #访问第1位
list1[-1]  #访问倒数第1位
list1[0:2] #访问1-2位，返回列表
list1[:2] #从头开始到第2位
list1[2:] #从第2位开始到末尾
# 1.3.2 修改列表
list1[0] = 'zhangsan'
# 1.3.3 添加元素
list1.append('zhaoliu') # 末尾填写
list1.insert(1, 'shengqi') # 指定位置插入
# 1.3.4 删除元素
del list1[1] # 指定位置删除
list1.pop() # 删除末尾，改变原列表，返回值
list1.pop(2) # 指定位置删除，改变原列表，返回删掉的值
list1.remove('ls') # 根据值删除，（只删除找到的第一个，没找到会报异常）
# 1.3.5 组织列表
list1.sort() # 永久排序(改变原列表)
sorted(list1) # 临时排序(不改变原列表)，返回排序的列表
list1.reverse() # 反转列表
len(list1) # 获取列表长度
# 1.3.6 操作列表
# 1.3.6.1 遍历列表
# for item in list1:
#   print(item)
# 1.3.3.2 创建数值列表
# range遍历
# for i in range(0, 5):
#   print(i)
# 创建列表
list2 = list(range(0,5))
# 创建列表，指定步长
list3 = list(range(0,10,2))
# 1.3.7 列表统计
min(list2)
max(list2)
sum(list2)
# 1.3.8 列表解析
list4 = [value**2 for value in range(1, 10)]
# 将1-9赋值给value,返回value**2并解析给列表
# 1.3.9 复制列表
list2_copy = list2[:] # 不改变原列表

# 1.4 元组
# 1.4.1 定义
tuple1 = (1,2) 
tuple2 = (1,) 
# 元组不可变
# tuple1[0] = 99 #err
# 元组变量只能重新赋值
tuple1 = (3,4)

# 1.5 字典
# 1.5.1 创建字典
dict1 = {'name': 'zhang san', 'age': 20}
# 1.5.2 访问字典
dict1['name']
# 1.5.3 增改删
dict1['address'] = 'cn'
dict1['age'] = 21
del dict1['address']
# 1.5.4 遍历字典
# for key,value in dict1.items():
#   print(key, value)
# for key in dict1.keys():
#   print(key)
# for value in dict1.values():
#   print(value)
# 1.5.5 嵌套
# 1.5.5.1 字典列表
persons = [{'name': '张三', 'age': 20}, {'name': '李四', 'age': 25}]
# 1.5.5.2 列表字典
dog1 = {
  'name': 'aHuang',
  'hobbies': ['ball', 'hang out'] 
}
# 1.5.5.3 嵌套字典
person1 = {
  'name': 'ZhangSan',
  'pet': dog1
}

# 2. 分支语句
# 2.1 if语句
# age = int(input('请输入年龄(整数)：'))
# if age >= 60:
#   print('you are retired')
# elif age >= 18:
#   print('you are adult')
# else:
#   print('you are young')
# 数值比较 ==; >=; <=; !=;
# 是否在列表/字符串中 in; not in;
# 条件关系 or and
# 布尔关系 a == 1 ? 'a等于1'

# 2.0 用户输入
# age = input('请输入整数：')
# 获取输入的数值
# int(age)

# 2.2 while 循环
# index = 1
# while index < 5:
#   # if index == 2:
#   #   break #终止循环
#   if index == 3:
#     index += 1
#     continue #跳过
#   print(index)
#   index += 1



# 3. 函数
# 3.1 形参,实参
def greet(who, greeter):
  print('hello {0}, from {1}.'.format(who, greeter))

# 形参默认值
def ask(a='zs', b='lis'):
  print('{} ask {}'.format(a, b))
# 关键字传参
# ask(b='zhaoliu')
# 3.2 返回值
def sum(num1, num2):
  return num1 + num2
# 3.3 传递任意数量的实参
def count_name(teacher, *names):
  print(teacher, 'is counting',*names)
# count_name('Mr.Wang', 'zs', 'ls')



# 4. 模块
# 4.1 定义模块 tools.py
# 4.2 引入模块
# import tools
# c = tools.sum(1,2)
# print(c)
# 引入模块的特定方法,并起别名
# from tools import sum as sumNum
# print(sumNum(2,2))
# from tools import * 导入所有模块




# 5. 类
# 5.1 创建类
class Person:
  name = ''
  def __init__(self, name) -> None: # 初始化函数
    self.name = name
  def say(self, word):
    print('{} say: {}'.format(self.name, word))
# 创建实例
zs = Person('zs')
# 调用方法
# zs.say('ni hao')

# 5.2 继承
class Baby(Person):
  def say(self): # 方法重写
    print('{} say: {}'.format(self.name, '!#%$$#a;?'))
b1 = Baby('fufu')
# b1.say()
# 5.3 导入类 
# from tools import Person, Baby




# 6. 文件和异常
# 6.1 打开文件
# with open('text.txt', encoding='utf-8') as f:
#   # print(f.read())
#   # 逐行读取
#   for line in f:
#     print(line.rstrip())

# 6.2 写入文件
# with open('text.txt', 'a') as f:
#   f.write('abc\n')

# 6.3 异常
# try:
#   print(2/1)
# except ZeroDivisionError:
#   print('zero err')
# else:
#   print('success')




# 7.pygame