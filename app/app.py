#Flaskとrender_template（HTMLを表示させるための関数）をインポート
from flask import Flask,render_template,request
import numpy as np
import pandas as pd

app = Flask(__name__)

#「/」へアクセスがあった場合に，'Hellow World'の文字列を返す
@app.route('/')
def hello():
    return 'Hello World'

#「/index」へアクセスがあった場合に，「index.html」を返す
@app.route('/index')
def index():
    name = request.args.get('name')
    graph_class = ['chordal', 'tree', 'arbitraly']

    url = 'https://dl.dropboxusercontent.com/s/6mztoeb6xf78g5w/COVID-19.csv'
    df = pd.read_csv(url)

    return render_template('index.html', name = name, graph_class = graph_class, syokugyo = df['職業_正誤確認用'].unique())

if __name__ == 'main':
    app.run(debug=True)