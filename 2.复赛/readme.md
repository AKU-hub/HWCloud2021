# 2021 第三届华为云人工智能大赛 · 无人车挑战杯 方案分享
## 复赛赛题
初赛Top40进入[复赛](https://competition.huaweicloud.com/information/1000041539/fusai), **参赛者需基于MindSpore框架（使用其他框架提交的作品无效）建立目标检测模型**，模型输出格式、数据标注及说明、评分标准和[初赛](https://competition.huaweicloud.com/information/1000041539/circumstance) 一致。
## 基本思路

## 解决方案
+ 数据集: [初赛数据](https://marketplace.huaweicloud.com/markets/aihub/datasets/detail/?content_id=93d35831-c084-4003-b175-4280ef289379)和[复赛数据](https://marketplace.huaweicloud.com/markets/aihub/notebook/detail/?id=0fbf9486-9e71-41f0-9295-3d75b68b15db)
+ 数据增强：[albu](https://github.com/albumentations-team/albumentations)和[imagecorruptions](https://github.com/bethgelab/imagecorruptions)
+ 后处理： tta+wbf, 使用[wbf](https://github.com/ZFTurbo/Weighted-Boxes-Fusion)进行多尺度集成，wbf应该是目前性能最好后处理方法，优于nms, soft-nms, nmw
+ 检测模型：[YoloV4](https://gitee.com/ascend/modelzoo/tree/master/built-in/MindSpore/Official/cv/detection/YOLOv4_Cspdarknet53_for_MindSpore), 在本次比赛中我们集成了两个yolov4模型，模型一使用albu增广，模型二使用albu+imagecorruptions增广，可以提升方案的鲁棒性。和只使用模型一相比，堆叠模型二后可以带来2个点左右的涨点

**感谢以上作者的开源工作！！！**

## 环境配置
(官方劝我们放弃本地搭建环境)
+ [ModelArts](https://console.huaweicloud.com/modelarts/?region=cn-north-4#/dev-container) 平台
+ mindspore 1.3.0


## 模型训练复现流程
### 数据集准备
训练集标签放在`data/annotations_xml`下，训练集图片放在`data/train`下

### 将voc格式的标签转为coco格式
```
mkdir -p data/annotations
python pascal2coco.py
```

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
