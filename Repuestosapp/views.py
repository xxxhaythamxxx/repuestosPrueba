from django.shortcuts import get_object_or_404, redirect, render, HttpResponse, HttpResponseRedirect
from .forms import Formulario, listCars
from .models import car, spare, engine
from django.core.paginator import Paginator
from io import BytesIO
from django.http import HttpResponse
from django.views import View
from django.template.loader import get_template
import os
from django.conf import settings
from django.contrib.staticfiles import finders
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .cart import *

def add2car(request,spare_id):

    if request.method=="POST":
        print("Está enviando POST-----------------------------------")
        list = request.POST.getlist('toAdd')
        print(list)
        # return render(request,"Repuestosapp/detail.html")

        carrito = Cart(request)
        spare_part = get_object_or_404(spare, id = spare_id)
        carrito.add(spare_part)
        # return redirect("home")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def er2car(request, spare_id):
    carrito = Cart(request)
    spare_part = get_object_or_404(spare, id = spare_id)
    carrito.remove(spare_part)
    # return render(request,"Repuestosapp/detail.html",{"carrito":carrito,"spare":spare_part})
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def detail(request):

    if selectf(request)==False:
        spares = spare.objects.all()
        carrito = Cart(request)
        dic.update({'carrito': carrito,'spare':spares})
        return render(request, 'Repuestosapp/detail.html', dic)
    else:
        return selectf(request)

def acceder(request):
    if request.method=="POST":
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            usuario = authenticate(username=nombre_usuario,password=password)
            if usuario is not None:
                login(request,usuario)
                messages.success(request,F"Bienvenid@ de nuevo {nombre_usuario}")
                return redirect("home")
            else:
                messages.error(request,"Los datos son incorrectos")
        else:    
            messages.error(request,"Los datos son incorrectos")

    form = AuthenticationForm()
    return render(request,"Repuestosapp/acceder.html",{"form":form})

class VistaRegistro(View):
    def get(self,request):
        form = UserCreationForm()
        return render(request,"Repuestosapp/registro.html",{"form":form})

    def post(self,request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            nombre_usuario = form.cleaned_data.get("username")
            messages.success(request,F"Bienvenid@ a la plataforma {nombre_usuario}")
            login(request,usuario)
            return redirect("home")
        else:
            for msg in form.error_messages:
                messages.error(request,form.error_messages[msg])
            return render(request,"Repuestosapp/registro.html",{"form":form})

def salir(request):
    logout(request)
    messages.success(request,F"Tu sesión se ha cerrado correctamente")
    return redirect("home")

def same(): # Creo el diccionario para los formularios en común de todos los templates
    formulario_busqueda=Formulario()
    allEngines=engine.objects.all()# Consigo TODOS los motores
    onlyManufCars=car.objects.all().values("car_manufacturer").distinct()# Conseguir TODOS los carros por fabricante
    allCars=car.objects.all()# Conseguir TODOS los carros
    allSpares=spare.objects.values("spare_name").order_by("spare_name").distinct()# Conseguir TODOS los repuestos
    dicc={"formulariop":formulario_busqueda,"allCars":allCars,"onlyManufCars":onlyManufCars,"allEngines":allEngines,"allSpares":allSpares}
    return dicc

dic=same().copy()

def trunc(val):
    allen = car.objects.filter(car_manufacturer__icontains=val).values("car_model").order_by("car_model")
    b=[]
    for a in allen:
        a = a["car_model"].split(" ")[0]
        b.append(a+" .")
    b = list(set(b)) 
    return b

def selectf(request):   # Código para saber si usa el input o el filtro

    if request.method=="POST":
        list = request.POST.getlist('toAdd')
        delist = request.POST.getlist("toDel")
        if delist:
            carrito = Cart(request)
            for a in delist:                
                spare_part = get_object_or_404(spare, id = a)
                carrito.remove(spare_part)
            # return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        if list:
            carrito = Cart(request)
            for a in list:                
                spare_part = get_object_or_404(spare, id = a)
                carrito.add(spare_part)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        # return render(request,"Repuestosapp/detail.html")

    if request.method=="GET":
        search=request.GET.get("engine_id")
        if search:    # Si usaron el filter
            engModel=request.GET.get("engine_id")       # Valor del modelo del motor
            carManu=request.GET.get("car_id")           # Valor del carro enviado
            carModel=request.GET.get("car_model_id")    #Valor del modelo del carro enviado
            comp=spare.objects.filter(engine_info__engine_ide__icontains=engModel,car_info__car_manufacturer__icontains=carManu,car_info__car_model__icontains=carModel).order_by("id")  # Creo un Query de spare que tenga el valor del motor pasado
            engcomp=engine.objects.filter(engine_ide__icontains=engModel,car_engine_info__car_manufacturer__icontains=carManu)
            dic.update({"spare":comp,"mig":engModel,"engcomp":engcomp})
            return render(request,"Repuestosapp/findfil.html",dic)
        else:   # Si se usa el buscador por código de repuesto
            valor=request.GET.get("search")
            if valor:
                comp=spare.objects.filter(spare_code__icontains=valor).order_by("id") # Compara el codigoRepuesto con valor
                dic.update({"spare":comp,"mig":valor})
                return render(request,"Repuestosapp/find.html",dic)
            else:
                return False
# def prueba1(request,val):
#     val1=request.GET.get("val1")
#     return (request,"Repuestosapp/prueba1.html")

def prueba1(request):
    if request.method=="GET":
        val=request.GET.get("val1")
        return (request,"Repuestosapp/prueba1.html")

def prueba(request):
    if request.method=="GET":
        val=request.GET.get("val1")
        if val:
            print(val)
            return render(request,"Repuestosapp/prueba1.html")
        else:
            return render(request,"Repuestosapp/prueba.html")
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
    

def home(request):

    if request.method=="POST":
        list = request.POST.getlist('toAdd')
        delist = request.POST.getlist("toDel")
        if delist:
            carrito = Cart(request)
            for a in delist:                
                spare_part = get_object_or_404(spare, id = a)
                carrito.remove(spare_part)
            # return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        if list:
            carrito = Cart(request)
            for a in list:                
                spare_part = get_object_or_404(spare, id = a)
                carrito.add(spare_part)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

    if request.method=="GET":

        if selectf(request)==False:
            b = []
            a = car.objects.all().values("car_manufacturer").order_by("car_manufacturer")
            for v in a:
                v = v["car_manufacturer"]
                b.append(v)
            b = (set(b))
            dic.update({"manu":b})
            return render(request,"Repuestosapp/home.html",dic)
        else:
            return selectf(request)

def find(request):
    print("Entra a find")

def findfil(request):
    print("Entra a findfil")
    
def brand(request,val):

    if selectf(request)==False:
        pr=spare.objects.values("id","spare_photo","spare_code","spare_brand","spare_name","car_info__car_manufacturer").filter(spare_brand__icontains=val).distinct()
        dic.update({"brand_id":pr,"mig":val})
        return render(request,"Repuestosapp/brand.html",dic)
    else:
        return selectf(request)

def name(request,val):

    if selectf(request)==False:
        pr=spare.objects.values("id","spare_photo","spare_code","spare_brand","spare_name","car_info__car_manufacturer").filter(spare_name__icontains=val).distinct()
        dic.update({"brand_id":pr,"mig":val})
        return render(request,"Repuestosapp/name.html",dic)
    else:
        return selectf(request)
    
def manuf(request,val):

    if selectf(request)==False:
        tr = trunc(val)
        pr=car.objects.filter(car_manufacturer__icontains=val)
        dic.update({"brand_id":pr,"mig":val,"tr":tr})
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
        dic.update({"brand_id":pr})
        return render(request,"Repuestosapp/sparedetails.html",dic)
    else:
        return selectf(request)
        