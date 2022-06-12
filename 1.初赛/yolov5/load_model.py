import torch

# state_dict = torch.load('./model/ckpt_epoch_1.pth')
# print(state_dict.keys())
# print(state_dict['model'].keys())

state_dict = torch.load('./weights/best.pt')
print(state_dict.keys())


