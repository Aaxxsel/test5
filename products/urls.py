from django.urls import path

from products.views import *

urlpatterns = [
    path('', index, name='index'),
    path('category/', categories, name='categories'),
    path('product/<slug:slug>/', product_detail, name='product_detail'),

]
