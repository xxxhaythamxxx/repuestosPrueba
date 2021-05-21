from django.shortcuts import render, HttpResponse
from .forms import Formulario, listCars
from .models import car, spare, engine
from django.core.paginator import Paginator
from .filters import spareFilter
from io import BytesIO
from django.http import HttpResponse
from django.views import View
from xhtml2pdf import pisa
from django.template.loader import get_template
from weasyprint import HTML, CSS
import os
from django.conf import settings
from django.contrib.staticfiles import finders

def same(): # Creo el diccionario para los formularios en común de todos los templates
    formulario_busqueda=Formulario()
    allEngines=engine.objects.all()# Consigo TODOS los motores
    onlyManufCars=car.objects.all().values("car_manufacturer").distinct()# Conseguir TODOS los carros por fabricante
    allCars=car.objects.all()# Conseguir TODOS los carros
    dicc={"formulariop":formulario_busqueda,"allCars":allCars,"onlyManufCars":onlyManufCars,"allEngines":allEngines}
    return dicc

dic=same().copy()

def selectf(request):   # Código para saber si usa el input o el filtro
    if request.method=="GET":
        search=request.GET.get("engine_id")
        if search:    # Si usaron el filter
            engModel=request.GET.get("engine_id")       # Valor del modelo del motor
            carManu=request.GET.get("car_id")           # Valor del carro enviado
            carModel=request.GET.get("car_model_id")    #Valor del modelo del carro enviado
            comp=spare.objects.filter(engine_info__engine_ide__icontains=engModel,car_info__car_manufacturer__icontains=carManu,car_info__car_model__icontains=carModel).order_by("id")  # Creo un Query de spare que tenga el valor del motor pasado
            dic.update({"spare":comp,"mig":engModel})
            return render(request,"Repuestosapp/findfil.html",dic)
        else:   # Si se usa el buscador por código de repuesto
            valor=request.GET.get("search")
            if valor:
                comp=spare.objects.filter(spare_code__icontains=valor).order_by("id") # Compara el codigoRepuesto con valor
                dic.update({"spare":comp,"mig":valor})
                return render(request,"Repuestosapp/find.html",dic)
            else:
                return False

def prueba(request):
    return render(request,"Repuestosapp/prueba.html",{"name":"LuisPapito"})
    # name=request.GET.get("view")
    # print=request.GET.get("print")
    # if name:
    #     return verPDF(request,"Repuestosapp/prueba.html",{"name":"SuperLuis"})
    # else:
    #     if print:
    #         return imprimirPDF(request,"Repuestosapp/prueba.html",{"name":"SuperLuis"})
    #     else:
    #         return render(request,"Repuestosapp/prueba.html")
    # comp=spare.objects.all().order_by("id")
    # filter=spareFilter(request.GET,queryset=comp)
    

def home(request):

    if request.method=="GET":
        print("Entra a home")

        if selectf(request)==False:
            return render(request,"Repuestosapp/home.html",same())
        else:
            return selectf(request)

def find(request):
    print("Entra a find")

def findfil(request):
    print("Entra a findfil")
    
def brand(request,val):

    if selectf(request)==False:
        pr=spare.objects.values("spare_photo","spare_code","spare_brand","spare_name","car_info__car_manufacturer").filter(spare_brand__icontains=val).distinct()
        dic.update({"brand_id":pr,"mig":val})
        return render(request,"Repuestosapp/brand.html",dic)
    else:
        return selectf(request)

def name(request,val):

    if selectf(request)==False:
        pr=spare.objects.values("spare_photo","spare_code","spare_brand","spare_name","car_info__car_manufacturer").filter(spare_name__icontains=val).distinct()
        dic.update({"brand_id":pr,"mig":val})
        return render(request,"Repuestosapp/name.html",dic)
    else:
        return selectf(request)
    
def manuf(request,val):

    if selectf(request)==False:
        pr=car.objects.filter(car_manufacturer__icontains=val)
        dic.update({"brand_id":pr,"mig":val})
        return render(request,"Repuestosapp/manuf.html",dic)
    else:
        return selectf(request)
    
def model(request,val):

    if selectf(request)==False:
        pr=engine.objects.filter(car_engine_info__car_model__icontains=val)
        dic.update({"brand_id":pr,"mig":val})
        return render(request,"Repuestosapp/model.html",dic)
    else:
        return selectf(request)
    
def enginei(request,val):

    if selectf(request)==False:
        pr=spare.objects.filter(engine_info__engine_ide__icontains=val)
        dic.update({"brand_id":pr,"test":val,"mig":val})
        return render(request,"Repuestosapp/engine.html",dic)
    else:
        return selectf(request)

def sparedetails(request,val):

    if selectf(request)==False:
        pr=spare.objects.filter(spare_code__icontains=val)
        dic.update({"brand_id":pr,"test":val,"mig":val})
        return render(request,"Repuestosapp/sparedetails.html",dic)
    else:
        return selectf(request)
        