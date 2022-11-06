from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from main.models import Setting
from operation.models import Cart, Order, OrderProduct, Wishlist
from product.models import Product


# Create your views here.
@login_required(login_url='/login')
def cart(request):
    cart = Cart.objects.filter(
        user=request.user
    )
    total = 0
    for i in cart:
        total += i.amount * i.product.price
    context = {
        'cart': cart,
        'total': total,
    }
    return render(request, "cart.html", context)


@login_required(login_url='/login')
def insert(request):
    user_id = request.user.id
    request.session['order_count'] = Cart.objects.filter(user_id=user_id).count()
    id = request.POST.get('product_id')
    quantity = int(request.POST.get('amount'))
    url = request.META.get('HTTP_REFERER')  # get last url
    current_user = request.user  # Access User Session information
    checkinproduct = Cart.objects.filter(product=id, user_id=user_id)  # Check product in shopcart
    if checkinproduct:
        control = 1  # The product is in the cart
    else:
        control = 0  # The product is not in the cart"""
    if request.method == 'POST':  # if there is a post
        if control == 1:  # Update  shopcart
            data = Cart.objects.get(product=id, user_id=user_id)
            data.amount += quantity
            data.save()  # save data
        else:  # Inser to Shopcart
            data = Cart()
            data.user_id = user_id  # current_user.id
            data.product_id = id
            data.amount = quantity
            data.save()
        Wishlist.objects.filter(user=user_id, product_id=id).delete()
        messages.success(request, "Added to cart successfully!")
        return HttpResponseRedirect(url)

    else:  # if there is no post
        if control == 1:  # Update  shopcart
            data = Cart.objects.get(product=id, user_id=user_id)
            data.amount += 1
            data.save()  #
        else:  # Insert to Shopcart
            data = Cart()  # model ile bağlantı kur
            data.user_id = current_user.id
            data.product_id = id
            data.amount = 1
            data.save()  #
        Wishlist.objects.filter(user=user_id, product_id=id).delete()
        messages.success(request, "Added to cart successfully!")
        return HttpResponseRedirect(url)


@login_required(login_url='/login')
def create_order(request):
    user_id = request.user.id
    shopcart = Cart.objects.filter(user_id=user_id)
    total = 0
    total_products = 0
    for i in shopcart:
        total_products += int(i.amount)
        total += int(i.amount) * int(i.product.price)

    order = Order.objects.create(
        user_id=user_id,
        total_summa=total,
        number_of_products=total_products,
    )

    for i in shopcart:
        OrderProduct.objects.create(
            user_id=user_id,
            order_id=order.id,
            product=i.product,
            quantity=i.amount,
            price=i.product.price,
            amount=i.product.price * i.amount
        )

    messages.success(request, "Your order has been accepted!")
    Cart.objects.filter(user_id=user_id).delete()
    return HttpResponseRedirect('/')


@login_required(login_url='/login')
def delete(request, id):
    Cart.objects.get(id=id).delete()
    return HttpResponseRedirect('/')


@login_required(login_url='/login')
def wishlist(request):
    if request.method == "POST":
        url = request.META.get('HTTP_REFERER')
        product_id = request.POST.get("product_id")
        if Wishlist.objects.filter(user_id=request.user.id, product_id=product_id).exists():
            messages.warning(request, "This product is already in the wishlist")
            return HttpResponseRedirect(url)
        else:
            Wishlist.objects.create(user=request.user, product_id=product_id)
            messages.success(request, "Added to wishlist successfully!")
            return HttpResponseRedirect(url)
    wishlists = Wishlist.objects.filter(user=request.user)
    context = {
        'wishlists': wishlists
    }
    return render(request, "wishlist.html", context)


@login_required(login_url='/login')
def delete_wishlist(request, id):
    Wishlist.objects.get(id=id).delete()
    return HttpResponseRedirect('/order/wishlist')


def processor(request):
    setting = Setting.objects.last()
    if request.user.is_authenticated:
        number_wishlist = Wishlist.objects.filter(user=request.user).count()
        number_shop_cart = Cart.objects.filter(user=request.user).count()
        cart = Cart.objects.filter(user=request.user)
        total = 0
        for i in cart:
            total += i.amount * i.product.price
        context = {
            "full_name": request.user.first_name,
            'number_wishlist': number_wishlist,
            'number_shop_cart': number_shop_cart,
            "carts": cart,
            "total": total,
            "setting": setting,
        }
        return context
    else:
        context = {
            "full_name": None,
            'number_wishlist': 0,
            'number_shop_cart': 0,
            "carts": None,
            "total": 0,
            "setting": setting
        }
        return context