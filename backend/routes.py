from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@db:5432/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Модель
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255))

# Создание таблиц сразу при старте приложения
with app.app_context():
    db.create_all()

# CRUD операции
@app.route("/products", methods=["POST"])
def create_product():
    data = request.json
    p = Product(name=data["name"], price=data["price"], description=data.get("description"))
    db.session.add(p)
    db.session.commit()
    return jsonify({"id": p.id}), 201

@app.route("/products", methods=["GET"])
def get_products():
    products = Product.query.all()
    return jsonify([{"id": p.id, "name": p.name, "price": p.price, "description": p.description} for p in products])

@app.route("/products/<int:id>", methods=["PUT"])
def update_product(id):
    data = request.json
    p = Product.query.get_or_404(id)
    p.name = data.get("name", p.name)
    p.price = data.get("price", p.price)
    p.description = data.get("description", p.description)
    db.session.commit()
    return jsonify({"message":"Updated"}),200

@app.route("/products/<int:id>", methods=["DELETE"])
def delete_product(id):
    p = Product.query.get_or_404(id)
    db.session.delete(p)
    db.session.commit()
    return jsonify({"message":"Deleted"}),200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
