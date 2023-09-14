# 三者最大
def fn1(a, b, c):
    return a if a > b else b if b > c else c

# print(fn1(50,10,3))

# 随机
from random import randrange

class Person:
    name = ''
    goal = 0
    records = []
    def __init__(self, name) -> None:
        self.name = name
        self.goal = 0
        self.records = []

    def play(self, times=1) -> None:
        for i in range(times):
            goal = randrange(0, 10)
            self.records.append(goal)
            self.goal += goal
        print('{} 玩了{}把，共得了{}分'.format(self.name, times, self.goal))
        print(self.records)
        return self.goal

def fn2(): 
    zs = Person('zs')
    zs.play(10)

    ls = Person('ls')
    ls.play(10)

    if(zs.goal == ls.goal):
        print('平了')
    else:
        print('{}赢了'.format(zs.name if zs.goal > ls.goal else ls.name))

fn2()


