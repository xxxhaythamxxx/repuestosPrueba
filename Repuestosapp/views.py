from django.shortcuts import render, HttpResponse
from .forms import Formulario, listCars
from .models import car, spare, engine
from django.core.paginator import Paginator

def same(): # Creo el diccionario para los formularios en común de todos los templates
    formulario_busqueda=Formulario()
    allEngines=engine.objects.all()# Consigo TODOS los motores
    onlyManufCars=car.objects.all().values("car_manufacturer").distinct()# Conseguir TODOS los carros por fabricante
    allCars=car.objects.all()# Conseguir TODOS los carros
    dicc={"formulariop":formulario_busqueda,"allCars":allCars,"onlyManufCars":onlyManufCars,"allEngines":allEngines}
    return dicc

dic=same().copy()

def pag(request,obj,num,htmlid,att,v):    # Creo la paginación de todas las plantillas
    paginator = Paginator(obj, num) # Show 25 contacts per page.
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    obj = paginator.get_page(page)
    dic.update({htmlid:obj,att:v})
    return dic


def selectf(request):   # Código para saber si usa el input o el filtro
    search=request.GET.get("engine_id")
    if search:    # Si usaron el filter
        engModel=request.GET.get("engine_id")       # Valor del modelo del motor
        carManu=request.GET.get("car_id")           # Valor del carro enviado
        carModel=request.GET.get("car_model_id")    #Valor del modelo del carro enviado
        comp=spare.objects.filter(engine_info__engine_ide__icontains=engModel,car_info__car_manufacturer__icontains=carManu,car_info__car_model__icontains=carModel).order_by("id")  # Creo un Query de spare que tenga el valor del motor pasado
        return render(request,"Repuestosapp/findfil.html",pag(request,comp,10,"spare","mig",engModel))
    else:   # Si se usa el buscador por código de repuesto
        valor=request.GET.get("search")
        if valor:
            comp=spare.objects.filter(spare_code__icontains=valor).order_by("id") # Compara el codigoRepuesto con valor
            return render(request,"Repuestosapp/find.html",pag(request,comp,10,"spare","mig",valor))
        else:
            return False

def prueba(request):
    all=spare.objects.all().order_by("id")
    paginator = Paginator(all, 2) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    all = paginator.get_page(page_number)
    return render(request,"Repuestosapp/prueba.html",{"all":all})


def home(request):

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
        return render(request,"Repuestosapp/brand.html",pag(request,pr,10,"brand_id","mig",val))
    else:
        return selectf(request)

def name(request,val):

    if selectf(request)==False:
        pr=spare.objects.values("spare_photo","spare_code","spare_brand","spare_name","car_info__car_manufacturer").filter(spare_name__icontains=val).distinct()
        return render(request,"Repuestosapp/name.html",pag(request,pr,10,"brand_id","mig",val))
    else:
        return selectf(request)
    
def manuf(request,val):

    if selectf(request)==False:
        pr=car.objects.filter(car_manufacturer__icontains=val)
        return render(request,"Repuestosapp/manuf.html",pag(request,pr,10,"brand_id","mig",val))
    else:
        return selectf(request)
    
def model(request,val):

    if selectf(request)==False:
        pr=engine.objects.filter(car_engine_info__car_model__icontains=val)
        return render(request,"Repuestosapp/model.html",pag(request,pr,10,"brand_id","mig",val))
    else:
        return selectf(request)
    
def enginei(request,val):

    if selectf(request)==False:
        pr=spare.objects.filter(engine_info__engine_ide__icontains=val)
        dic.update({"test":val})
        return render(request,"Repuestosapp/engine.html",pag(request,pr,10,"brand_id","mig",val))
    else:
        return selectf(request)

def sparedetails(request,val):

    if selectf(request)==False:
        pr=spare.objects.filter(spare_code__icontains=val)
        dic.update({"test":val})
        return render(request,"Repuestosapp/sparedetails.html",pag(request,pr,10,"brand_id","mig",val))
    else:
        return selectf(request)
        