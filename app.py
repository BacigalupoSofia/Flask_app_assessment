from flask import Flask, render_template, request, redirect, url_for, flash
from data_base import products


app = Flask(__name__)
app.secret_key = "your_secret_key"

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
            "category": request.form.get('category'),
            "name": request.form.get('name').strip().title(),
            "brand": request.form.get('brand'),
            "supplier": request.form.get('Supplier'),
            "quantity": int(request.form.get('quantity')),
            "minimum_stock": int(request.form.get('minimum')),
            "expiry_date": request.form.get('expiration'),
            "image": request.form.get('image', "")
        }

        errors = []
        if not new_product["category"]:
            errors.append("Category is required.")
        if not new_product["name"]:
            errors.append("Name is required.")
        if not new_product["brand"]:
            errors.append("Brand is required.")
        if not new_product["supplier"]:
            errors.append("Supplier is required.")
        if not new_product["expiry_date"]:
            errors.append("Expiry date is required.")

        if errors:
            return render_template('add.html', errors=errors)

        products.append(new_product)
        flash(f"{new_product['name']} was added successfully.", "success")
        return redirect(url_for('Stock'))
    
    return render_template('add.html')

@app.route('/delete/<int:product_id>', methods=['GET', 'POST'])
def Delete(product_id):
    deleting = next((p for p in products if p['id'] == product_id), None)

    if deleting is None:
        flash(f"Product not found.", "danger")
        return redirect(url_for('Stock'))


    if request.method == 'POST':
        if deleting in products:
            products.remove(deleting)
            for index, product in enumerate(products, start=1):
                product['id'] = index
            flash(f"{deleting['name']} was deleted successfully.", "success")
            return redirect(url_for('Stock'))
       

    return render_template('delete.html', 
                           deleting=deleting)


@app.route('/info/<int:product_id>')
def Info(product_id):
    product = products[product_id-1]
    product_image = images.get(product_id)
    return render_template('info.html', product=product, product_image=product_image )




if __name__ == "__main__":
    app.run(debug=True)