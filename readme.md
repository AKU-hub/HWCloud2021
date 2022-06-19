# 2021 第三届华为云人工智能大赛 · 无人车挑战杯 方案分享
## 赛题介绍
本赛事是由沈抚改革创新示范区与华为（辽宁）人工智能创新中心、上海交通大学三方合作，共同主办的面向全国的人工智能交流赛事。大赛基于华为云人工智能平台（一站式AI开发平台ModelArts、端云协同多模态AI开发应用平台HiLens）及无人驾驶小车，全面锻炼和提高赛队的AI解决方案能力及无人驾驶编程技巧。

本届[无人车挑战杯](https://competition.huaweicloud.com/information/1000041539/introduction) 大赛主要考核点有交通信号灯识别、车道线检测、斑马线检测、限速标志识别、施工标志识别、障碍物检测等，其中交通信号灯、斑马线、限速标志检测算法需要基于AI开发平台ModelArts开发， 训练数据集包含红灯、绿灯、黄灯、人行横道、限速标志、解除限速标志六种类型图片

Contact: [ru_yi_zhao@163.com](mailto:ru_yi_zhao@163.com). Any questions or discussions are welcomed! 

## 解决方案及算法介绍
+ 数据集: [初赛数据](https://marketplace.huaweicloud.com/markets/aihub/datasets/detail/?content_id=93d35831-c084-4003-b175-4280ef289379) 和 [复赛数据](https://marketplace.huaweicloud.com/markets/aihub/notebook/detail/?id=0fbf9486-9e71-41f0-9295-3d75b68b15db)
+ 数据增强：[albu](https://github.com/albumentations-team/albumentations)和[imagecorruptions](https://github.com/bethgelab/imagecorruptions)
+ 后处理： tta+wbf, 使用[wbf](https://github.com/ZFTurbo/Weighted-Boxes-Fusion)进行多尺度集成，wbf应该是目前性能最好后处理方法，优于nms, soft-nms, nmw
+ 检测模型：[YoloV4](https://gitee.com/ascend/modelzoo/tree/master/built-in/MindSpore/Official/cv/detection/YOLOv4_Cspdarknet53_for_MindSpore), 在本次比赛中我们集成了两个yolov4模型，模型一使用albu增广，模型二使用albu+imagecorruptions增广，可以提升方案的鲁棒性。和只使用模型一相比，堆叠模型二后可以带来2个点左右的涨点

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
