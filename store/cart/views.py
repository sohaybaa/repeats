from decimal import Decimal
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from store.models import Product
from store.cart.cart import Cart            # session-based cart
from vouchers.forms import VoucherApplyForm

def _apply_voucher_to_totals(request, subtotal: Decimal):
    v = request.session.get("voucher", {})
    discount = Decimal(str(v.get("amount", 0))) if v else Decimal("0")
    new_total = subtotal - discount
    if new_total < 0:
        new_total = Decimal("0")
    return (discount, new_total)

def cart_detail(request):
    cart = Cart(request)
    subtotal = cart.total()
    discount, new_total = _apply_voucher_to_totals(request, subtotal)
    context = {
        "cart": cart,
        "total": subtotal,
        "counter": cart.count(),
        "voucher_apply_form": VoucherApplyForm(),
        "voucher": request.session.get("voucher", {}),
        "discount": discount,
        "new_total": new_total,
    }
    return render(request, "store/cart.html", context)

def add_cart(request, product_id):
    get_object_or_404(Product, id=product_id)
    qty = int(request.POST.get("qty", 1))
    if qty < 1: qty = 1
    Cart(request).add(product_id, qty=qty)
    messages.success(request, "Item added to cart.")
    return redirect("store:cart_detail")

def cart_remove(request, product_id):
    cart = Cart(request)
    current_qty = 0
    for item in cart:
        if item["product"].id == product_id:
            current_qty = item["qty"]
            break
    if current_qty > 1:
        cart.add(product_id, qty=current_qty - 1, override=True)
    else:
        cart.remove(product_id)
    messages.info(request, "Item updated.")
    return redirect("store:cart_detail")

def full_remove(request, product_id):
    Cart(request).remove(product_id)
    messages.info(request, "Item removed.")
    return redirect("store:cart_detail")

def empty_cart(request):
    Cart(request).clear()
    messages.info(request, "Cart emptied.")
    return redirect("store:product_list")

def create_order(request):
    if Cart(request).count() == 0:
        messages.warning(request, "Your cart is empty.")
        return redirect("store:product_list")
    return redirect("order:checkout")
