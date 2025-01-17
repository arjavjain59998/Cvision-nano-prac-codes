## TODO: define the convolutional neural network architecture

import torch
import torch.nn as nn
import torch.nn.functional as F
# can use the below import should you choose to initialize the weights of your Net
import torch.nn.init as I


class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, 5, padding=2) #32x224x224  32x56x56
                                                    
        ## Note that among the layers to add, consider including:
        # maxpooling layers, multiple conv layers, fully-connected layers, and other layers (such as dropout or batch normalization) to avoid overfitting
        # ---------------------------------------------------------------
        
        self.conv2 = nn.Conv2d(32, 64, 3)   #64x54x54  #64x27x27
        self.conv3 = nn.Conv2d(64, 128, 1)  #128x27x27  #128x13x13
        self.pool1 = nn.MaxPool2d(4, 4)
        self.pool2 = nn.MaxPool2d(2, 2)
        self.lin1 = nn.Linear(128*13*13,1000)
        self.lin2 = nn.Linear(1000,68*2)
        self.drop1 = nn.Dropout(0.1)
        self.drop2 = nn.Dropout(0.2)
        self.drop3 = nn.Dropout(0.3)
        self.drop4 = nn.Dropout(0.4)
        # --------------------------------------------------------------
        
    def forward(self, x):
        ## TODO: Define the feedforward behavior of this model
        ## x is the input image and, as an example, here you may choose to include a pool/conv step:
        ## x = self.pool(F.relu(self.conv1(x)))
        # ---------------------------------------------------------------
        
   
        x = self.drop1(self.pool1(F.relu(self.conv1(x))))
        x = self.drop2(self.pool2(F.relu(self.conv2(x))))
        x = self.drop3(self.pool2(F.relu(self.conv3(x))))
        
        x = x.view(x.size(0), -1) # flatten
        
        x = self.drop4(F.relu(self.lin1(x)))
        x = self.lin2(x)
        # ---------------------------------------------------------------
        # a modified x, having gone through all the layers of your model, should be returned
        return x
