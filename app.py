from flask import Flask, render_template, request
from finace import op

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/eyeglass')
def eyeglass():
    nac = op.get_all_name_and_code()
    return render_template('eyeglass.html', nac=nac)


@app.route('/diamond')
def diamond():
    return render_template('diamond.html')


@app.route('/result')
def result():
    name = request.args.get('name')
    t1 = request.args.get('begin-date')
    t2 = request.args.get('end-date')
    df1 = op.get_asset(name, t1, t2)
    df2 = op.get_gain(name, t1, t2)
    x = df1['流动资产合计'].mean() / df1['流动负债总计'].mean()
    y = df1['负债总计'].mean() / df1['资产总计'].mean()
    z = df2['净利润'].mean() / df1['资产总计'].mean()
    return render_template('result.html', df1=df1, df2=df2,
                           name=name, t1=t1, t2=t2, x=x, y=y, z=z)


if __name__ == '__main__':
    app.run()
