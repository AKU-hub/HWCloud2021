import csv
import matplotlib.pyplot as plt

x = list(range(0, 300, 5))
y = list(range(0, 300, 5))

random_ap50 = []
random_ap = []
coco2017_supervised_ap50 = []
coco2017_supervised_ap = []

voc2012e400_400_ap50 = []
voc2012e400_400_ap = []
voc2012e400_5_ap50 = []
voc2012e400_5_ap = []

coco2017lr1e400_5r192_ap50 = []
coco2017lr1e400_5r192_ap = []
coco2017lr1e400_100r192_ap50 = []
coco2017lr1e400_100r192_ap = []
coco2017lr1e400_200r192_ap50 = []
coco2017lr1e400_200r192_ap = []
coco2017lr1e400_300r192_ap50 = []
coco2017lr1e400_300r192_ap = []
coco2017lr1e400_400r192_ap50 = []
coco2017lr1e400_400r192_ap = []

with open('./coco2017lr1e400_5r192/results.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for i, row in enumerate(f_csv):
        if i % 5 == 0:
            coco2017lr1e400_5r192_ap50.append(float(row[6].strip()))
            coco2017lr1e400_5r192_ap.append(float(row[7].strip()))

with open('./coco2017lr1e400_100r192/results.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for i, row in enumerate(f_csv):
        if i % 5 == 0:
            coco2017lr1e400_100r192_ap50.append(float(row[6].strip()))
            coco2017lr1e400_100r192_ap.append(float(row[7].strip()))

with open('./coco2017lr1e400_200r192/results.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for i, row in enumerate(f_csv):
        if i % 5 == 0:
            coco2017lr1e400_200r192_ap50.append(float(row[6].strip()))
            coco2017lr1e400_200r192_ap.append(float(row[7].strip()))

with open('./coco2017lr1e400_400r192/results.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for i, row in enumerate(f_csv):
        if i % 5 == 0:
            coco2017lr1e400_400r192_ap50.append(float(row[6].strip()))
            coco2017lr1e400_400r192_ap.append(float(row[7].strip()))

with open('./voc2012lr1e400_5r192/results.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for i, row in enumerate(f_csv):
        if i % 5 == 0:
            voc2012e400_5_ap50.append(float(row[6].strip()))
            voc2012e400_5_ap.append(float(row[7].strip()))

with open('./VOC2007_pre2012lr1e400r192/results.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for i, row in enumerate(f_csv):
        if i % 5 == 0:
            voc2012e400_400_ap50.append(float(row[6].strip()))
            voc2012e400_400_ap.append(float(row[7].strip()))

with open('./coco2017lr1e400_300r192/results.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for i, row in enumerate(f_csv):
        if i % 5 == 0:
            coco2017lr1e400_300r192_ap50.append(float(row[6].strip()))
            coco2017lr1e400_300r192_ap.append(float(row[7].strip()))

with open('./VOC2007_random/results.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for i, row in enumerate(f_csv):
        if i % 5 == 0:
            random_ap50.append(float(row[6].strip()))
            random_ap.append(float(row[7].strip()))

with open('./VOC2007_coco/results.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for i, row in enumerate(f_csv):
        if i % 5 == 0:
            coco2017_supervised_ap50.append(float(row[6].strip()))
            coco2017_supervised_ap.append(float(row[7].strip()))

# plt.plot(x, random_ap50, label='random')
# plt.plot(x, coco2017_supervised_ap50, label='coco2017_supervised')
plt.plot(x, coco2017lr1e400_5r192_ap, label='coco2017_SoCo_e400_5')
plt.plot(x, coco2017lr1e400_100r192_ap, label='coco2017_SoCo_e400_100')
plt.plot(x, coco2017lr1e400_200r192_ap, label='coco2017_SoCo_e400_200')
plt.plot(x, coco2017lr1e400_300r192_ap, label='coco2017_SoCo_e400_300')
plt.plot(x, coco2017lr1e400_400r192_ap, label='coco2017_SoCo_e400_400')


plt.xlabel('Epoch')
plt.ylabel('mAP')
plt.grid(True)
plt.legend(loc="lower right")
plt.savefig('figure/coco_map.pdf')
plt.show()
