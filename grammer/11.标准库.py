# os 操作系统处理
import os
# print(os.getcwd())
# os.chdir('./out')
# print(os.getcwd())
# os.system('mkdir dir1')

# glob 文件通配符
import glob
# os.chdir('./grammer')
# print(glob.glob('*.py'))

# sys 命令行参数
import sys
# print(sys.argv)
# sys.exit() # 终止程序

# re 正则
import re
# res = re.findall(r'\bf[a-z]*', 'which is the fools feet')
# print(res)

# math 数学
import math
# print(math.pi)

# random 随机数
import random
# print(random.choice([1,2,3]))
# print(random.sample(range(10), 3))
# print(random.randrange(2))

# 访问互联网
from urllib.request import urlopen
# web1 = urlopen('http://baidu.com')
# print(web1)

# datetime 日期事件
from datetime import date
# print(date.today())
# print(date(2023, 12, 1))

# 数据压缩 zlib，gzip，bz2，zipfile，以及 tarfile

# 性能度量 
from timeit import Timer
# print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
# print(Timer('a,b = b,a', 'a=1; b=2').timeit())

# 测试模块
# import doctest
# doctest.testmod()

# import unittest
# unittest.main()