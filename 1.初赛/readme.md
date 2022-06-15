# 2021 第三届华为云人工智能大赛 · 无人车挑战杯 方案分享
## 初赛赛题
[初赛](https://competition.huaweicloud.com/information/1000041539/circumstance) 训练数据集包含红灯、绿灯、黄灯、人行横道、限速标志、解除限速标志六种类型图片，需使用ModelArts数据管理模块完成以上六种检测目标的标注,然后自定义算法建立目标检测模型。参赛者可使用**任意深度学习框架**框架建立目标检测模型

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
+ 后处理: WBF, 使用[WBF](https://github.com/ZFTurbo/Weighted-Boxes-Fusion)进行模型集成，WBF应该是目前性能最好后处理方法，优于NMS, Soft-NMS

**感谢以上作者的开源工作！！！**

## 环境配置
### 环境依赖
+ python 3.7
+ cuda 10.1
+ pytorch 1.7.0
+ detectron2 0.4
### 训练设备
4张2080ti

## 实验结果
