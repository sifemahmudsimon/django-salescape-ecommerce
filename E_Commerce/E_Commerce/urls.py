from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static 
from .import views


urlpatterns = [
    #error page
    path('404',views.Error404, name="404" ),

    path('admin/', admin.site.urls),
    path('base/',views.BASE,name='base'),

    #pages
    path("", views.HOME, name="home"),
    path('about',views.ABOUT,name='about'),
    path('contact',views.CONTACT,name='contact'),
    path('product',views.PRODUCT,name='product'),

    path('product/<slug:slug>/',views.PRODUCT_DETAILS, name='product_detail'), 

    # account urls
    path('account/my-account',views.MY_ACCOUNT,name='my_account'),
    path('account/register',views.REGISTER,name='handleregister'),
    path('account/login',views.LOGIN,name='handlelogin'),
    path('account/profile',views.PROFILE, name='profile'),
    path('account/profile/update',views.PROFILE_UPDATE, name='profile_update'),
    #user accounts
    path('accounts/', include('django.contrib.auth.urls')),

     #cart
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
    path('myorder/',views.myorder,name='myorder'),
    path('orderlist/',views.orderlist,name='orderlist'),
    path('submitoffer/<int:product_id>/',views.submitoffer,name='submitoffer')

] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Add this line separately