# -*- coding: utf-8 -*-

# 分类模型
# Author: Alex
# Created Time: 2016年12月30日 星期五 14时18分58秒

from tgrocery import Grocery

gr = Grocery("test")
gr.load()

lessVal = 0.2

# 统计变量
statDict = {
    "total": 0,    # 总数
    "notEq": 0,    # title和content的识别结果不一致
    "less": 0,     # 小于某个阀值的数量
    "title": 0,    # 以title为结果的次数
    "content": 0   # 以content为结果的次数
}


def getStatDict():
    return statDict


def classify(title, content):
    """
    分类器
    :return cat 预测的分类
    :return status 分类状态，title or content
    :return titleCat 根据title的预测结果
    :return contentCat 根据content的预测结果
    """
    titleCat = gr.predict(title)
    contentCat = gr.predict(content)
    tCat = titleCat.predicted_y
    cCat = contentCat.predicted_y
    tVal = titleCat.dec_values[tCat]
    status = "title"
    statDict['total'] += 1
    if tCat == cCat:
        if tVal < lessVal:
            statDict["less"] += 1
        return tCat, status, titleCat, contentCat

    statDict['notEq'] += 1
    cVal = contentCat.dec_values[cCat]
    pCat = tCat
    if cVal > 1.4*tVal:
        pCat = cCat
        status = "content"
        statDict["content"] += 1
        if cVal < lessVal:
            statDict["less"] += 1
    else:
        statDict["title"] += 1
        if tVal < lessVal:
            statDict["less"] += 1

    return pCat, status, titleCat, contentCat
