'''
导数
f(x) = 3x^2 + 2x + 1
f'(x) = 6x + 2

偏导数
f(u,v) = u^3 + v^2 + 4uv
∂u/∂x = 3u^2 + 4v
∂v/∂x = 2v + 4u
'''


import torch
import matplotlib.pyplot as plt
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

# x = torch.tensor(3.0, requires_grad=True)
# print(x)
# y = 3 * x ** 2
# # y' = 6x
# y.backward()
# print('y在x=3.的导数为：{}'.format(x.grad))


# u = torch.tensor(3.0, requires_grad=True)
# v = torch.tensor(4.0, requires_grad=True)
# f = u**3 + v**2 + 4*v*u
# print(u,v,f)
# f.backward()
# print('对u的偏导: {}'.format(u.grad))
# print('对v的偏导: {}'.format(v.grad))


# x = torch.linspace(-20,20,20, requires_grad=True)
# print(x)
# Y = x**2
# y = torch.sum(Y)
# print(Y)
# print(y)
# y.backward()
# print('x.grad: {}' .format(x.grad))
# function_line, = plt.plot(x.detach().numpy(), Y.detach().numpy(), label = 'Function')
# function_line.set_color("red")
# derivative_line, = plt.plot(x.detach().numpy(), x.grad.detach().numpy(), label = 'Derivative')
# derivative_line.set_color("green")
# plt.xlabel('x')
# plt.legend()
# plt.show()


# x = torch.tensor([1.,2.], requires_grad=True)
# print(x)
# Y = x**2
# y = torch.sum(Y)
# print(Y,y)
# y.backward()
# print('x.grad:{}'.format(x.grad))


x = torch.randn(3, requires_grad=True)
y = x * 2
while y.data.norm() < 1000:
    y = y * 2
print(y)
v = torch.tensor([0.1, 1.0, 0.0001], dtype=torch.float)
y.backward(v)
print(x.grad)