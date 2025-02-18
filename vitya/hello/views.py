from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')


'''
def contact(request):
    #CN = request.META['CONTENT_LENGTH']
    CT = request.META['CONTENT_TYPE']
    HA = request.META['HTTP_ACCEPT']
    HAE = request.META['HTTP_ACCEPT_ENCODING']
    HAL = request.META['HTTP_ACCEPT_LANGUAGE']
    HH = request.META['HTTP_HOST']
    #HR = request.META['HTTP_REFERER']
    HUA = request.META['HTTP_USER_AGENT']
    #QS = request.META['QUERY_STRING']
    RA = request.META['REMOTE_ADDR']
    #RH = request.META['REMOTE_HOST']
    #RU = request.META['REMOTE_USER']
    #RM = request.META['REQUEST_METHOD']
    #SN = request.META['SERVER_NAME']
    #SP = request.META['SERVER_POST']

    return HttpResponse(f"""
        <p>content_type: {CT}\</p>
        <p>http_accept: {HA}</p>
        <p>http_accept_encoding: {HAE}</p>
        <p>http_accept_language: {HAL}</p>
        <p>http_host: {HH}</p>
        <p>http_user_agent: {HUA}</p>
        <p>remote_addr: {RA}</p>
    """)
'''