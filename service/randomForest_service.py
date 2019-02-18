#!/usr/bin/env python
# -*- coding: utf-8 -*-
# by vellhe 2017/7/9
import pandas as pd #数据分析
import numpy as np #科学计算
import sklearn.preprocessing as preprocessing
from sklearn.ensemble import RandomForestRegressor
from flask import Flask

# Flask初始化参数尽量使用你的包名，这个初始化方式是官方推荐的，官方解释：http://flask.pocoo.org/docs/0.12/api/#flask.Flask
app = Flask(__name__)

#使用随机森林方法拟合补全缺失数据，适合缺失数据较少时
@app.route('/randomForest')
#path为csv文件路径，target是补全的目标列名，ref是用来生成拟合值的相关项列表
def randomForest(path,target,ref):
    data_train = pd.read_csv("path")
    total_list=ref.insert(0,target)#将target列名插入在ref最前面生成新列表
    target_df=data_train[total_list]#将这些列的数据都取出来
    #将数据分成已知目标项值和未知目标项值两部分
    known_data= target_df[target_df[target].notnull()].as_matrix()
    unknown_data =  target_df[target_df[target].isnull()].as_matrix()
    # y即目标值
    y = known_data[:, 0]
    # X即特征属性值
    X = known_data[:, 1:]
    # fit到RandomForestRegressor之中
    rfr = RandomForestRegressor(random_state=0, n_estimators=2000, n_jobs=-1)
    rfr.fit(X, y)
    # 用得到的模型进行未知目标值结果预测
    predictedAges = rfr.predict(unknown_data[:, 1::])
    # 用得到的预测结果填补原缺失数据
    data_train.loc[(data_train[target].isnull()), target] = predictedAges
    return data_train





if __name__ == "__main__":
    # 这种是不太推荐的启动方式，我这只是做演示用，官方启动方式参见：http://flask.pocoo.org/docs/0.12/quickstart/#a-minimal-application
    app.run(debug=True)