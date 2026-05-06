from flask import Blueprint, session, redirect, request, render_template

cart_bp = Blueprint("cart", __name__)

@cart_bp.route("/add_to_cart")
def add_to_cart():
    product = request.args.get("product")
    price = int(request.args.get("price"))
    qty = int(request.args.get("qty", 1))  # default qty = 1

    if "cart" not in session:
        session["cart"] = []

    session["cart"].append({
        "product": product,
        "price": price,
        "qty": qty
    })

    session.modified = True
    return redirect("/cart")


@cart_bp.route("/cart")
def cart():
    cart = session.get("cart", [])

    # FIX: price string nahi, int hona chahiye
    total = sum(item["price"] * item["qty"] for item in cart)

    return render_template("cart.html", cart=cart, total=total)


@cart_bp.route("/buy_now")
def buy_now():
    product = request.args.get("product")
    price = int(request.args.get("price"))

    # qty bhi add karo (warna error aayega)
    session["cart"] = [{
        "product": product,
        "price": price,
        "qty": 1
    }]

    return redirect("/payment")