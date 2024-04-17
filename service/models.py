from django.db import models

class Service(models.Model):
    service_title = models.CharField(max_length=50)
    service_desc = models.TextField()

class Indexbanner(models.Model):
    banner_img = models.FileField(upload_to="index_banner/", max_length=5000, null=True, default=None)

class Maplocation(models.Model):
    map_location = models.TextField()

class Footer(models.Model):
    address = models.TextField()
    copyright = models.TextField()

class Header(models.Model):
    navbar_link = models.TextField()
    navbar_content = models.TextField()
    navbar_icon = models.FileField(upload_to="img/", max_length=5000, null=True, default=None)

class IndexProducts(models.Model):
    index_product_title = models.TextField()
    index_external_link = models.TextField(null=True,blank=True)
    index_product_img = models.FileField(upload_to="productimg/", max_length=5000, null=True, default=None)

class ProductsCategory(models.Model):
    product_category_title = models.TextField()
    product_category_desc = models.TextField()
    external_category_link = models.TextField(null=True,blank=True)
    product_category_img = models.FileField(upload_to="productimg/", max_length=5000, null=True, default=None)

class ServicesCategory(models.Model):
    services_category_title = models.TextField()
    services_category_desc = models.TextField()
    services_category_img = models.FileField(upload_to="productimg/", max_length=5000, null=True, default=None)


class ProductsArchitecture(models.Model):
    architecture_product_title = models.TextField()
    architecture_product_desc = models.TextField()
    architecture_external_link = models.TextField(null=True,blank=True)
    architecture_product_img = models.FileField(upload_to="productimg/", max_length=5000, null=True, default=None)

class ProductsGame(models.Model):
    game_product_title = models.TextField()
    game_product_desc = models.TextField()
    game_external_link = models.TextField(null=True,blank=True)
    game_product_img = models.FileField(upload_to="productimg/", max_length=5000, null=True, default=None)


class ProductsDesign(models.Model):
    design_product_title = models.TextField()
    design_product_desc = models.TextField()
    design_external_link = models.TextField(null=True,blank=True)
    design_product_img = models.FileField(upload_to="productimg/", max_length=5000, null=True, default=None)


class Whywe(models.Model):
    why_title = models.TextField()
    why_desc = models.TextField()

class Visitingcard(models.Model):
    front_img = models.FileField(upload_to="img/", max_length=5000, null=True, default=None)
    back_img = models.FileField(upload_to="img/", max_length=5000, null=True, default=None)