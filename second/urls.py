
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('index',views.index,name='index'),
    path('cart',views.cart,name='cart'),
    path('checkout',views.checkout,name='checkout'),
    path('contact',views.contact,name='contact'),
    path('signup',views.signup,name='signup'),
    path('loginn',views.loginn,name='loginn'),
    path('myaccount',views.myaccount,name='myaccount'),
    path('productdetail',views.productdetail,name='productdetail'),
    path('productlist',views.productlist,name='productlist'),
    path('wishlist',views.wishlist,name='wishlist'),
   
]
