from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "your_secret_key"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/products')
def products_page():
    products = [
        {'id': 1, 'name': 'Denim Jacket', 'price': 120, 'image': 'denim-jacket.jpg', 'description': 'Classic denim jacket with customizable fading and patterns.'},
            {'id': 2, 'name': 'Denim Jeans', 'price': 32, 'image': 'denim-jeans.jpg', 'description': 'Comfortable jeans with personalized laser engraving option.'},
    {'id': 5, 'name': 'Denim Shirt', 'price': 25, 'image': 'denim-shirt.jpg', 'description': 'Button-down shirt, perfect for layering or standalone.'},
    {'id': 6, 'name': 'Denim Overalls', 'price': 70, 'image': 'denim-overalls.jpg', 'description': 'Comfortable overalls with adjustable straps.'},
    {'id': 7, 'name': 'Denim Shoes', 'price': 30, 'image': 'denim-shoes.jpg', 'description': 'Trendy denim shoes for a casual yet stylish look.'},
    {'id': 8, 'name': 'Denim Dress', 'price': 99, 'image': 'denim-dress.jpg', 'description': 'Chic denim dress with customizable embroidery.'},
    {'id': 9, 'name': 'Denim Cap', 'price': 15, 'image': 'denim-cap.jpg', 'description': 'Stylish cap with adjustable strap.'},
    {'id': 10, 'name': 'Denim Bag', 'price': 75, 'image': 'denim-bag.jpg', 'description': 'Durable denim bag with spacious compartments.'},
    {'id': 11, 'name': 'Denim Belt', 'price': 20, 'image': 'denim-belt.jpg', 'description': 'Adjustable denim belt with stylish buckle.'}
       ]
    return render_template('products.html', products=products)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        product = request.form['product']
        message = request.form['message']
        # For now, we just flash a message, later we can save to database or send email
        flash(f"Thank you {name}! Your order for {product} has been submitted.")
        return redirect(url_for('contact'))
    return render_template('contact.html')


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/choose-color")
def choose_color():
    return render_template("choose_color.html")

@app.route('/cart')
def cart_page():
    return render_template('cart_page.html')

@app.route('/checkout')
def checkout_page():
    return render_template('checkout_page.html')

if __name__ == "__main__":
    app.run(debug=True)
