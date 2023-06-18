'''
注释: #,''''''
严格缩进 
多行语句用 \ 连接
一号
'''
# 输出
print('hello')
# 变量
a = 1
# 连续赋值
b = c = d = 2
e, f, g = 1, 2, 'zs'
# 标准数据类型
'''
Numbers(数字)
String(字符串)
List(列表)
Tuple(元组)
Sets(集合)
Dictionary(字典)
'''
# 数字类型
'''
int(有符号整型)
long(长整型，也可以代表八进制和十六进制)
float(浮点型)
complex(复数)
'''
# 字符串 ''
str1 = 'abcdefg'
str1[1:5]  # 字符串截取 =>bcde
# print(str1[1:5:2])
# 列表 []
l1 = [1, 2, 3, 4]
l2 = [5, 6]
# print(l1[1:3])
# 元组 () 相当于只读列表
t1 = (1, 2)
# 字典 {}
dist = {}
dist['one'] = 1
dist[2] = '22'
# print(dist)
# print(dist.keys())
# print(dist.values())
# 数据类型转换
''' base:进制
int(x [,base]) 代进制参数x为字符串
long(x [,base] ) 3.x移除
float(x)
complex(real [,imag]) 实部,虚部
str(x) 将对象 x 转换为字符串
repr(x) 转换为表达式字符串
eval(str) 用来计算在字符串中的有效Python表达式,并返回一个对象(字符串语句)
tuple(s)
list(s)
set(s)
dict(d) 创建一个字典。d 必须是一个序列 (key,value)元组。
frozenset(s) 转换为不可变集合
chr(x) 将一个整数转换为一个字符
unichr(x) 将一个整数转换为Unicode字符
ord(x) 将一个字符转换为它的整数值
hex(x) 将一个整数转换为一个十六进制字符串
oct(x) 将一个整数转换为一个八进制字符串
'''
# da1 = int('10',2)
# da1 = float('10.2')
# da1 = complex(10, 5)
s = {'a': 1}
da1 = str(s)

print(da1)
