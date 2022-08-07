# 2021 第三届华为云人工智能大赛 · 无人车挑战杯 方案分享
## 复赛赛题
初赛Top40进入[复赛](https://competition.huaweicloud.com/information/1000041539/fusai), **参赛者需基于MindSpore框架（使用其他框架提交的作品无效）建立目标检测模型**，模型输出格式、数据标注及说明、评分标准和[初赛](https://competition.huaweicloud.com/information/1000041539/circumstance) 一致。
## 基本思路
+ 复赛只有一周时间, 每天只能提交一次, 必须使用MindSpore, 从战略角度，基本可以放弃迁移框架算法的想法, 否则到后面即便迁移成功, 也没有提交的机会了(一言难尽)
+ 基本思路就是找现成MindSpore算法, 官方提供了一个YOLOv3的[Baseline](https://developer.huaweicloud.com/develop/aigallery/article/detail?id=81b7eaf2-e767-4937-822f-e3e887c73380) (但据我所知凡是用这个Baseline的, mAP没有超过0.01的)

## 解决方案
+ 数据集: [复赛数据](https://marketplace.huaweicloud.com/markets/aihub/notebook/detail/?id=0fbf9486-9e71-41f0-9295-3d75b68b15db)
+ 数据增强 (同初赛)
    + [Albumentations](https://github.com/albumentations-team/albumentations): 因交通灯对颜色敏感, 去掉色彩类增强
    + [Imagecorruptions](https://github.com/bethgelab/imagecorruptions): 增加鲁棒性
    + [Mosiac](https://github.com/Tianxiaomo/pytorch-YOLOv4): 离线生成, 扩充数据集, 变相增加BS
    + [Mixup](https://github.com/facebookresearch/mixup-cifar10): 有掉点, 时间有限, 没认真调, 感兴趣的可以调一调
+ 训练策略: 同初赛, 采用**多尺度训练**
+ 后处理： TTA+WBF, 使用[WBF](https://github.com/ZFTurbo/Weighted-Boxes-Fusion)进行检测结果集成
+ 检测模型
    + [YoloV4](https://gitee.com/ascend/modelzoo/tree/master/built-in/MindSpore/Official/cv/detection/YOLOv4_Cspdarknet53_for_MindSpore), 幸运的是我们在开源社区找到了MindSpore版的YOLOv4, 但无奈没有预训练模型, 经常NaN, 所以挺考验炼丹基本功的
    + 同样的，在本次比赛中我们集成了两个YOLOv4模型，模型一检测六个类别，模型二单独检测人行横道, 最后将检测结果融合。和只使用模型一相比，堆叠模型二后可以带来2个点左右的涨点

**感谢以上作者的开源工作！！！**

## 环境配置
(官方劝我们放弃本地搭建环境)
+ [ModelArts](https://console.huaweicloud.com/modelarts/?region=cn-north-4#/dev-container) 平台
+ mindspore 1.3.0


## 实验结果

