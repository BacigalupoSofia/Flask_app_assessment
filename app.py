from flask import Flask, render_template, request, redirect, url_for, flash
from data_base import products, images


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
            "name": request.form.get('name').strip(),
            "brand": request.form.get('brand'),
            "Supplier": request.form.get('Supplier'),
            "quantity": int(request.form.get('quantity')),
            "minimum": int(request.form.get('minimum')),
            "expiration": request.form.get('expiration')
        }

        errors = []
        if not new_product["category"]:
            errors.append("Category is required.")
        if not new_product["name"]:
            errors.append("Name is required.")
        if not new_product["brand"]:
            errors.append("Brand is required.")
        if not new_product["Supplier"]:
            errors.append("Supplier is required.")
        if not new_product["expiration"]:
            errors.append("Expiration date is required.")

        if errors:
            return render_template('add.html', errors=errors)

        products.append(new_product)
        return redirect(url_for('Stock'))
    
    return render_template('add.html')

@app.route('/delete/<int:product_id>', methods=['GET', 'POST'])
def Delete(product_id):
    deleting = next((p for p in products if p['id'] == product_id), None)
    product_image = images.get(product_id)

    if deleting is None:
        flash("Product not found.", "error")
        return redirect(url_for('Stock'))

    if request.method == 'POST':
        if deleting in products:
            products.remove(deleting)
            for index, product in enumerate(products, start=1):
                product['id'] = index
            flash(f"{deleting['name']} was deleted successfully.", "success")
            return redirect(url_for('Stock'))

    return render_template('delete.html', 
                           deleting=deleting, 
                           product_image=product_image)


@app.route('/info/<int:product_id>')
def Info(product_id):
    product = products[product_id-1]
    product_image = images.get(product_id)
    return render_template('info.html', product=product, product_image=product_image )




if __name__ == "__main__":
    app.run(debug=True)