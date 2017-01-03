# -*- coding: utf-8 -*-
#
# 训练样本的预测分类
# Author: Alex
# Created Time: 2016年12月29日 星期四 11时25分45秒

import os
from config import findSecondVal, statOutput
from classify import classify


# 对训练样本进行识别
# 统计最高得分的分布
# 统计最高得分和第二得分的比值的分布
filename = "./data/train.csv"
results_file = "./data/train_results.txt"
less = 1.005     # 阀值
maxList = []   # 保存最高得分
rateList = []  # 保存最高得分与次高得分的比值
lessRateList = []  # 小于阀值的比值
lessMaxList = []  # 小于阀值的值

if os.path.exists(results_file):
    os.unlink(results_file)

resFile = open(results_file, "ab")
with open(filename, "rb") as f:
    countSucc = 0
    countErr = 0
    countErrPredict = 0
    countSpitErr = 0
    countErrTC = 0
    total = 0
    for line in f.readlines():
        line = line.strip()
        row = line.split("\t")
        if len(row) != 2:
            continue

        # 分别判断标题和内容，看结果是否一致
        splitRow = row[1].split("||")
        if len(splitRow) != 2:
            continue

        title, content = splitRow[0], splitRow[1]

        # 作为整体进行判断
        cat, status, titleCat, contentCat = classify(title, content)
        newCat = titleCat
        if status == "content":
            newCat = contentCat

        if cat == row[0]:
            resFile.write("\n%s\nEQ: %s = %s\n" % (row[1], row[0], cat))
        else:
            resFile.write("\n%s\nERROR: %s = %s\n" % (row[1], row[0], cat))

        first = newCat.dec_values[cat]
        maxList.append(first)
        _, second = findSecondVal(newCat.dec_values, cat)
        isPrint = False
        rate = 0
        if second > 0:
            rate = first / second
            rateList.append(rate)

            if rate < 10.0:
                lessMaxList.append(first)
                isPrint = True

            # 小于阀值的
            if first < less:
                lessRateList.append(rate)
                isPrint = True

        if isPrint:
            print("%s\n====> %s: %f, %f\n" % (row[1], row[0], first, rate))

        total += 1
        if row[0] == cat:
            countSucc += 1
        else:
            countErr += 1
            print("%s\nERROR====>%s: %f > %s: %f\n" %
                  (row[1], row[0], newCat.dec_values[row[0]], cat, newCat.dec_values[cat]))

        # 分别判断标题和内容，看结果是否一致
        if titleCat.predicted_y != contentCat.predicted_y:
            countSpitErr += 1
            tCat = titleCat.predicted_y
            cCat = contentCat.predicted_y
            tVal = titleCat.dec_values[tCat]
            cVal = contentCat.dec_values[cCat]
            pCat = tCat
            if tVal > 1.5*cVal or cVal > 1.5*tVal:
                countErrTC += 1
                if cVal > tVal:
                    pCat = cCat

            if pCat != row[0]:
                countErrPredict += 1
                print("ERROR: %s\n" % (line))
            else:
                print("%s\n" % (line))

            print("====> title: %s: %f <==> content: %f" %
                  (tCat, tVal, titleCat.dec_values[cCat]))
            print("====> content: %s: %f <==> title: %f\n" %
                  (cCat, cVal, contentCat.dec_values[tCat]))


    print("\nSucc: %d, Err: %d, Rate: %f, spitErr: %d, tc: %d, perr: %d" %
          (countSucc, countErr, float(countSucc) / total, countSpitErr, countErrTC, countErrPredict))

resFile.flush()
resFile.close()

"""
maxList: count: 2619, max: 3.083332, min: 0.853927, mean: 1.048717, median: 0.977919
rateList: count: 695, max: 30095.730398, min: 4.133694, mean: 187.524008, median: 39.450127
lessMaxList: count: 32, max: 1.738444, min: 1.110746, mean: 1.228861, median: 1.163622
lessRateList: count: 45, max: 30095.730398, min: 21.857167, mean: 1772.666181, median: 434.546347
"""
statOutput("maxList", maxList)
statOutput("rateList", rateList)
statOutput("lessMaxList", lessMaxList)
statOutput("lessRateList", lessRateList)
