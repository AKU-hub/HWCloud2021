#!/bin/bash

set -e
set -x

python our.py \
    --data our_voc.yaml \
    --cfg yolov5s.yaml --resume \
    --weights /opt/zhaoruyi02/project/zry/yolov5/runs/train/exp/weights/last.pt --epochs 500 \
    --batch-size 96