from django.urls import path
from django.views.generic.detail import DetailView
from . import views
from .models import Product

app_name = 'shop'
urlpatterns = [
    path('', views.index, name='index'),
    path('index_product/<int:id>/', views.index_product, name='index_product' )
]

