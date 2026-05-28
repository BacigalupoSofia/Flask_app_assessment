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
        new_product = {
            "id": len(products) + 1,
            "category": request.form['category'],
            "name": request.form['name'],
            "brand": request.form['brand'],
            "Supplier": request.form['Supplier'],
            "quantity": int(request.form['quantity']),
            "minimum": int(request.form['minimum']),
            "expiration": request.form['expiration']
        }
        products.append(new_product)
        return redirect(url_for('Stock'))
    return render_template('add.html')

@app.route('/delete/<int:product_id>')
def Delete(product_id):
    return render_template('delete.html', products=products)


@app.route('/info/<int:product_id>')
def Info(product_id):
    product = products[product_id-1]
    return render_template('info.html', product=product)




if __name__ == "__main__":
    app.run(debug=True)