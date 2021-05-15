from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from Repuestosapp import views

urlpatterns = [
    path('', views.home,name='home'),
    path('find',views.find,name='find'),
    # path('brand',views.brand,name='brand'),
    path('brand/<str:val>',views.brand,name='brand'),
    path('name/<str:val>',views.name,name='name'),
    path('manuf/<str:val>',views.manuf,name='manuf'),
    path('model/<str:val>',views.model,name='model'),
    path('engine/<str:val>',views.enginei,name='engine'),
    # path('', views.base,name='base'),
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)