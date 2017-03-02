# 使用SVM算法对短文本分类

主要针对投诉类短文本分类。

## Install

```
pip install -r requirements.txt
```

## 使用步骤

提取的特征在文件`confing.py`中

```sh
# 准备原始文本数据
# csv格式，每行两个字段：title和content
# 可以有其他的字段
./source_data.csv

# 创建语料库等数据目录
mkdir data

# 根据特征生成语料库
# 特征配置在文件config.py中
python ./format_samples_data.py

# 训练
python ./train.py

# 在训练集上预测
python ./train_predict.py

# 在测试集上预测
python ./test.py

# 应用
python ./predict.py
```


