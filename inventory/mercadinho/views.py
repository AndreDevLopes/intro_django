from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView, ListView

from .models import Product


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    module = Product
