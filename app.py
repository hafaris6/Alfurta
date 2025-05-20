import os
import uuid
import logging
from flask import Flask, render_template, request, redirect, url_for, session, flash

# Set up logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev_secret_key")

# In-memory data storage
products = []
merchants = []

# Add some sample merchants for testing
merchants.append({
    "id": "1",
    "name": "تاجر الإلكترونيات",
    "phone": "9123456789"  # Syria country code is 963
})

@app.route('/')
def index():
    """Render the homepage with all products"""
    return render_template('index.html', products=products)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handle merchant login"""
    if request.method == 'POST':
        phone = request.form.get('phone')
        name = request.form.get('name')
        
        # Check if merchant exists
        merchant = next((m for m in merchants if m['phone'] == phone), None)
        
        if merchant:
            # Set the merchant session
            session['merchant_id'] = merchant['id']
            session['merchant_name'] = merchant['name']
            session['merchant_phone'] = merchant['phone']
            flash('تم تسجيل الدخول بنجاح', 'success')
            return redirect(url_for('dashboard'))
        else:
            # Create new merchant
            merchant_id = str(uuid.uuid4())
            new_merchant = {
                "id": merchant_id,
                "name": name,
                "phone": phone
            }
            merchants.append(new_merchant)
            
            # Set the merchant session
            session['merchant_id'] = merchant_id
            session['merchant_name'] = name
            session['merchant_phone'] = phone
            flash('تم إنشاء حساب جديد بنجاح', 'success')
            return redirect(url_for('dashboard'))
    
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    """Render the merchant dashboard with their products"""
    if 'merchant_id' not in session:
        flash('يرجى تسجيل الدخول أولاً', 'warning')
        return redirect(url_for('login'))
    
    merchant_id = session['merchant_id']
    # Filter products that belong to this merchant
    merchant_products = [p for p in products if p['merchant_id'] == merchant_id]
    
    return render_template('dashboard.html', products=merchant_products)

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    """Add a new product"""
    if 'merchant_id' not in session:
        flash('يرجى تسجيل الدخول أولاً', 'warning')
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        image = request.form.get('image')
        price = request.form.get('price')
        
        # Create new product
        product_id = str(uuid.uuid4())
        new_product = {
            "id": product_id,
            "name": name,
            "description": description,
            "image": image,
            "price": price,
            "merchant_id": session['merchant_id'],
            "phone": session['merchant_phone']
        }
        products.append(new_product)
        
        flash('تمت إضافة المنتج بنجاح', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('add_product.html')

@app.route('/logout')
def logout():
    """Log out the merchant"""
    session.clear()
    flash('تم تسجيل الخروج بنجاح', 'success')
    return redirect(url_for('index'))

@app.route('/delete_product/<product_id>')
def delete_product(product_id):
    """Delete a product"""
    if 'merchant_id' not in session:
        flash('يرجى تسجيل الدخول أولاً', 'warning')
        return redirect(url_for('login'))
    
    merchant_id = session['merchant_id']
    
    # Find the product
    product_index = next((i for i, p in enumerate(products) 
                         if p['id'] == product_id and p['merchant_id'] == merchant_id), None)
    
    if product_index is not None:
        products.pop(product_index)
        flash('تم حذف المنتج بنجاح', 'success')
    else:
        flash('لم يتم العثور على المنتج', 'danger')
    
    return redirect(url_for('dashboard'))

# Add some sample products for testing
def add_sample_products():
    if not products:
        sample_products = [
            {
                "id": str(uuid.uuid4()),
                "name": "هاتف ذكي",
                "description": "هاتف ذكي جديد بمواصفات عالية",
                "image": "https://cdn.pixabay.com/photo/2016/11/29/12/30/android-1869510_960_720.jpg",
                "price": "500",
                "merchant_id": "1",
                "phone": "9123456789"
            },
            {
                "id": str(uuid.uuid4()),
                "name": "لابتوب متطور",
                "description": "لابتوب سريع مناسب للألعاب والعمل",
                "image": "https://cdn.pixabay.com/photo/2016/03/27/07/12/apple-1282241_960_720.jpg",
                "price": "1200",
                "merchant_id": "1",
                "phone": "9123456789"
            },
            {
                "id": str(uuid.uuid4()),
                "name": "سماعات لاسلكية",
                "description": "سماعات بجودة صوت عالية مع عزل الضوضاء",
                "image": "https://cdn.pixabay.com/photo/2018/09/17/14/27/headphones-3683983_960_720.jpg",
                "price": "150",
                "merchant_id": "1",
                "phone": "9123456789"
            }
        ]
        products.extend(sample_products)

# Add sample products when app starts
add_sample_products()
