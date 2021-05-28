from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
# from django.conf.urls.static import templatetags

from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('find',views.find,name='find'),
    path('findfil',views.findfil,name='findfil'),
    path('brand/<str:val>',views.brand,name='brand'),
    path('name/<str:val>',views.name,name='name'),
    path('manuf/<str:val>',views.manuf,name='manuf'),
    path('model/<str:val>',views.model,name='model'),
    path('engine/<str:val>',views.enginei,name='engine'),
    path('sparedetails/<str:val>',views.sparedetails,name='sparedetails'),
    path('prueba',views.prueba,name='prueba'),
    # path('prueba1/<str:val>',views.prueba1,name='prueba1'),
    path('prueba1',views.prueba1,name='prueba1'),
    path('registro/',views.VistaRegistro.as_view(),name='registro'),
    path('salir',views.salir,name='salir'),
    path('acceder',views.acceder,name='acceder'),
    path('add2car/<str:spare_id>',views.add2car,name='add2car'),
    path('er2car/<str:spare_id>',views.er2car,name='er2car'),
    path('detail',views.detail,name='detail'),

]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)