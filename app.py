from flask import Flask, render_template, request, redirect, url_for, flash, session
from data_base import products, users


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
            "supplier": request.form.get('supplier'),
            "quantity": int(request.form.get('quantity')),
            "minimum_stock": int(request.form.get('minimum')),
            "expiry_date": request.form.get('expiry_date'),
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


@app.route('/edit/<int:product_id>', methods=['GET', 'POST'])
def Edit(product_id):
    product = next((p for p in products if p['id'] == product_id), None)

    if product is None:
        flash("Product not found.", "danger")
        return redirect(url_for('Stock'))

    if request.method == 'POST':
        product['category'] = request.form.get('category')
        product['name'] = request.form.get('name')
        product['brand'] = request.form.get('brand')
        product['supplier'] = request.form.get('supplier')
        product['description'] = request.form.get('description')
        product['quantity'] = int(request.form.get('quantity'))
        product['minimum_stock'] = int(request.form.get('minimum_stock'))
        product['expiry_date'] = request.form.get('expiry_date')

        flash(f"{product['name']} updated successfully.", "success")
        return redirect(url_for('Stock'))

    return render_template('edit.html', product=product)
   

@app.route('/login', methods=['GET', 'POST'])
def Login():
    if request.method == 'POST':
        for user in users:
            if (request.form.get('name') == user['name'] and
                request.form.get('password') == user['password']):

                session['user_log'] = user
                return redirect(url_for('Home'))

        flash('Invalid username or password', 'error')
        return redirect(url_for('Login'))
        
    return render_template('log_in.html') 

@app.route('/account')
def Account ():

    return render_template ('my_account.html')

if __name__ == "__main__":
    app.run(debug=True)