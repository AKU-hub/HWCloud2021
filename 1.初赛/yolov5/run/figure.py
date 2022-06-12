import matplotlib.pyplot as plt
from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval
import numpy as np

cocoGt_file = 'figure/val_07new.json'
cocoGt = COCO(cocoGt_file)  # 取得标注集中coco json对象
cocoDt_file = 'figure/results.json'
cocoDt = cocoGt.loadRes(cocoDt_file)

coco_eval = COCOeval(cocoGt, cocoDt, 'bbox')
coco_eval.evaluate()
coco_eval.accumulate()
coco_eval.summarize()

pr_array1 = coco_eval.eval['precision'][0, :, 0, 0, 2]
pr_array2 = coco_eval.eval['precision'][1, :, 0, 0, 2]
pr_array3 = coco_eval.eval['precision'][2, :, 0, 0, 2]
pr_array4 = coco_eval.eval['precision'][3, :, 0, 0, 2]
pr_array5 = coco_eval.eval['precision'][4, :, 0, 0, 2]
pr_array6 = coco_eval.eval['precision'][5, :, 0, 0, 2]
x = np.arange(0.0, 1.01, 0.01)
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.xlim(0, 1.0)
plt.ylim(0, 1.01)
plt.grid(True)

plt.plot(x, pr_array1, label='α=0.5')
plt.plot(x, pr_array2, label='α=0.55')
plt.plot(x, pr_array3, label='α=0.6')
plt.plot(x, pr_array4, label='α=0.65')
plt.plot(x, pr_array5, label='α=0.7')
plt.plot(x, pr_array6, label='α=0.75')
plt.legend(loc="lower left")
plt.savefig('figure/pr.pdf')
plt.show()
