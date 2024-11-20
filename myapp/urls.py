# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('create_product/', views.create_product, name='create_product'),
    path('get_products/', views.get_products, name='get_product'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('update_product/<int:product_id>/', views.update_product, name='update_product'),
]
