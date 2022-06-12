import torch
import yaml
from models.yolo import Model

with open('./data/hyps/hyp.scratch-low.yaml', errors='ignore') as f:
    hyp = yaml.safe_load(f)  # load hyps dict

model = Model('./models/our_yolov5s.yaml', ch=3, nc=1, anchors=hyp.get('anchors'))
x = torch.rand(32, 3, 224, 224)
y = model(x)

print(len(y), y[0].shape, y[1].shape, y[2].shape)
