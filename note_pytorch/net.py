'''Numpy 实现2层神经网络'''
import sys
import numpy as np

# #定义样本数，输入层，隐藏层，输出层的参数
# N, D_in, H, D_out = 64, 1000, 100, 10

# #创造训练样本x,y，这里随着产生
# x = np.random.randn(N, D_in)
# y = np.random.randn(N, D_out)

# #随机初始化参数w1, w2
# w1 = np.random.randn(D_in, H)
# w2 = np.random.rand(H, D_out)

# #下面就是实现神经网路的计算过程
# learning_rate = 1e-6
# epochs = 500
# for epoch in range(epochs):
#     #前向传播
#     h = x.dot(w1)
#     h_relu = np.maximum(h, 0)
#     y_pred = h_relu.dot(w2)
    
#     #计算损失
#     loss = np.square(y_pred-y).sum()
#     print(epoch, loss)
    
#     #反向传播
#     #w2的梯度
#     grad_y_pred = 2.0 * (y_pred - y)
#     grad_w2 = h_relu.T.dot(grad_y_pred)
#     #w1的梯度
#     grad_h_relu = grad_y_pred.dot(w2.T)
#     grad_h = grad_h_relu.copy()
#     grad_h[h<0] = 0
#     grad_w1 = x.T.dot(grad_h)
    
#     #更新参数
#     w1 -= learning_rate * grad_w1
#     w2 -= learning_rate * grad_w2


''' pytorch '''
import torch

# #定义样本数，输入层，隐藏层，输出层的参数
# N, D_in, H, D_out = 64, 1000, 100, 10

# # 随机创建训练数据   这里的np.random.randn换成Pytorch的写法
# x = torch.randn(N, D_in)
# y = torch.randn(N, D_out)

# # 初始化权重
# w1 = torch.randn(D_in, H)
# w2 = torch.randn(H, D_out)

# #下面训练网络，和上面版本过程一致，只不过有些地方换成了Pytorch的写法而已
# learning_rate = 1e-6
# epochs = 500

# for epoch in range(epochs):
#   # 前向传播   矩阵的点乘这里换成了mm
#   h = x.mm(w1)
#   h_relu = h.clamp(min=0)     # 这个张量里面换成了clamp操作，来保证元素取值控制在区间内
#   y_pred = h_relu.mm(w2)

#   # 计算损失   这里要使用张量的item()取出值来
#   loss = (y_pred-y).pow(2).sum().item()
#   print(epoch, loss)

#   # 反向传播, 转置操作换成了t(). copy()换成了clone()
#   # compute the gradient
#   grad_y_pred = 2.0 * (y_pred - y)
#   grad_w2 = h_relu.t().mm(grad_y_pred)
#   grad_h_relu = grad_y_pred.mm(w2.T)
#   grad_h = grad_h_relu.clone()
#   grad_h[h<0] = 0
#   grad_w1 = x.t().mm(grad_h)

#   # 更新参数
#   w1 -= learning_rate  * grad_w1
#   w2 -= learning_rate * grad_w2


'''pytorch:tensor和autograd'''
'''
导数
f(x) = 3x^2 + 2x + 1
f'(x) = 6x + 2
偏导数
f(u,v) = u^3 + v^2 + 4uv
∂u/∂x = 3u^2 + 4v
∂v/∂x = 2v + 4u
'''
# 自动求导例子
# x = torch.tensor(1., requires_grad=True)
# w = torch.tensor(2., requires_grad=True)
# b = torch.tensor(3., requires_grad=True)

# y = w * x + b

# y.backward()      # 求导只需这一句话

# print(w.grad)    # tensor(1.)   也就是x
# print(b.grad)    # tensor(1.)    b求导本身为1
# print(x.grad)     # tensor(2.)   也就是w


# 这里依然不变
# N, D_in, H, D_out = 64, 1000, 100, 10   # N表示训练数据的个数， D_in表示输入的特征数 H是中间层，

# # 随机创建一下训练数据
# x = torch.randn(N, D_in)
# y = torch.randn(N, D_out)

# # 这里随机初始化权重，需要requires_grad=True  需要保留梯度
# w1 = torch.randn(D_in, H, requires_grad=True)
# w2 = torch.randn(H, D_out, requires_grad=True)

# # 开始神经网络计算
# learning_rate = 1e-6
# epoches = 500

# for epoch in range(epoches):
# 	# 前向传播，简单精简一下
# 	y_pred = x.mm(w1).clamp(min=0).mm(w2)
	
# 	# 计算损失和上面一样
# 	loss = (y_pred-y).pow(2).sum()
# 	print(epoch, loss.item())

# 	# 反向传播  这里我们使用自动求导机制，一句话就搞定
# 	loss.backward()

# 	# 更新参数，注意，这时候我们不需要计算w的梯度了，所以得关上梯度计算
# 	with torch.no_grad():
# 		w1 -= learning_rate * w1.grad
# 		w2 -= learning_rate * w2.grad
		
# 		# 这里还有个关键的地方，就是Pytorch的求导机制是默认采用累加的方式，也就是每一代求完梯度，不会自动清零，下一代的梯度是前一代加上本一代的梯度，这时候就错了，所以我们得自动每一代之后，梯度清零
# 		w1.grad.zero_()
# 		w2.grad.zero_()


'''pytorch:nn'''
# 这次先导入nn的库
# import torch.nn as nn
# # 定义输入，中间，输出层的单元数量
# N, D_in, H, D_out = 64, 1000, 100, 10   # N表示训练数据的个数， D_in表示输入的特征数 H是中间层

# # 创建训练数据，和上面一样
# x = torch.randn(N, D_in)
# y = torch.randn(N, D_out)

# # 这里我们不定义w了，使用nn建立一个模型进行前向传播的过程计算,这里建模型，就类似于Keras的Sequential了，非常方便
# model = nn.Sequential(
# 	nn.Linear(D_in, H),
# 	nn.ReLU(),
# 	nn.Linear(H, D_out)
# )
# # 这里我们初始化一下子我们的参数(这一步非关键，但是初始化完了之后发现训练的效果好，你可以对比看看，不加这两句的话增大学习率也可以)
# # nn.init.normal_(model[0].weight)
# # nn.init.normal_(model[2].weight)

# # 开始神经网络的计算
# loss_fn = nn.MSELoss(reduction='sum')
# learning_rate = 1e-6

# for it in range(500):
# 	# 前向传播，建立模型即可, 也是一句话搞定
# 	y_pred = model(x)
	
# 	# 计算损失  这里的损失函数用Pytorch版
# 	loss = loss_fn(y_pred, y)
# 	# print(it, loss.item())

# 	# 参数导数归0，然后反向传播，这里会计算所有需要求导参数的梯度保存到一个参数列表中
# 	model.zero_grad()
# 	loss.backward()

# 	# 更新参数, 这个地方注意，使用model之后，反向传播得到的参数会在一个参数列表中model.parameters() 我们需要在这里面求出参数来进行改变
# 	with torch.no_grad():
# 		for param in model.parameters():  # param (tensor, grad)的形式
# 			param -= learning_rate * param.grad


'''pytorch:optim'''
# 这一次我们不再手动更新模型的weights,而是使用optim这个包来帮助我们更新参数

# # 定义输入输出层的个数 和上面一样
# N, D_in, H, D_out = 64, 1000, 100, 10

# # 创造训练集
# x = torch.randn(N, D_in)
# y = torch.randn(N, D_out)

# # 定义模型
# model = torch.nn.Sequential(
# 	torch.nn.Linear(D_in, H),
# 	torch.nn.ReLU(),
# 	torch.nn.Linear(H, D_out)
# )

# # 如果训练效果不好，也可以加上这两句试试，深度学习有点玄学
# #torch.nn.init.normal_(model[0].weight)
# #torch.nn.init.normal_(model[2].weight)

# # 开始神经网络的计算,但是这里我们使用优化器帮我们更新参数
# learning_rate = 1e-6
# loss_fn = torch.nn.MSELoss(reduction='sum')
# optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

# for it in range(500):
# 	# 前向传播
# 	y_pred = model(x)

# 	# 计算损失
# 	loss = loss_fn(y_pred, y)
# 	print(it, loss.item())

# 	# 梯度清零, 然后反向传播
# 	optimizer.zero_grad()
# 	loss.backward()

# 	# 更新参数，这里只需要一句话
# 	optimizer.step()


'''pytorch：自定义nn Modules'''

# # 我们定义一个两层的神经网络类，这个继承与nn.Module模块
class TwoLayerNet(torch.nn.Module):
	
	# 定义成员层
	def __init__(self, D_in, H, D_out):
		super(TwoLayerNet, self).__init__()
		self.linear1 = torch.nn.Linear(D_in, H)
		self.linear2 = torch.nn.Linear(H, D_out)
	
	# 定义前向传播
	def forward(self, x):
		h_relu = self.linear1(x).clamp(min=0)
		y_pred = self.linear2(h_relu)
		return y_pred

# # 这样就定义了一个二层神经网络的类

# N, D_in, H, D_out = 64, 1000, 100, 10

# x = torch.randn(N, D_in)
# y = torch.randn(N, D_out)

# # 定义一个模型
# model = TwoLayerNet(D_in, H, D_out)

# # 开始计算神经网络
# criterion = torch.nn.MSELoss(reduction='sum')
# optimizer = torch.optim.SGD(model.parameters(), lr=1e-4)

# for it in range(500):
# 	# 前向传播
# 	y_pred = model(x)

# 	# 计算损失
# 	loss = criterion(y_pred, y)
# 	print(it, loss.item())

# 	# 反向传播, 更新参数
# 	optimizer.zero_grad()
# 	loss.backward()
# 	optimizer.step()

'''
教网络玩FizzBuzz小游戏
FizzBuzz时一个简单的小游戏。游戏规则如下：从1开始往上数数，当遇到3的倍数的时候，说fizz，当遇到5的倍数，说buzz，当遇到15的倍数，就说fizzbuzz,其他情况下则正常数数。
'''

# 先写一个编码函数
def fizz_buzz_encode(i):
	if i % 15 == 0: return 3
	elif i % 5 == 0: return 2
	elif i % 3 == 0: return 1
	else: return 0

# 我们写一个解码函数，就是根据上面的返回数，我们得到fuzz，buzz还是别的
def fizz_buzz_decode(i, prediction):
	return [str(i), "fizz", "buzz", "fizzbuzz"][prediction]


NUM_DIGITS = 15

def binary_encode(i, num_digits):
	return np.array([i >> d & 1 for d in range(num_digits)])

# 准备训练集
trX = torch.Tensor([binary_encode(i, NUM_DIGITS) for i in range(101, 2 ** NUM_DIGITS)])
trY = torch.LongTensor([fizz_buzz_encode(i) for i in range(101, 2 ** NUM_DIGITS)])

# 然后用pytorch定义模型
# 这实际上是一个4分类的问题，就是输入数字，看看模型输出的是哪一个类别。

NUM_HIDDEN = 160
# 单层模型 正确率:100 97
# model = torch.nn.Sequential(
# 	torch.nn.Linear(NUM_DIGITS, NUM_HIDDEN),
# 	torch.nn.ReLU(),
# 	torch.nn.Linear(NUM_HIDDEN, 4)
# )
# 双层模型 正确率:100 100 2次稳定
model = TwoLayerNet(NUM_DIGITS, NUM_HIDDEN, 4)
# 参数改为(NUM_DIGITS=15,NUM_HIDDEN=160) 

# 模型的训练
'''
-为了让我们的模型学会FizzBuzzz这个游戏，我们需要定义一个损失函数，和一个优化算法
-这个优化算法会不断优化(降低)损失函数，使得模型的在该任务上取得尽可能低的损失值
-损失值低往往表示我们的模型表现好，损失值高表示我们的模型表现差
-由于FizzBuzz游戏本质上是一个分类问题，我们选用Cross Entropy Loss函数
-优化函数我们选用Stochastic Gradient Descent.
'''
loss_fn = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr = 0.05)
BATCH_SIZE = 128


for epoch in range(1000):
	for start in range(0, len(trX), BATCH_SIZE):
		end = start + BATCH_SIZE
		batchX = trX[start:end]
		batchY = trY[start:end]

		y_pred = model(batchX)
		loss = loss_fn(y_pred, batchY)

		optimizer.zero_grad()
		loss.backward()
		optimizer.step()
	
	loss = loss_fn(model(trX),trY).item()
	print(epoch, loss)
	
# 保存模型
torch.save(model, 'model.pth')

# 最后用我们训练好的模型尝试在1-100上玩fizzbuzz游戏
testX = torch.Tensor([binary_encode(i, NUM_DIGITS) for i in range(1, 101)])
with torch.no_grad():
  testY = model(testX)
  predictions = zip(range(1, 101), list(testY.max(1)[1].data.tolist()))
  print([fizz_buzz_decode(i, x) for (i, x) in predictions])

  print(np.sum(testY.max(1)[1].numpy() == np.array([fizz_buzz_encode(i) for i in range(1,101)])))
  print(testY.max(1)[1].numpy() == np.array([fizz_buzz_encode(i) for i in range(1,101)]))