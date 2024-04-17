"""
URL configuration for infinitetechnologies project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from infinitetechnologies import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products_architecture/', views.productsarchitecture, name='our_architecture_product'),
    path('products_game/', views.productsgame, name='our_game_product'),
    path('products_design/', views.productsdesign, name='our_design_product'),
    path('products/', views.products, name='our_product'),
    path('itservices/', views.itservices, name='it_services'),
    path('about-us/', views.about_us, name='about_us'),
    path('contact/',views.contact, name='contact_us'),
    path('thankyou/', views.thankyou, name='thankyou'),
    path('',views.home),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)