
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# by vellhe 2017/7/9
import pandas as pd #数据分析
import numpy as np #科学计算
import sklearn.preprocessing as preprocessing
from flask import Flask

# Flask初始化参数尽量使用你的包名，这个初始化方式是官方推荐的，官方解释：http://flask.pocoo.org/docs/0.12/api/#flask.Flask
app = Flask(__name__)


@app.route('/setId')
def setId(path):
    data_train = pd.read_csv("path")
    count = len(data_train)
    list = []
    for num in range(0, count):
        list.append(num)
    data_train.insert(0, 'id', list)
    return data_train





if __name__ == "__main__":
    # 这种是不太推荐的启动方式，我这只是做演示用，官方启动方式参见：http://flask.pocoo.org/docs/0.12/quickstart/#a-minimal-application
    app.run(debug=True)