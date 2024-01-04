from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff',)


class Product_Images(admin.TabularInline):
    model = Product_Image
class Additional_Informations(admin.TabularInline):
    model = Additional_Information
class Product_Admin(admin.ModelAdmin):
    inlines = [Product_Images, Additional_Informations]
    list_display = ('product_name','price','Catagorys','section')
    list_editable = ('Catagorys','section')

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    fields = ('product_name', 'quantity', 'price',)
    readonly_fields = ('product_name', 'quantity', 'price',)

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline,]
    list_display = ('id','get_user_full_name', 'address','created_at','packaged','dispatched','delivered')   
    def get_user_full_name(self, obj):
        return obj.user.get_full_name() if obj.user else 'N/A'  # Replace 'user' with the actual field name

    get_user_full_name.short_description = 'User Full Name'

admin.site.register(UserProfile)
admin.site.register(Section)
admin.site.register(Product,Product_Admin)
admin.site.register(Product_Image)
admin.site.register(Additional_Information)

# Register your models here.
admin.site.register(slider)
admin.site.register(banner_area)

#Menu Catagory
admin.site.register(Main_Catagory)
admin.site.register(Catagory)
admin.site.register(Sub_Catagory)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem)
admin.site.unregister(User)
# Register UserAdmin with your customizations
admin.site.register(User, CustomUserAdmin)


admin.site.register(NegotiationPannel)