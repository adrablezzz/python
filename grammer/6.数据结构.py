# 详:w3cschool
# list 列表
list1 = []
list1.append(1)
list1.extend([2,3])
list1.insert(1,4) 
list1.remove(4)
list1.pop(1)
list1.pop()
list1.clear()
list1.extend([1,1,3,4,-2])
# print(list1.index(1,1,4))
# print(list1.count(1))
list1.sort()
list1.reverse()
list2 = list1.copy()
list1.pop()
# print(list2)
# print(list1)
# 访问元素 list1[0] list1[-1] list1[1:3] list1[1:]

# tuple 元组(相当于只读列表)
tuple1 = (1,)
tuple2 = 1,2,3
# del tuple1
# len()
# tuple1 + tuple2 连接
# tuple2 * 4 复制
# 2 in tuple2 -> True
# for i in tuple2: print(x);
# 访问元素与数组相同
# 函数 len(tuple1) max(tuple1) min(tuple1) tuple(tuple1) operator(tuple1, tuple2)比较
# print(tuple2)

# dict 字典
dict1 = {'name': 'zs'}
dict1['name']
dict1['name'] = 'ls'
# del dict1['name']
# 函数： len(dict1) str(dict1) type(dict1)
'''
字典方法：
dict1.clear()
dict1.copy()
dict1.fromkeys()
dict1.get(key,default=None)
key in dict1
dict1.items()
dict1.keys()
dict1.setdefault(key,default=None)
dic1.update(dict2) 吧dict2的键值更新到dict1
dic1.values()
'''

# set 集合
'''
set1 = {2,3,4,5}
set1.add(1)
set1.update(1)
set1.remove(1)
set1.discard(2)
len(set1)
set1.clear()
set1.pop()
3 in set1
set1.copy()
set1.difference(set2) #返回两个集合的差集
set1.difference_update(set2) #移除两个集合中都存在的元素
set1.intersection(set2) 交集
set1.intersection_update(set2) 返回交集,并删除父集合中不相交的元素
set1.union(set2) 并集
# 略
'''