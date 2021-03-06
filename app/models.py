from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login
import pyotp

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    otp_secret = db.Column(db.String(32))

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        if self.otp_secret is None:
            # generate a random secret
            self.otp_secret = pyotp.random_base32()

    def __repr__(self):
        return '<User {}>'.format(self.username)  

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_totp_uri(self):
        return 'otpauth://totp/mikeralph:{0}?secret={1}&issuer=mikeralph' \
            .format(self.username, self.otp_secret)

    def verify_totp(self, token):
        return pyotp.TOTP(self.otp_secret).verify(token)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(64), unique=True, nullable=False)
    priority = db.Column(db.Integer, unique=True)
    img_filename = db.Column(db.String(64))
    description = db.Column(db.String(1024))
    product_subtype_list = db.relationship('Product_Subtype', backref='product', lazy='dynamic')
    product_images = db.relationship('Product_Image', backref='product', lazy='dynamic')

class Product_Subtype(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    width = db.Column(db.Numeric(10, 2))
    length = db.Column(db.Numeric(10, 2))
    height = db.Column(db.Numeric(10, 2))
    price = db.Column(db.Numeric(10, 2))

class Product_Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img_filename = db.Column(db.String(64))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    priority = db.Column(db.Integer)
