# 迭代器
list1 = [1,2,3,4]
iter1 = iter(list1)
# for i in iter1:
#   print(i)

def fn1(i):
  import sys
  while True:
    try:
      print(next(i))
    except StopIteration:
      sys.exit()



# 生成器 yeild 返回迭代器
def fibonacci(n):
  a, b, counter = 0, 1, 0
  while True:
    if(counter > n):
      return
    yield a
    a, b = b, a + b
    counter += 1
f = fibonacci(10)
fn1(f)

