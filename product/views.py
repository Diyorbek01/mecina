from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView
from product.models import Product, Category, Review


# Create your views here.
def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {
        'products_all': products,
        'categories': categories
    }
    return render(request, "shop.html", context)

class IndexView(ListView):
    model = Product
    template_name = 'shop.html'
    paginate_by = 12
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        products_all = Product.objects.all()
        categories = Category.objects.all()

        paginator = Paginator(products_all, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            file_exams = paginator.page(page)
        except PageNotAnInteger:
            file_exams = paginator.page(1)
        except EmptyPage:
            file_exams = paginator.page(paginator.num_pages)
       
        context['products_all'] = file_exams
        context['categories'] = categories
        return context


def filter_product(request, id):
    categories = Category.objects.all()
    products = Product.objects.filter(category=id)
    context = {
        'products_all': products,
        'categories': categories,
        "id_category": id
    }
    return render(request, "shop.html", context)


def details(request, id):
    product = get_object_or_404(Product, pk=id)
    products = Product.objects.all()
    related_products = Product.objects.filter(category=product.category)[:4]
    context = {
        'product': product,
        'products_all': products,
        'related_products': related_products,
    }
    return render(request, "product-details.html", context)


@login_required(login_url='/login')
def review(request):
    url = request.META.get('HTTP_REFERER')
    if not Review.objects.filter(user=request.user, product_id=request.POST.get('product_id')).exists():
        product_id = request.POST.get('product_id')
        rate = request.POST.get('rating')
        comment = request.POST.get('comment')

        Review.objects.create(
            user=request.user,
            product_id=product_id,
            rate=rate,
            comment=comment
        )
        messages.success(request, "Commented successfully!")
        return HttpResponseRedirect(url)
    else:
        messages.warning(request, "You have already rated for this product!")
        return HttpResponseRedirect(url)
