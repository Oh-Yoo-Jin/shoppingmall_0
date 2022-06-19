from django.urls import path
from django.views.generic.detail import DetailView
from . import views
from .models import Product

app_name = 'detail'
urlpatterns = [
    path('detail_top/', views.detail_top, name='detail_top'),
    path('detail_bottom/', views.detail_bottom, name='detail_bottom'),
    path('detail_product/<int:id>/', views.detail_product, name='detail_product')
]
