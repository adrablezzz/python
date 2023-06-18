# import sys
# from ... import *

# if __name__ == '__main__':
#     print('程序自身在运行')
# else:
#     print('我来自另一模块')

# print(dir()) #返回模块属性列表


# 输入输出 print() write()  sys.stdout
# str() repr()

# print('{} is {} years old'.format('zhangsan', 18))
# print('{0} is {1} years old'.format('zhangsan', 18))
# print('{1} is {0} years old'.format('zhangsan', 18))
# print('{0} is {age} years old'.format('zhangsan', age=18))
# '!a' (使用 ascii()), '!s' (使用 str()) 和 '!r' (使用 repr()) 可以用于在格式化某个值之前对其进行转化:
# print('The value of PI is approximately {0:.3f}.'.format(3.1415926)) # :.3f 保留3位小时 浮点型
# print('{0:10} ==> {1:10d}'.format('zhangsan', 119)) # :10d 确保字符宽度至少为10 整数型

# table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
# print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
#         'Dcab: {0[Dcab]:d}'.format(table))
# print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

# print('The value of PI is approximately %5.3f.' % 3.1415926) # %格式化


# 读写文件
# open(filename, mode) mode: r w a r+ 只读 只写 追加 读写
dataUrl = 'D:\Study\python\grammer\data.txt'
# f = open(dataUrl, 'rb+')
# print(f.read())
# print(f.readline())
# print(f.readline())
# print(f.readlines())

# f.write('hello')
# print(f.read())

# print(f.tell())
# f.write(b'0123456789abcdefg')
# f.seek(1, 2) #?

# f.close() #关闭打开模式没有b的文件


# pickle 模块 ?
# pickle.dump(obj, file, [,protocol])
# import pickle

# data1 = {'a': [1, 2.0, 3, 4+6j],
#          'b': ('string', u'Unicode string'),
#          'c': None}

# selfref_list = [1, 2, 3]
# selfref_list.append(selfref_list)

# output = open('data', 'wb')

# # Pickle dictionary using protocol 0.
# pickle.dump(data1, output)

# # Pickle the list using the highest protocol available.
# pickle.dump(selfref_list, output, -1)

# output.close()


# os 模块提供了非常丰富的方法用来处理文件和目录：略

# 异常
# try:
#   x = int(input('请输入整数：'))
# except ValueError: # 捕获到xx错误
#   print('输入错误')
#   raise # 抛出异常
# # except xxx
# # ...
# else: # 没有捕获到异常
#   print('输入正常')
# 自定义异常
# class MyError(Exception):
#     def __init__(self, value):
#         self.value = value

#     def __str__(self):
#         return repr(self.value)


# try:
#     raise MyError(2*2)
# except MyError as e:
#     print('My exception occurred, value:', e.value)