#!/usr/bin/env python
# -*- coding: utf-8 -*-
# by vellhe 2017/7/9
import pandas as pd #数据分析
import numpy as np #科学计算
import sklearn.preprocessing as preprocessing
from flask import Flask

# Flask初始化参数尽量使用你的包名，这个初始化方式是官方推荐的，官方解释：http://flask.pocoo.org/docs/0.12/api/#flask.Flask
app = Flask(__name__)


@app.route('/Normalize')
#path为csv文件路径，target是归一化的目标列名
def normalize(path,target):
    data_train = pd.read_csv("path")
    target_df=data_train[target] #取出目标列数据
    mm = preprocessing.MinMaxScaler() #归一化
    mm_data = mm.fit_transform(target_df) #处理数据
    data_train.drop([target],axis=1,inplace=True)
    data_train[target]=mm_data
    return data_train





if __name__ == "__main__":
    # 这种是不太推荐的启动方式，我这只是做演示用，官方启动方式参见：http://flask.pocoo.org/docs/0.12/quickstart/#a-minimal-application
    app.run(debug=True)