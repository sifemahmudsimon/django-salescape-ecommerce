from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_vendor')
    def is_vendor(self, obj):
        return obj.userprofile.is_vendor if hasattr(obj, 'userprofile') else False
    is_vendor.boolean = True
    is_vendor.short_description = 'Vendor'


class Product_Images(admin.TabularInline):
    model = Product_Image
class Additional_Informations(admin.TabularInline):
    model = Additional_Information
class Product_Admin(admin.ModelAdmin):
    inlines = [Product_Images, Additional_Informations]
    list_display = ('product_name','price','Catagorys','section')
    list_editable = ('Catagorys','section')
    


# PRODUCT DESCRIPTIONS
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

admin.site.unregister(User)
# Register UserAdmin with your customizations
admin.site.register(User, CustomUserAdmin)