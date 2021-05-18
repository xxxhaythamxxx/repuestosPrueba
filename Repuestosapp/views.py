from django.shortcuts import render, HttpResponse
from .forms import Formulario, listCars
from .models import car, spare, engine

def same():
    formulario_busqueda=Formulario()
    allEngines=engine.objects.all()# Consigo TODOS los motores
    onlyManufCars=car.objects.all().values("car_manufacturer").distinct()# Conseguir TODOS los carros por fabricante
    allCars=car.objects.all()# Conseguir TODOS los carros
    dicc={"formulariop":formulario_busqueda,"allCars":allCars,"onlyManufCars":onlyManufCars,"allEngines":allEngines}
    return dicc

dic=same().copy()

def selectf(request):
    search=request.GET.get("engine_id")
    if search:    # Si usaron el filter
        engModel=request.GET.get("engine_id")   # Valor del modelo del motor
        comp=spare.objects.filter(engine_info__engine_ide__icontains=engModel)  # Creo un Query de spare que tenga el valor del motor pasado
        dic.update({"spare":comp})
        return render(request,"Repuestosapp/find.html",dic)
    else:   # Si se usa el buscador por código de repuesto
        valor=request.GET.get("search")
        if valor:
            print("Entra en input")
            print(valor)
            comp=spare.objects.filter(spare_code__icontains=valor) # Compara el codigoRepuesto con valor
            dic.update({"spare":comp})
            print(dic)
            return render(request,"Repuestosapp/find.html",dic)
        else:
            return False

def home(request):

    if selectf(request)==False:
        return render(request,"Repuestosapp/home.html",same())
    else:
        return selectf(request)

def find(request):
    print("Entra a find")
    
def brand(request,val):

    if selectf(request)==False:
        pr=spare.objects.values("spare_photo","spare_code","spare_brand","spare_name","car_info__car_manufacturer").filter(spare_brand__icontains=val).distinct()
        dic.update({"brand_id":pr})
        return render(request,"Repuestosapp/brand.html",dic)
    else:
        return selectf(request)

def name(request,val):

    if selectf(request)==False:
        pr=spare.objects.values("spare_photo","spare_code","spare_brand","spare_name","car_info__car_manufacturer").filter(spare_name__icontains=val).distinct()
        dic.update({"brand_id":pr})
        return render(request,"Repuestosapp/name.html",dic)
    else:
        return selectf(request)
    
def manuf(request,val):

    if selectf(request)==False:
        pr=car.objects.filter(car_manufacturer__icontains=val)
        dic.update({"brand_id":pr})
        return render(request,"Repuestosapp/manuf.html",dic)
    else:
        return selectf(request)
    
def model(request,val):

    if selectf(request)==False:
        pr=engine.objects.filter(car_engine_info__car_model__icontains=val)
        dic.update({"brand_id":pr})
        return render(request,"Repuestosapp/model.html",dic)
    else:
        return selectf(request)
    
def enginei(request,val):

    if selectf(request)==False:
        pr=spare.objects.filter(engine_info__engine_ide__icontains=val)
        dic.update({"brand_id":pr,"test":val})
        return render(request,"Repuestosapp/engine.html",dic)
    else:
        return selectf(request)

def sparedetails(request,val):

    if selectf(request)==False:
        pr=spare.objects.filter(spare_code__icontains=val)
        dic.update({"brand_id":pr,"test":val})
        return render(request,"Repuestosapp/sparedetails.html",dic)
    else:
        return selectf(request)
        