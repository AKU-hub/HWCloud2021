# 2021 第三届华为云人工智能大赛 · 无人车挑战杯 方案分享
## 决赛赛题
结合各队伍初赛打榜成绩（40%）、复赛打榜成绩（40%）、复赛答辩成绩（20%）综合评选出TOP20支队伍进入决赛

决赛就是要将算法落地到无人车上，全自动跑起来，**考核点:** 交通灯识别（出发&泊车）、速度控制、弯道行驶、斑马线识别、动态障碍物避障、自动泊车、竞速等

![rule](./figs/rule.png)

## 基本思路
+ 完整的无人车系统通常包含**感知、定位、导航、决策、控制**五个部位, 由于本人是CV方向，因此主要负责其中的视觉感知部分
+ 决赛中的视觉感知任务主要包括**交通灯**(出发&泊车)、**交通标志**(加速&减速)、**斑马线**(停车)、**车道线**(巡线行驶)
+ 
## 解决方案
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

