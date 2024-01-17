# 加载训练好的模型验证
import torch
import numpy as np

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

# 然后用pytorch定义模型
# 这实际上是一个4分类的问题，就是输入数字，看看模型输出的是哪一个类别。

model = torch.load('model.pth')
model.eval()

# 最后用我们训练好的模型尝试在1-100上玩fizzbuzz游戏
start, end = 1, 101
testX = torch.Tensor([binary_encode(i, NUM_DIGITS) for i in range(start, end)])
with torch.no_grad():
  testY = model(testX)
  predictions = zip(range(start, end), list(testY.max(1)[1].data.tolist()))
  # print([fizz_buzz_decode(i, x) for (i, x) in predictions])
  print(np.sum(testY.max(1)[1].numpy() == np.array([fizz_buzz_encode(i) for i in range(start,end)])))
  # print(testY.max(1)[1].numpy() == np.array([fizz_buzz_encode(i) for i in range(start,end)]))


