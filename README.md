# 使用SVM算法对短文本分类

## Install

```
pip install -r requirements.txt
```

## 步骤

提取的特征在文件`confing.py`中

```sh
# 根据特征生成语料库
python ./format_samples_data.py

# 训练
python ./train.py

# 在训练集上预测
python ./train_predict.py

# 测试
python ./test_predict.py

# 应用
python ./predict.py
```


