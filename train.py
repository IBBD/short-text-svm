# -*- coding: utf-8 -*-
#
# 训练样本
# Author: Alex
# Created Time: 2016年12月29日 星期四 11时19分06秒

from tgrocery import Grocery

gr = Grocery('test')
train_file = "./data/train.csv"
gr.train(train_src=train_file)
gr.save()
