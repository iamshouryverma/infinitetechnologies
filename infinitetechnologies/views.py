from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail
from datetime import datetime
from service.models import Service, Footer, Maplocation, Indexbanner, Header, IndexProducts, Whywe, Visitingcard, ProductsArchitecture, ProductsCategory, ProductsGame, ProductsDesign, ServicesCategory
from django.core.paginator import Paginator


def home(request):
    whyData=Whywe.objects.all()
    indexproductData=IndexProducts.objects.all()
    indexbannerData=Indexbanner.objects.all()
    serviceData = Service.objects.all()
    data={
        'serviceData':serviceData,
        'indexbannerData':indexbannerData,
        'indexproductData':indexproductData,
        'whyData':whyData
    }
    return render(request,"index.html",data)




def about_us(request):
    current_year = datetime.now().year
    return render(request, "about.html", {'current_year': current_year})

def contact(request):
    visitingcardData = Visitingcard.objects.all()
    headerData = Header.objects.all()  # Replace with your actual query
    footerData = Footer.objects.all()
    current_year = datetime.now().year
    maplocationData=Maplocation.objects.all()
    data={
        'maplocationData':maplocationData,
        'current_year':current_year,
        'footerData': footerData,
        'headerData': headerData,
        'visitingcardData':visitingcardData,
        }
    return render(request,"contact.html", data)

def productsarchitecture(request):
    architectureproductcategoryData=ProductsArchitecture.objects.all()
    data={
        'architectureproductcategoryData':architectureproductcategoryData,
        }
    return render(request,"products_architecture.html",data)

def products(request):
    productcategoryData=ProductsCategory.objects.all()
    data={
        'productcategoryData':productcategoryData,
        }
    return render(request,"products.html",data)

def productsgame(request):
    gameproductcategoryData=ProductsGame.objects.all()
    data={
        'gameproductcategoryData':gameproductcategoryData,
        }
    return render(request,"products_game.html",data)

def productsdesign(request):
    designproductcategoryData=ProductsDesign.objects.all()
    data={
        'designproductcategoryData':designproductcategoryData,
        }
    return render(request,"products_design.html",data)

def itservices(request):
    itservicecategoryData=ServicesCategory.objects.all()
    data={
        'itservicecategoryData':itservicecategoryData,
        }
    return render(request,"itservices.html",data)

def thankyou(request):
    try:
        if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            phone= request.POST['phone']
            message = request.POST['reason']
            subject = name+' wants to reach out to you through your website.'
            email_message = f'Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}'
            from_email = 'websiteinfinite3d@gmail.com'  # Your email address
            recipient_list = ['infinite3dbyitl@gmail.com']  # List of email recipients

            send_mail(subject, email_message, from_email, recipient_list)
            return render(request,"thankyou.html",{'data':name})
    except:
        pass