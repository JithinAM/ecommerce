from django.shortcuts import render
from django.urls import reverse
from . models import Product
from django.core.paginator import Paginator
from .forms import ProductSearchForm
# Create your views here.



def index(request):
    featured_products=Product.objects.order_by('priority')[:4]
    latest_products=Product.objects.order_by('-id')[:4]
    context={
        'featured_products':featured_products,
        'latest_products':latest_products
    }
    return render(request ,'index.html',context)



def list_products(request):
    page=1
    if request.GET:
        page=request.GET.get('page',1)
    product_list=Product.objects.order_by('priority')
    product_paginator=Paginator(product_list,8)
    product_list=product_paginator.get_page(page)
    context={'products':product_list}
    return render(request ,'products.html',context)



def detail_product(request,pk):
    product=Product.objects.get(pk=pk)
    context={'product':product}
    return render(request ,'product_detail.html',context)
    
def search_view(request):
    search_query = request.GET.get('search_query', '')
    results = Product.objects.filter(title__icontains=search_query)
    all_results = []

    for result in results:
        url = reverse('detail_product', args=[result.id])  # Assuming 'product_detail' is the name of the view for product details
        all_results.append({'product': result, 'url': url})

    context = {'search_results': all_results, 'search_query': search_query}
    
    return render(request, 'search.html', context)

    