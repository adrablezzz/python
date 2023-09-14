# 列表查找返回索引
def search1(x, list):
    try:
        return list.index(x)
    except:
        return -1

# a = search1(1, [2,3])
# print(a)

def search2(x, list):
    for i in range(len(list)):
        if(list[i] == x):
            return i
    return -1

# a = search2(1, [1,2,3])
# print(a)

# 二分查找顺序列表 [] mid []
def binarySearch(x, list):
    min = 0
    max = len(list) - 1
    while(min <= max):
        mid = (min + max) // 2
        if(list[mid] == x):
            return mid
        elif(list[mid] < x):
            min = mid + 1
        else:
            max = mid - 1
    return -1

# a = binarySearch(4, [1,2,3,4,5])
# print(a)

# 递归
def fact(n):
    if(n == 0):
        return 1
    else:
        return n * fact(n-1)
    
# a = fact(4)
# print(a)

def reverse(s):
    if s == '':
        return s
    else:
        return reverse(s[1:]) + s[0]
    
# a = reverse('abc')
# print(a)

# 重组词
def anagrams(s):
    if s == '':
        return [s]
    else:
        ans = []
        for item in anagrams(s[1:]):
            for index in range(len(item) + 1):
                ans.append(item[:index] + s[0] + item[index:])
        return ans
# a = anagrams('abc')
# print(a)

# 指数
# x^n = x^(n//2) * x^(n//2) n为奇数
#       x^(n//2) 8 x^(n//2) * x  n为偶数
def myPower(x, n):
    if n == 0:
        return 1
    else:
        factor = pow(x, n // 2)
        if n % 2 == 0:
            return factor * factor
        else:
            return factor * factor * x
        
# a = myPower(2, 5)
# print(a)

def myPower1(x, n):
    if n == 0:
        return 1
    ans = 1
    for i in range(n):
        ans *= x
    return ans

# a = myPower1(2, 5)
# print(a)
