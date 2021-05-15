from django.db import models

# Create your models here.
class car(models.Model):
    car_manufacturer=models.CharField(max_length=20, verbose_name="Manufacturer")    #Ejemplo: Audi
    car_model=models.CharField(max_length=30, verbose_name="Model")           #Ejemplo: 100 C1 Coupe (817)
    VIN=models.CharField(max_length=18, blank=True)
    car_from=models.DateField(verbose_name="From")      #Ejemplo: 11/2015
    car_to=models.DateField(verbose_name="To")          #Ejemplo: 11/2018
    transmission=models.CharField(max_length=10)        #Ejemplo: ATM, MTM (Automatic, Manual)

    def __str__(self):
        return '%s %s, (%s / %s)' %(self.car_manufacturer, self.car_model, self.car_from.year, self.car_to.year)

class engine(models.Model):
    car_engine_info=models.ManyToManyField(car)
    engine_l=models.CharField(max_length=6, verbose_name="Litre")             #Ejemplo: 1.8 D
    engine_ide=models.CharField(max_length=10, verbose_name="Code")          #Ejemplo: 1GRFE
    engine_type=models.CharField(max_length=10, verbose_name="Type")         #Ejemplo: Diesel, Petrol
    engine_cylinder=models.IntegerField(verbose_name="Cylinder (ccm)")               #Ejemplo: 1588 ccm
    engine_pistons=models.IntegerField(verbose_name="Pistons")                #Ejemplo: 4 pistons
    engine_power_kw=models.IntegerField(verbose_name="Power (kW)")               #Ejemplo: 63 kw
    engine_power_hp=models.IntegerField(verbose_name="Power (hp)")               #Ejemplo: 85 hp

    def __str__(self):
        return '%s %s %s %s ccm/%s pistons %s kW/%s hp' %(self.engine_l, self.engine_ide, self.engine_type, self.engine_cylinder, self.engine_pistons, self.engine_power_kw, self.engine_power_hp)
    
class spare(models.Model):
    car_info=models.ManyToManyField(car)
    engine_info=models.ManyToManyField(engine)
    spare_photo=models.ImageField(upload_to="spares")         #Será ImageField()
    spare_code=models.CharField(max_length=15, verbose_name="Code")          #Ejemplo: 50013073
    spare_brand=models.CharField(max_length=15, verbose_name="Brand")         #Ejemplo: KOLBENSCMIDT
    spare_name=models.CharField(max_length=20, verbose_name="Name")          #Ejemplo: Oil filter

    def __str__(self):
        return '%s %s %s' %(self.spare_code, self.spare_brand, self.spare_name)


