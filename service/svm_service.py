from flask import Flask
from flask import request
import numpy as np
from sklearn import svm
app = Flask(__name__)



@app.route('/svm',methods=['POST'])
def svm():
    # x1=request.form['x1']
    # y1=request.form['y1']
    # y2 = request.form['y2']
    # X = np.array(x1)
    # y = np.array(y1)
    # clt = svm.SVC()
    # s = clt.fit(X, y)
    # c = clt.predict(y2)

    c=request.form['c']
    return c


if __name__ == "__main__":
    # 这种是不太推荐的启动方式，我这只是做演示用，官方启动方式参见：http://flask.pocoo.org/docs/0.12/quickstart/#a-minimal-application
    app.run(debug=True)
