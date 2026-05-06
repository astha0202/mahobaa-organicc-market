from flask import Blueprint, render_template, request

main_bp = Blueprint("main", __name__)

# 🔹 Shops
shops_data = [
    {"id":1,"name":"Aashiyana","image":"/static/images/shops/aashiyana.png"},
    {"id":2,"name":"FPO 2","image":"/static/images/shops/default.jpg"},
    {"id":3,"name":"Achyutam","image":"/static/images/shops/default.jpg"},
    {"id":4,"name":"Kisan Jaivik Utpadak Sangathan","image":"/static/images/shops/default.jpg"},
    {"id":5,"name":"Green Valley","image":"/static/images/shops/default.jpg"},
    {"id":6,"name":"Desi Organic","image":"/static/images/shops/default.jpg"},
    {"id":7,"name":"Farm Fresh","image":"/static/images/shops/default.jpg"},
    {"id":8,"name":"Nature Basket","image":"/static/images/shops/default.jpg"},
    {"id":9,"name":"Healthy Harvest","image":"/static/images/shops/default.jpg"},

    # 🔥 VEDIC SPECIAL IMAGE
    {"id":10,"name":"Vedic Foods","image":"/static/images/shops/vedic.jpg"}
]

# 🔹 Products
products_data = [

# ===== SHOP 1 : AASHIYANA =====
{"product_id":1,"name":"Masoor Dal","price":100,"shop_id":1,"shop_name":"Aashiyana","image":"/static/images/products/masoor.jpg"},
{"product_id":2,"name":"Arhar Dal","price":120,"shop_id":1,"shop_name":"Aashiyana","image":"/static/images/products/arhar.jpg"},
{"product_id":3,"name":"Moong Chhilka Dal","price":110,"shop_id":1,"shop_name":"Aashiyana","image":"/static/images/products/moong.jpg"},
{"product_id":4,"name":"Urad Chhilka Dal","price":130,"shop_id":1,"shop_name":"Aashiyana","image":"/static/images/products/urad.jpg"},

# ===== SHOP 2 : FPO 2 =====
{"product_id":5,"name":"Masoor Dal","price":95,"shop_id":2,"shop_name":"FPO 2","image":"/static/images/products/masoor.jpg"},
{"product_id":6,"name":"Arhar Dal","price":115,"shop_id":2,"shop_name":"FPO 2","image":"/static/images/products/arhar.jpg"},
{"product_id":7,"name":"Moong Chhilka Dal","price":105,"shop_id":2,"shop_name":"FPO 2","image":"/static/images/products/moong.jpg"},
{"product_id":8,"name":"Urad Chhilka Dal","price":125,"shop_id":2,"shop_name":"FPO 2","image":"/static/images/products/urad.jpg"},

# ===== SHOP 3 : ACHYUTAM =====
{"product_id":9,"name":"Masoor Dal","price":90,"shop_id":3,"shop_name":"Achyutam","image":"/static/images/products/masoor.jpg"},
{"product_id":10,"name":"Arhar Dal","price":110,"shop_id":3,"shop_name":"Achyutam","image":"/static/images/products/arhar.jpg"},
{"product_id":11,"name":"Moong Chhilka Dal","price":100,"shop_id":3,"shop_name":"Achyutam","image":"/static/images/products/moong.jpg"},
{"product_id":12,"name":"Urad Chhilka Dal","price":120,"shop_id":3,"shop_name":"Achyutam","image":"/static/images/products/urad.jpg"},

# ===== SHOP 4 : KISAN =====
{"product_id":13,"name":"Masoor Dal","price":100,"shop_id":4,"shop_name":"Kisan Jaivik Utpadak Sangathan","image":"/static/images/products/masoor.jpg"},
{"product_id":14,"name":"Arhar Dal","price":120,"shop_id":4,"shop_name":"Kisan Jaivik Utpadak Sangathan","image":"/static/images/products/arhar.jpg"},
{"product_id":15,"name":"Moong Chhilka Dal","price":110,"shop_id":4,"shop_name":"Kisan Jaivik Utpadak Sangathan","image":"/static/images/products/moong.jpg"},
{"product_id":16,"name":"Urad Chhilka Dal","price":130,"shop_id":4,"shop_name":"Kisan Jaivik Utpadak Sangathan","image":"/static/images/products/urad.jpg"},

# ===== SHOP 10 : VEDIC =====
{"product_id":17,"name":"Masoor Dal","price":105,"shop_id":10,"shop_name":"Vedic Foods","image":"/static/images/products/masoor.jpg"},
{"product_id":18,"name":"Arhar Dal","price":125,"shop_id":10,"shop_name":"Vedic Foods","image":"/static/images/products/arhar.jpg"},
{"product_id":19,"name":"Moong Chhilka Dal","price":115,"shop_id":10,"shop_name":"Vedic Foods","image":"/static/images/products/moong.jpg"},
{"product_id":20,"name":"Urad Chhilka Dal","price":135,"shop_id":10,"shop_name":"Vedic Foods","image":"/static/images/products/urad.jpg"},

]

# 🏠 HOME
@main_bp.route("/")
def home():
    return render_template("index.html", shops=shops_data)

# 🏪 ALL SHOPS
@main_bp.route("/shops")
def shops():
    return render_template("shops.html", shops=shops_data)

# 🔍 SEARCH (multi-shop)
@main_bp.route("/search")
def search():
    query = request.args.get("q", "").lower()

    words = query.split()

    results = []

    for p in products_data:
        name = p["name"].lower()

        if any(word in name for word in words):
            results.append(p)

    return render_template("product.html", products=results)