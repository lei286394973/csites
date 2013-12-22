# coding: utf-8
from django.shortcuts import render_to_response

def index(request):
    return render_to_response('index.html')


def about_us(request):
    return render_to_response('about_us.html')


def news(request):
    return render_to_response('news.html')
    

def news_detail(request):
    return render_to_response('news_detail.html')


def message(request):
    return render_to_response('message.html')


def product_detail(request):
    return render_to_response('product_detail.html')


def products(request):
    return render_to_response('products.html')
    
    
def contact_us(request):
    return render_to_response('contact_us.html')
