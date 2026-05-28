from flask import Flask, render_template, request, redirect, url_for
from data_base import products


app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('home.html')

@app.route('/stock')
def Stock():
    return render_template('stock.html', products=products)

@app.route('/add', methods=['GET', 'POST'])
def Add():
    if request.method == 'POST':
        pass
    return render_template('add.html')

if __name__ == "__main__":
    app.run(debug=True)