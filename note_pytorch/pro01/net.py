import torch

class Net(torch.nn.Module):
  def __init__(self, n_feature, n_hidden, n_output):
    super(Net, self).__init__()
    self.n_hidden = torch.nn.Linear(n_feature, n_hidden)
    self.out = torch.nn.Linear(n_feature, n_output)

  def forward(self, x_layer):
    x_layer = torch.relu(self.n_hidden(x_layer))
    x_layer = self.out(x_layer)
    x_layer = torch.nn.functional.softmax(x_layer)
    return x_layer

net = Net(n_feature=2, n_hidden=10, n_output=2)
