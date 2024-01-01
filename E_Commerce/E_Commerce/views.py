from django.shortcuts import render,redirect
from app.models import slider,banner_area,Main_Catagory,Product,Catagory,User,UserProfile

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.contrib import messages
from cart.cart import Cart

def BASE(request):
    return render(request,'base.html')

#pages views
def HOME(request):
    sliders = slider.objects.all().order_by('-id')[0:3]
    banners = banner_area.objects.all().order_by('-id')[0:3]

    main_catagory = Main_Catagory.objects.all()

    product = Product.objects.filter(section__name='Top Deals of The Day')
    
    context = {
        'sliders':sliders,
        'banners':banners,
        'main_catagory':main_catagory,
        'product':product,
    }
    return render(request,'Main/home.html',context)

def ABOUT(request):
    return render(request,'Main/about.html')

def CONTACT(request):
    return render(request,'Main/contact.html')





#USER VIEWS
def MY_ACCOUNT(request):
    return render(request,'account/my-account.html')

def REGISTER (request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        is_vendor = request.POST.get('is_vendor') == 'on'

        if User.objects.filter(username = username).exists():
            messages.error(request,'This username is already exsists')
            return redirect('login')
       
        if User.objects.filter(email = email).exists():
            messages.error(request,'This email is already exsists')
            return redirect('login')

        user = User(
            username = username,
            email = email,
            
        )
        user.set_password(password)
        user.save()
        user_profile = UserProfile.objects.create(user=user, is_vendor=is_vendor)
        user_profile.save()
        return redirect('login')

def LOGIN(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Email or Password is invalid !')
            return redirect('login')

@login_required(login_url='/accounts/login/')
def PROFILE(request):
    return render(request,'profile/profile.html')
@login_required(login_url='/accounts/login/')
def PROFILE_UPDATE(request):
    if request.method == 'POST':
        #get data from Form by POST method
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_id = request.user.id

        #set data to Form value
        user = User.objects.get(id=user_id)
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email

        if password != None and password != "":
            user.set_password(password)
        user.save()
        messages.success(request,'Your profile is successfully updated !')

    return redirect('profile')

#PRODUCT SECTION
def PRODUCT(request):

    catagory = Catagory.objects.all
    selected_catagory_id  = request.GET.get('catagory_id')

    if selected_catagory_id:
        selected_category = Catagory.objects.get(id=selected_catagory_id)
        product = Product.objects.filter(Catagorys=selected_category)
    else:
        product = Product.objects.all()
    
        
    context = {
        'catagory':catagory,
        'product':product,
    }

    return render(request,'product/product.html',context)

def PRODUCT_DETAILS(request,slug):
    product = Product.objects.filter(slug = slug)
    if product.exists():
        product = Product.objects.get(slug = slug)
    else:
        return redirect('404')

    context = {'product':product}
    return render(request,'product/product_detail.html',context)

def Error404(request):
    return render(request,'errors/404.html')

#CART SECTION
@login_required(login_url="/accounts/login/")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def cart_detail(request):
    cart = request.session.get('cart')
    packing_cost=sum(i['packing_cost'] for i in cart.values() if i)
    tax=sum(i['tax'] for i in cart.values() if i)

    context = {
        'packing_cost':packing_cost,
        'tax':tax,
    }
    return render(request, 'cart/cart.html',context)


def Checkout(request):
    return render(request,'checkout/checkout.html')

def vendor_dashbord(request):
    pass 




# Install django-filter
#whitenoise
#templatetag