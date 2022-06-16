# 2021 第三届华为云人工智能大赛 · 无人车挑战杯 方案分享
## 决赛赛题
结合各队伍初赛打榜成绩（40%）、复赛打榜成绩（40%）、复赛答辩成绩（20%）综合评选出TOP20支队伍进入决赛

决赛就是要将算法落地到无人车上，全自动跑起来，**考核点:** 交通灯识别（出发&泊车）、速度控制、弯道行驶、斑马线识别、动态障碍物避障、自动泊车、竞速等

![rule](https://github.com/AKU-hub/I2DKPCN/blob/master/%20figs/framework.png)
## 解决方案及算法介绍
+ 数据集: [初赛数据](https://marketplace.huaweicloud.com/markets/aihub/datasets/detail/?content_id=93d35831-c084-4003-b175-4280ef289379)和[复赛数据](https://marketplace.huaweicloud.com/markets/aihub/notebook/detail/?id=0fbf9486-9e71-41f0-9295-3d75b68b15db)
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
