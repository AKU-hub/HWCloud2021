# 2021 第三届华为云人工智能大赛 · 无人车挑战杯 方案分享
## 赛题介绍
本赛事是由沈抚改革创新示范区与华为（辽宁）人工智能创新中心、上海交通大学三方合作，共同主办的面向全国的人工智能交流赛事。大赛基于华为云人工智能平台（一站式AI开发平台ModelArts、端云协同多模态AI开发应用平台HiLens）及无人驾驶小车，全面锻炼和提高赛队的AI解决方案能力及无人驾驶编程技巧。

本届[无人车挑战杯](https://competition.huaweicloud.com/information/1000041539/introduction) 大赛主要考核点有交通信号灯识别、车道线检测、斑马线检测、限速标志识别、施工标志识别、障碍物检测等，其中交通信号灯、斑马线、限速标志检测算法需要基于AI开发平台ModelArts开发， 训练数据集包含红灯、绿灯、黄灯、人行横道、限速标志、解除限速标志六种类型图片

Contact: [ru_yi_zhao@163.com](mailto:ru_yi_zhao@163.com). Any questions or discussions are welcomed! 

## 初赛
+ **基本任务**: 线上打榜(形式), 目标检测(类型), 交通灯&交通标志(数据集)
+ **详细方案**: 见[初赛方案](./1.初赛/)

**感谢以上作者的开源工作！！！**

## 环境配置
### 环境依赖
+ cuda 10.1
+ cudnn 7.6.4
+ gcc 7.3.0
+ python 3.7
+ mindspore 1.3.0
### 训练设备
4张1080ti，batch_size(6x4)

## 模型训练复现流程
### 数据集准备
训练集标签放在`data/annotations_xml`下，训练集图片放在`data/train`下

### 将voc格式的标签转为coco格式
```
mkdir -p data/annotations
python pascal2coco.py
```
