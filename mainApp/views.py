from django.shortcuts import render
from django.http import HttpResponse 
from .models import iletisim, yazilar
def index(request):
    htmlFilePath = "index.html"
    return render(request, htmlFilePath)

def hakkimda(request):
    htmlFilePath = "about.html"
    return render(request, htmlFilePath)

def iletisimm(request):
    htmlFilePath = "iletisim.html"
    if request.method == "POST" and request.POST['name'] != "" and request.POST['mail'] != "" and request.POST['message'] != "":
        name = request.POST['name']
        mail = request.POST['mail']
        message = request.POST['message']
        
        model = iletisim(name=name, mail=mail, message=message)
        model.save()
    return render(request, htmlFilePath)


def yazilarr(request):
    htmlFilePath = "blog.html"
    
    model1 = yazilar.objects.values()
    #model11 = model1.get(yaziBenzersizId=100)
    
    
    context = {
        "yazi":model1
    }
    
    return render(request, htmlFilePath, context)

def yazi1(request):
    htmlFilePath = "yazilar/yazi1.html"
    
    #model1 = yazilar.objects.values().all()
    
    #print(model1[0])
    model1 = yazilar.objects
    model1 = model1.get(yaziBenzersizId=100)
    yazi1_firsletter = model1.yazi1[0]
    
    context = {
        'yazi': model1, "yazi_first": yazi1_firsletter
        
    }
    return render(request, htmlFilePath, context)

def yazi2(request):
    htmlFilePath = "yazilar/yazi2.html"
    
    model1 = yazilar.objects
    model1 = model1.get(yaziBenzersizId=101)
    yazi1_firsletter = model1.yazi1[0]
    
    
    context = {
        "yazi": model1, "yazi_first": yazi1_firsletter
    }
    
    return render(request, htmlFilePath, context)


def yazi3(request):
    htmlFilePath = "yazilar/yazi3.html"
    
    model1 = yazilar.objects
    model1 = model1.get(yaziBenzersizId=102)
    yazi1_firsletter = model1.yazi1[0]
    context = {
        'yazi': model1, "yazi_first": yazi1_firsletter
    }
    
    return render(request, htmlFilePath, context)


def yazi4(request):
    htmlFilePath = "yazilar/yazi4.html"
    
    model1 = yazilar.objects 
    model1 = model1.get(yaziBenzersizId=103)
    yazi1_firsletter = model1.yazi1[0]
    context = {
        'yazi': model1, "yazi_first": yazi1_firsletter
    }
    
    return render(request, htmlFilePath, context)


def yazi5(request):
    htmlFilePath = "yazilar/yazi5.html"
    
    model1 = yazilar.objects 
    model1 = model1.get(yaziBenzersizId=104)
    yazi1_firsletter = model1.yazi1[0]
    context = {
        'yazi': model1, "yazi_first": yazi1_firsletter
    }
    
    return render(request, htmlFilePath, context)