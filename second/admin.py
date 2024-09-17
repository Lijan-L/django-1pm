from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(category)
class categpry_admin(admin.ModelAdmin):
    list_display=['category_name','slug']
    prepopulated_fields={'slug':('category_name',)}

# class Meta:
#     verbose_name_pural='categories'


@admin.register(product)
class admin_Product(admin.ModelAdmin):
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    list_display = ['name', 'slug', 'price', 'is_available', 'image','discount_price']
    # list_editable = ['price', 'is_available', 'status']
    # prepopulated_fields = {'slug': ('name',)}
    # list_per_page = 5
    # search_fields = ['name', 'price', 'is_available', 'status']
@admin.register(product2)
class admin_Product2(admin.ModelAdmin):
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    list_display = ['name', 'slug', 'price', 'is_available', 'image2','discount_price']

@admin.register(asettings)
class admin_set(admin.ModelAdmin):
    list_display=['a_name','a_logo','a_email','a_phone',]

@admin.register(ad) 
class ad_admin(admin.ModelAdmin):
    list_display=['adname','addlogo']   


@admin.register(agx) 
class agx_admin(admin.ModelAdmin):
    list_display=['agxname','agxlogo'] 

@admin.register(fo)
class fo_admin(admin.ModelAdmin):
    list_display=['foname','fologo','foprice']      

@admin.register(review)
class rev_admin(admin.ModelAdmin):
    list_display=['re_name','re_logo','re_prof','re_dep']   

@admin.register(footer)
class fot_admin(admin.ModelAdmin):
    list_display=['footaddress','footph','footemail','we','we1','we2','we3']

@admin.register(two)
class two_admin(admin.ModelAdmin):
    list_display=['twon','twoim','twopr']