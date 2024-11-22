# myapp/urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.hello, name='hello'),
    path('login/', views.login_view, name='login'),


 #<------- CRUD operations for user --------->

path('create_user/', views.create_user, name='create_user'),
path('get_users/', views.get_users, name='get_users'),
path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
path('update_user/<int:user_id>/', views.update_user, name='update_user'),



 #<------- CRUD operations for products --------->
path('create_product/', views.create_product, name='create_product'),
path('get_products/', views.get_products, name='get_product'),
path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
path('update_product/<int:product_id>/', views.update_product, name='update_product'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
