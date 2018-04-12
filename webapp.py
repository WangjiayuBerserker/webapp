from flask import Flask
from flask import render_template
from flask import request
import qcode

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

#   装饰器     给函数增加功能
@app.route('/url',methods=['GET','POST'])
def url():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        # 接受用户传递的url地址
        urls = request.form.get('url')
        print('2222')
        imgurl = qcode.url(url)
        return render_template('img.html',imgurl = imgurl)



if __name__ == '__main__':
    app.run()