from django.shortcuts import render, HttpResponse
from .forms import Formulario, listCars
from .models import car, spare, engine

def home(request):
    # if request.method=="GET":                   # Si recibe un GET desde la pagina
    formulario_busqueda=Formulario()
    allEngines=engine.objects.all()# Consigo TODOS los motores
    onlyManufCars=car.objects.all().values("car_manufacturer").distinct()# Conseguir TODOS los carros por fabricante
    allCars=car.objects.all()# Conseguir TODOS los carros

    comp=spare.objects.none()
    if request.GET.get("engine_id"):    # Si usaron el filter
            engModel=request.GET.get("engine_id")   # Valor del modelo del motor
            comp=spare.objects.filter(engine_info__engine_ide__icontains=engModel)  # Creo un Query de spare que tenga el valor del motor pasado
            return render(request,"Repuestosapp/find.html",{"formulariop":formulario_busqueda,"allCars":allCars,"onlyManufCars":onlyManufCars,"allEngines":allEngines,"spare":comp})
    else:   # Si se usa el buscador por código de repuesto
        if request.GET.get("search"):
            valor=request.GET.get("search")
            comp=spare.objects.filter(spare_code__icontains=valor) # Compara el codigoRepuesto con valor
            return render(request,"Repuestosapp/find.html",{"formulariop":formulario_busqueda,"allCars":allCars,"onlyManufCars":onlyManufCars,"allEngines":allEngines,"spare":comp})
        else:
            return render(request,"Repuestosapp/home.html",{"formulariop":formulario_busqueda,"allCars":allCars,"onlyManufCars":onlyManufCars,"allEngines":allEngines})

def find(request):
    if request.method=="GET":                   # Si recibe un GET desde la pagina
        formulario_busqueda=Formulario()
        allEngines=engine.objects.all()# Consigo TODOS los motores
        onlyManufCars=car.objects.all().values("car_manufacturer").distinct()# Conseguir TODOS los carros por fabricante
        allCars=car.objects.all()# Conseguir TODOS los carros
        comp=spare.objects.none()
        # if formulario_busqueda.is_valid():      # Si rellenan el formulario correctamente
        valor=request.GET.get("search")     # Guardo la busqueda
        if request.GET.get("engine_id"):    # Si usaron el filter
            engModel=request.GET.get("engine_id")   # Valor del modelo del motor
            comp=spare.objects.filter(engine_info__engine_ide__icontains=engModel)  # Creo un Query de spare que tenga el valor del motor pasado
        else:   # Si se usa el buscador por código de repuesto
            if valor:
                comp=spare.objects.filter(spare_code__icontains=valor) # Compara el codigoRepuesto con valor
        
        return render(request,"Repuestosapp/find.html",{"formulariop":formulario_busqueda,"spare":comp,"allCars":allCars,"onlyManufCars":onlyManufCars,"allEngines":allEngines})
    

def brand(request,val):

    formulario_busqueda=Formulario()
    allEngines=engine.objects.all()# Consigo TODOS los motores
    onlyManufCars=car.objects.all().values("car_manufacturer").distinct()# Conseguir TODOS los carros por fabricante
    allCars=car.objects.all()# Conseguir TODOS los carros
    comp=spare.objects.none()
    if request.GET.get("engine_id"):    # Si usaron el filter
            engModel=request.GET.get("engine_id")   # Valor del modelo del motor
            comp=spare.objects.filter(engine_info__engine_ide__icontains=engModel)  # Creo un Query de spare que tenga el valor del motor pasado
            return render(request,"Repuestosapp/find.html",{"formulariop":formulario_busqueda,"allCars":allCars,"onlyManufCars":onlyManufCars,"allEngines":allEngines,"spare":comp})
    else:   # Si se usa el buscador por código de repuesto
        if request.GET.get("search"):
            valor=request.GET.get("search")
            comp=spare.objects.filter(spare_code__icontains=valor) # Compara el codigoRepuesto con valor
            return render(request,"Repuestosapp/find.html",{"formulariop":formulario_busqueda,"allCars":allCars,"onlyManufCars":onlyManufCars,"allEngines":allEngines,"spare":comp})
        else:
            test=val
            pr=spare.objects.values("spare_photo","spare_code","spare_brand","spare_name","car_info__car_manufacturer").filter(spare_brand__icontains=test).distinct()
            return render(request,"Repuestosapp/brand.html",{"brand_id":pr,"formulariop":formulario_busqueda,"allCars":allCars,"onlyManufCars":onlyManufCars,"allEngines":allEngines})
    

def name(request,val):

    formulario_busqueda=Formulario()
    allEngines=engine.objects.all()# Consigo TODOS los motores
    onlyManufCars=car.objects.all().values("car_manufacturer").distinct()# Conseguir TODOS los carros por fabricante
    allCars=car.objects.all()# Conseguir TODOS los carros
    comp=spare.objects.none()
    if request.GET.get("engine_id"):    # Si usaron el filter
            engModel=request.GET.get("engine_id")   # Valor del modelo del motor
            comp=spare.objects.filter(engine_info__engine_ide__icontains=engModel)  # Creo un Query de spare que tenga el valor del motor pasado
            return render(request,"Repuestosapp/find.html",{"formulariop":formulario_busqueda,"allCars":allCars,"onlyManufCars":onlyManufCars,"allEngines":allEngines,"spare":comp})
    else:   # Si se usa el buscador por código de repuesto
        if request.GET.get("search"):
            valor=request.GET.get("search")
            comp=spare.objects.filter(spare_code__icontains=valor) # Compara el codigoRepuesto con valor
            return render(request,"Repuestosapp/find.html",{"formulariop":formulario_busqueda,"allCars":allCars,"onlyManufCars":onlyManufCars,"allEngines":allEngines,"spare":comp})
        else:
            test=val
            pr=spare.objects.values("spare_photo","spare_code","spare_brand","spare_name","car_info__car_manufacturer").filter(spare_name__icontains=test).distinct()
            return render(request,"Repuestosapp/name.html",{"brand_id":pr,"formulariop":formulario_busqueda,"allCars":allCars,"onlyManufCars":onlyManufCars,"allEngines":allEngines})
    
def manuf(request,val):

    formulario_busqueda=Formulario()
    allEngines=engine.objects.all()# Consigo TODOS los motores
    onlyManufCars=car.objects.all().values("car_manufacturer").distinct()# Conseguir TODOS los carros por fabricante
    allCars=car.objects.all()# Conseguir TODOS los carros
    comp=spare.objects.none()
    if request.GET.get("engine_id"):    # Si usaron el filter
            engModel=request.GET.get("engine_id")   # Valor del modelo del motor
            comp=spare.objects.filter(engine_info__engine_ide__icontains=engModel)  # Creo un Query de spare que tenga el valor del motor pasado
            return render(request,"Repuestosapp/find.html",{"formulariop":formulario_busqueda,"allCars":allCars,"onlyManufCars":onlyManufCars,"allEngines":allEngines,"spare":comp})
    else:   # Si se usa el buscador por código de repuesto
        if request.GET.get("search"):
            valor=request.GET.get("search")
            comp=spare.objects.filter(spare_code__icontains=valor) # Compara el codigoRepuesto con valor
            return render(request,"Repuestosapp/find.html",{"formulariop":formulario_busqueda,"allCars":allCars,"onlyManufCars":onlyManufCars,"allEngines":allEngines,"spare":comp})
        else:
            test=val
            pr=car.objects.filter(car_manufacturer__icontains=test)
            return render(request,"Repuestosapp/manuf.html",{"brand_id":pr,"formulariop":formulario_busqueda,"allCars":allCars,"onlyManufCars":onlyManufCars,"allEngines":allEngines})
    
def model(request,val):

    formulario_busqueda=Formulario()
    allEngines=engine.objects.all()# Consigo TODOS los motores
    onlyManufCars=car.objects.all().values("car_manufacturer").distinct()# Conseguir TODOS los carros por fabricante
    allCars=car.objects.all()# Conseguir TODOS los carros
    comp=spare.objects.none()
    if request.GET.get("engine_id"):    # Si usaron el filter
            engModel=request.GET.get("engine_id")   # Valor del modelo del motor
            comp=spare.objects.filter(engine_info__engine_ide__icontains=engModel)  # Creo un Query de spare que tenga el valor del motor pasado
            return render(request,"Repuestosapp/find.html",{"formulariop":formulario_busqueda,"allCars":allCars,"onlyManufCars":onlyManufCars,"allEngines":allEngines,"spare":comp})
    else:   # Si se usa el buscador por código de repuesto
        if request.GET.get("search"):
            valor=request.GET.get("search")
            comp=spare.objects.filter(spare_code__icontains=valor) # Compara el codigoRepuesto con valor
            return render(request,"Repuestosapp/find.html",{"formulariop":formulario_busqueda,"allCars":allCars,"onlyManufCars":onlyManufCars,"allEngines":allEngines,"spare":comp})
        else:
            test=val
            pr=engine.objects.filter(car_engine_info__car_model__icontains=test)
            return render(request,"Repuestosapp/model.html",{"brand_id":pr,"formulariop":formulario_busqueda,"allCars":allCars,"onlyManufCars":onlyManufCars,"allEngines":allEngines})
    
def enginei(request,val):

    formulario_busqueda=Formulario()
    allEngines=engine.objects.all()# Consigo TODOS los motores
    onlyManufCars=car.objects.all().values("car_manufacturer").distinct()# Conseguir TODOS los carros por fabricante
    allCars=car.objects.all()# Conseguir TODOS los carros
    comp=spare.objects.none()
    if request.GET.get("engine_id"):    # Si usaron el filter
            engModel=request.GET.get("engine_id")   # Valor del modelo del motor
            comp=spare.objects.filter(engine_info__engine_ide__icontains=engModel)  # Creo un Query de spare que tenga el valor del motor pasado
            return render(request,"Repuestosapp/find.html",{"formulariop":formulario_busqueda,"allCars":allCars,"onlyManufCars":onlyManufCars,"allEngines":allEngines,"spare":comp})
    else:   # Si se usa el buscador por código de repuesto
        if request.GET.get("search"):
            valor=request.GET.get("search")
            comp=spare.objects.filter(spare_code__icontains=valor) # Compara el codigoRepuesto con valor
            return render(request,"Repuestosapp/find.html",{"formulariop":formulario_busqueda,"allCars":allCars,"onlyManufCars":onlyManufCars,"allEngines":allEngines,"spare":comp})
        else:    
            test=val
            pr=spare.objects.filter(engine_info__engine_ide__icontains=test)
            return render(request,"Repuestosapp/engine.html",{"brand_id":pr,"formulariop":formulario_busqueda,"allCars":allCars,"onlyManufCars":onlyManufCars,"allEngines":allEngines})
    





# def base(request): # Sólo el formulario busqueda y el filtro izquierdo
#     formulario_busqueda=Formulario()
#     allEngines=engine.objects.all()# Consigo TODOS los motores
#     onlyManufCars=car.objects.all().values("car_manufacturer").distinct()# Conseguir TODOS los carros por fabricante
#     allCars=car.objects.all()# Conseguir TODOS los carros
#     comp=spare.objects.none()
#     return render(request,"Repuestosapp/base.html",{"formulariop":formulario_busqueda,"spare":comp,"allCars":allCars,"onlyManufCars":onlyManufCars,"allEngines":allEngines})

# def home(request):
#     return render(request,"Repuestosapp/home.html")
