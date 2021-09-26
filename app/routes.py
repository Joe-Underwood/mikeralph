from app import app, db
from app.models import User, Product, Product_Subtype, Product_Image
from app.forms import LoginForm
from flask import render_template, request, jsonify, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('main.html')

@app.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    return render_template('admin.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin'))
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user is None or not user.check_password(form.password.data) or not user.verify_totp(form.token.data):
            #flask('Invalid username or password')
            return redirect(url_for('login'))
        
        login_user(user)
        return redirect(url_for('admin'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/get_public_product_list', methods=['POST'])
def get_public_product_list():
    query = db.session.query(Product).order_by(Product.priority.asc())
    public_product_list = []

    for product in query:
        product_subtype_list = []
        product_image_list = []
        
        for item in product.product_subtype_list:
            product_subtype_list.append({
                'width': item.width,
                'length': item.length,
                'height': item.height,
                'price': item.price
            }) 

        for image in product.product_images:
            product_image_list.append({
                'imgFilename': image.img_filename,
                'priority': image.priority
            })

        public_product_list.append({
            'productName': product.product_name,
            'priority': product.priority,
            'imgFilename': product.img_filename,
            'description': product.description,
            'productSubtypeList': product_subtype_list,
            'productImages': product_image_list, 
        })
    
    return { 'publicProductList': public_product_list }

@login_required
@app.route('/get_private_product_list', methods=['POST'])
def get_private_product_list():
    return None

@login_required
@app.route('/set_product_list', methods=['POST'])
def set_product_list():
    return None
