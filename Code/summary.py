import torch
from torchsummary import summary
from utils.model.unet import Unet

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = Unet(1, 1).to(device)
summary(model, input_size=(384, 384), batch_size=8)