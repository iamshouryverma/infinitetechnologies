from django.contrib import admin
from .models import Service, Indexbanner, Maplocation, Footer, Header, IndexProducts, Whywe, Visitingcard, ProductsArchitecture, ProductsCategory, ProductsGame, ProductsDesign, ServicesCategory

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_title', 'service_desc')

class IndexbannerAdmin(admin.ModelAdmin):
    list_display = ('banner_img',)

class MaplocationAdmin(admin.ModelAdmin):
    list_display = ('map_location',)

class FooterAdmin(admin.ModelAdmin):
    list_display = ('address','copyright')
    
class HeaderAdmin(admin.ModelAdmin):
    list_display = ( 'navbar_link', 'navbar_icon', 'navbar_content')

class IndexProductsAdmin(admin.ModelAdmin):
    list_display = ( 'index_product_title', 'index_product_img','index_external_link')

class ProductsCategoryAdmin(admin.ModelAdmin):
    list_display = ( 'product_category_title', 'product_category_desc', 'product_category_img','external_category_link')

class ServicesCategoryAdmin(admin.ModelAdmin):
    list_display = ( 'services_category_title', 'services_category_desc', 'services_category_img')

class ProductsArchitectureAdmin(admin.ModelAdmin):
    list_display = ( 'architecture_product_title', 'architecture_product_desc', 'architecture_product_img','architecture_external_link')

class ProductsGameAdmin(admin.ModelAdmin):
    list_display = ( 'game_product_title', 'game_product_desc', 'game_product_img','game_external_link')

class ProductsDesignAdmin(admin.ModelAdmin):
    list_display = ( 'design_product_title', 'design_product_desc', 'design_product_img','design_external_link')

class WhyweAdmin(admin.ModelAdmin):
    list_display = ( 'why_title', 'why_desc')

class VisitingcardAdmin(admin.ModelAdmin):
    list_display = ( 'front_img', 'back_img')


admin.site.register(Service, ServiceAdmin)
admin.site.register(Indexbanner, IndexbannerAdmin)
admin.site.register(Maplocation, MaplocationAdmin)
admin.site.register(Footer, FooterAdmin)
admin.site.register(Header, HeaderAdmin)
admin.site.register(IndexProducts, IndexProductsAdmin)
admin.site.register(ProductsCategory, ProductsCategoryAdmin)
admin.site.register(ProductsArchitecture, ProductsArchitectureAdmin)
admin.site.register(ProductsDesign, ProductsDesignAdmin)
admin.site.register(ProductsGame, ProductsGameAdmin)
admin.site.register(Whywe, WhyweAdmin)
admin.site.register(Visitingcard, VisitingcardAdmin)
admin.site.register(ServicesCategory, ServicesCategoryAdmin)
