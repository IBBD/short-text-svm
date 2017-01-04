# -*- coding: utf-8 -*-
#
# 预处理数据：使用人工提取的特征，对文本进行归类，即是语料库
# Author: Alex
# Created Time: 2016年12月28日 星期三 16时16分38秒

import csv
import re
import sys
import os
from config import re_patterns

# 原数据文件
source_file = "./source_data.csv"

# 提取完特征之后的文件
train_file = "./data/train.csv"
more_file = "./data/more.csv"
none_file = "./data/none.csv"

# 删掉旧的数据文件
if os.path.exists(train_file):
    os.unlink(train_file)
if os.path.exists(more_file):
    os.unlink(more_file)
if os.path.exists(none_file):
    os.unlink(none_file)


def documents_from_file(filename, delimiter=","):
    """
    Return a generator for pulling rows from a given delimited file.

    :param filename: the name of the file to read from or '-' if stdin
    :param delimiter: the delimiter to use
    :param quiet: don't output anything to the console when this is True
    :return: generator returning document-indexing operations
    """
    with open(filename, 'rb') if filename != '-' else sys.stdin as doc_file:
        # delimited file should include the field names as the first row
        fieldnames = doc_file.next().strip().split(delimiter)

        reader = csv.DictReader(
            doc_file, delimiter=delimiter, fieldnames=fieldnames)

        for row in reader:
            yield row


def write(key, title, content):
    title = title.replace("\t", " ")
    content = content.replace("\t", " ")
    if key in re_patterns:
        # 训练样本
        title = title.replace("||", " ")
        content = content.replace("||", " ")
        with open(train_file, 'ab') as f:
            f.write("%s\t%s || %s\n" % (key, title, content))
    else:
        with open("./data/" + key + ".csv", 'ab') as f:
            w = csv.DictWriter(
                f, delimiter="\t", fieldnames=["title", "content"])
            w.writerow({"title": title, "content": content})


def findKeys(content):
    keys = []
    for key in re_patterns:
        pattern = re_patterns[key]
        groups = re.findall(pattern, content.decode("utf8"))
        if groups and len(groups) > 0:
            keys.append(key)

    return keys


def parse(content):
    keys = findKeys(content)
    num = len(keys)
    if num > 1:
        key = "more"
    elif num == 1:
        key = keys[0]
    else:
        key = "none"
    return key


if __name__ == "__main__":
    count = 0
    countNone = 0
    countMore = 0
    countAll = 0
    countDict = {}
    for row in documents_from_file(source_file):
        print(row["title"])
        countAll += 1
        num = 0

        # 处理title
        key = parse(row["title"])
        if key == "none":
            key = parse(row['content'])

        if key == "more":
            countMore += 1
        elif key == "none":
            countNone += 1
        else:
            count += 1
            if key not in countDict:
                countDict[key] = 1
            else:
                countDict[key] += 1

        write(key, row['title'], row["content"])

    print("\ncount: %d, more: %d, none: %d, all: %d" %
          (count, countMore, countNone, countAll))
    print(countDict)
