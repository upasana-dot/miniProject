from extensions import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_code = db.Column(db.String(100), unique=True, nullable=False)
    product_name = db.Column(db.String(100), nullable=False)
    stock = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"<Product {self.product_code}>"