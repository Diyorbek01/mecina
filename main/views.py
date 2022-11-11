from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from main.models import Contact, Subscription, Blog
from operation.models import OrderProduct
from product.models import Product, Category


# Create your views here.
def index(request):
    last_4_products = Product.objects.all().order_by("-created_at")[:4]
    last_6_products = Product.objects.all().order_by("-created_at")[:6]
    best_sellers_products = Product.objects.all().order_by("-count_sold")[:6]
    products_all = Product.objects.all()
    categories = Category.objects.all()
    context = {
        'last_4_products': last_4_products,
        'last_6_products': last_6_products,
        'best_sellers_products': best_sellers_products,
        'products_all': products_all,
        'categories': categories,
    }
    return render(request, "index.html", context)


def about(request):
    return render(request, "about.html")


def blog(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, "blog.html", context)


def blog_details(request, id):
    blog = Blog.objects.get(id=id)
    latest_blogs = Blog.objects.all().order_by("-created_at")[:5]
    context = {
        'blog_': blog,
        'latest_blogs': latest_blogs
    }
    return render(request, "blog-details.html", context)


def contact(request):
    if request.method == "POST":
        subject = request.POST.get("subject")
        name = request.POST.get("name")
        email = request.POST.get("email")
        text = request.POST.get("text")

        Contact.objects.create(
            subject=subject,
            name=name,
            email=email,
            text=text,
        )
        messages.success(request, 'Your message has been sent!')
    return render(request, "contact.html")


def subscription(request):
    email = request.POST.get("email")

    Subscription.objects.create(
        email=email
    )
    messages.success(request, 'Thanks for your subscription')
    return HttpResponseRedirect('/')


def login_register(request):
    if request.method == "POST":
        status = request.POST.get('status')
        if status == "register":
            try:
                phone_number = request.POST.get('phone_number')
                full_name = request.POST.get('full_name')
                password = request.POST.get('password')
                user_instance = User.objects.create(
                    username=phone_number,
                    first_name=full_name,
                )
                user_instance.set_password(password)
                user_instance.save()
                user = authenticate(username=phone_number, password=password)
                if user is not None:
                    login(request, user)
                messages.success(request, 'Your account has been created!')
                return HttpResponseRedirect('/')
            except:
                messages.success(request, 'Something went wrong!')
                return HttpResponseRedirect('/login')
        elif status == "login":
            phone_number = request.POST['phone_number']
            password = request.POST['password']
            user = authenticate(username=phone_number, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                messages.warning(request, "Login Error !! Phone number or Password is incorrect")
                return HttpResponseRedirect('/login')
    return render(request, "login-register.html")


def logout_func(request):
    logout(request)
    return HttpResponseRedirect('/')
