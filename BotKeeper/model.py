import torch
import torch.nn as nn

class NeuraNet(nn.Module):
    def __init__(self,input_size,hidden_size,num_classes):
        super(NeuraNet,self).__init__()
        self.l1=nn.Linear(input_size,hidden_size)
        self.l2=nn.Linear(input_size,hidden_size)
        self.l3=nn.Linear(input_size,num_classes)
        self.relu=nn.ReLU
    
    def forward(self,x):
        out=self.l1(x)
        out=self.relu(out)
        out=self.l2(x)
        out=self.relu(out)
        out=self.l3(x)

        return out