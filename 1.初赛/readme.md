# 2021 第三届华为云人工智能大赛 · 无人车挑战杯 方案分享
## 初赛赛题介绍
本届[无人车挑战杯](https://competition.huaweicloud.com/information/1000041539/introduction)大赛主要考核点有交通信号灯识别、车道线检测、斑马线检测、限速标志识别、施工标志识别、障碍物检测等，其中交通信号灯、斑马线、限速标志检测算法需要基于AI开发平台ModelArts开发。

初赛训练数据集包含红灯、绿灯、黄灯、人行横道、限速标志、解除限速标志六种类型图片，需使用ModelArts数据管理模块完成以上六种检测目标的标注。参赛者可使用**任意深度学习框架**框架建立目标检测模型

## 基本思路
+ 因初赛不限定深度学习框架, 基本原则就是啥方法好用哪个 (速度别太慢就行)
+ 但是需要考虑一下本地训练模型迁移到华为云平台的工作量及难度 (这个真的一言难尽)
+ 综合考虑, 选用[CenterNet2](https://github.com/xingyizhou/CenterNet2) 和[YOLOv5](https://github.com/ultralytics/yolov5) (比赛嘛，少不了集成啊)

## 解决方案
+ 数据集: [初赛数据](https://marketplace.huaweicloud.com/markets/aihub/datasets/detail/?content_id=93d35831-c084-4003-b175-4280ef289379)
    + 官方提供的数据没有标注
    + 标注方法: [自动标注](https://console.huaweicloud.com/modelarts/?region=cn-north-4#/dataLabel) +人工矫正
    + 标注原则是尽可能贴紧目标，但本地测试结果与官方差距过大，把训练集框外扩一点，有效涨点
+ 数据增强
    + [Albumentations](https://github.com/albumentations-team/albumentations): 因交通灯对颜色敏感, 去掉色彩类增强
    + [Imagecorruptions](https://github.com/bethgelab/imagecorruptions): 增加鲁棒性
    + [Mosiac](https://github.com/Tianxiaomo/pytorch-YOLOv4): 离线生成, 扩充数据集, 变相增加BS
    + [Mixup](https://github.com/facebookresearch/mixup-cifar10): 有掉点, 时间有限, 没认真调, 感兴趣的可以调一调
+ 训练策略: 考虑到无人车场景下, 目标尺度变化较大, 采用**多尺度训练**, 每轮迭代随机从预定义尺度范围内选择一个
+ 检测模型: [CenterNet2](https://github.com/xingyizhou/CenterNet2), 实际测试时，我们发现**人行横道**的检测精度与其它五类差距过大, 因为我们额外训练了一个[YOLOv5](https://github.com/ultralytics/yolov5) 模型对其进行单独检测, 并将结果进行融合, 模型融合, 亲测有效!
+ 后处理: TTA+WBF, 使用[WBF](https://github.com/ZFTurbo/Weighted-Boxes-Fusion)进行模型集成，WBF应该是目前性能最好后处理方法，优于NMS, Soft-NMS

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

### 预训练模型下载
[coco预训练模型](https://mindspore.cn/resources/hub/details?MindSpore/ascend/1.1/yolov4_v1.1)下载完后放在weights文件夹下面

### 模型训练
```
sh train.sh
```
生成的模型在weights文件夹下

## 模型推理
测试图片放在samples文件夹下，推理结果在outputs文件夹下，该脚本可以本地运行，也可以直接用于部署Modelarts在线服务和批量服务
```
python customize_service.py
```
