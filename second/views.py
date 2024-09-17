from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from . import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .models import two,cart,CartItem,Wishlist
from django.contrib.auth.decorators import login_required

# from .forms import RegisterForm
# Create your views here.

def index(request):

    data={
        'bannerpro':models.product.objects.order_by('-id'),
        'bannerdown':models.product2.objects.order_by('-id')[:15],
        'ado':models.ad.objects.order_by('-id')[:15],
        'igx':models.agx.objects.order_by('-id')[:15],
        'foa':models.fo.objects.order_by('-id')[:15],
        're':models.review.objects.order_by('-id')[:15],
    }
    return render(request, 'pages/index.html',data)



# @login_required
def cart(request,product_id):
    two = get_object_or_404(two, id=product_id)
    cart, created = cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=two)

    if not created:
        cart_item.quantity += 1
        cart_item.save()
    else:
        cart_item.quantity = 1
        cart_item.save()

    return render(request,'pages/cart.html')

def cart_view(request):
    cart, created = cart.objects.get_or_create(user=request.user)
    cart_items = cart.cartitem_set.all()
    return render(request, 'shop/cart.html', {'cart_items': cart_items})


def remove_from_cart(request, product_id):

    cart = get_object_or_404(cart, user=request.user)

 
    cart_item = get_object_or_404(CartItem, cart=cart, product__id=product_id)
    cart_item.delete()

    # Redirect to the cart view
    return redirect('cart')


def update_cart_item_quantity(request, product_id):
 
    cart = get_object_or_404(cart, user=request.user)

  
    cart_item = get_object_or_404(CartItem, cart=cart, product__id=product_id)

def signup(request):
    if request.method=='POST':
        username=request.POST.get('Username')
        useremail=request.POST.get('Email')
        userpass=request.POST.get('Password')    
        my_user=User.objects.create_user(username,useremail,userpass)
        my_user.save()
        return redirect('loginn')
      
    return render(request,'pages/signup.html')


    #     uname=request.POST.get('Username')
    #     upassword=request.POST.get('Password')
    #     uemail=request.POST.get('Email')
    #     my_user=User.objects.create_user(uname,upassword,uemail)
    #     my_user.save()
    #     return redirect('loginn')   
    # return render(request,'pages/signup.html')

def loginn(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
           messages.error(request,'Invalid username or password')

    return render(request,'pages/loginn.html')


 
def checkout(request):
    cart, created = cart.objects.get_or_create(user=request.user)
    cart_items = cart.cartitem_set.all()
    total = 0
    for item in cart_items:
        total += item.product.price * item.quantity

    if request.method == 'POST':
      
        payment_method = request.POST.get('payment_method')
        if payment_method == 'credit_card':
         
            card_number = request.POST.get('card_number')
            expiration_date = request.POST.get('expiration_date')
            cvv = request.POST.get('cvv')
            
            
            # if payment_successful:
             
            #     order = models.Order.objects.create(user=request.user, total=total)
            #     for item in cart_items:
            #         order_item = models.OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)
            #     cart.status = 'paid'
            #     cart.save()
            #     return redirect('order_success')
            # else:
            #     messages.error(request, 'Payment failed')
        elif payment_method == 'paypal':
            # Process PayPal payment
            # ...
            # Redirect to PayPal payment page
            return redirect('paypal_payment_page')
        else:
            messages.error(request, 'Invalid payment method')

    return render(request, 'pages/checkout.html', {'cart_items': cart_items, 'total': total})
    # return render(request,'pages/checkout.html')

def contact(request):
    return render(request,'pages/contact.html')

def myaccount(request):
    return render(request,'pages/myaccount.html')

def productdetail(request):
    data={
        'tw':models.two.objects.order_by('-id')[:15],
        'ado':models.ad.objects.order_by('-id')[:15],
        'foa':models.fo.objects.order_by('-id')[:15],

    }
    return render(request,'pages/productdetail.html',data)

def productlist(request):
    data={
        'tw':models.two.objects.order_by('-id')[:15],

    }
    return render(request,'pages/productlist.html',data)

def wishlist(request,product_id):
    product = get_object_or_404(two, id=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user, product=product)
    if not created:
        messages.error(request, "Product already in wishlist")
    else:
        messages.success(request, "Product added to wishlist")
    return redirect('productdetail')

    
    # return render(request,'pages/wishlist.html')

def remove_from_wishlist(request, product_id):
    product = get_object_or_404(two, id=product_id)
    wishlist = get_object_or_404(Wishlist, user=request.user, product=product)
    wishlist.delete()
    messages.success(request, "Product removed from wishlist")
    return redirect('wishlist')

def wishlist_view(request):
    wishlist = Wishlist.objects.filter(user=request.user)
    return render(request, 'pages/wishlist.html', {'wishlist': wishlist})