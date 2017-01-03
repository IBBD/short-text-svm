# -*- coding: utf-8 -*-
#
# 测试样本预测分类
# Author: Alex
# Created Time: 2016年12月29日 星期四 11时25分45秒

import os
from classify import classify, getStatDict


# 测试样本
filename = "./data/more.csv"
res_filename = "./data/test_results.txt"
if os.path.exists(res_filename):
    os.unlink(res_filename)

resFile = open(res_filename, "ab")
with open(filename) as f:
    for line in f.readlines():
        line = line.strip()
        row = line.split("\t")
        if len(row) != 2:
            continue

        cat, status, titleCat, contentCat = classify(row[0], row[1])
        resFile.write("%s\n===> %s\n\n" % (line, cat))
        tCat = titleCat.predicted_y
        cCat = contentCat.predicted_y
        tVal = titleCat.dec_values[tCat]
        cVal = contentCat.dec_values[cCat]
        if tCat != cCat:
            print("\n%s\n===> %s: %s" % (line, cat, status))
            print("===> %s: %f, %s: %f" % (tCat, tVal, cCat, cVal))

resFile.flush()
resFile.close()
stat = getStatDict()
print("\nstat:")
print(stat)
