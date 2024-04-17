# services/context_processors.py
from service.models import Footer, Header

def header_and_footer(request):
    headerData = Header.objects.all()  # Replace with your actual query
    footerData = Footer.objects.all()    # Replace with your actual query

    return {'headerData': headerData, 'footerData': footerData}
