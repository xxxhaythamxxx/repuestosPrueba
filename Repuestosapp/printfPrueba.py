# import os
# from django.core.wsgi import get_wsgi_application
# os.environ['DJANGO_SETTINGS_MODULE'] = 'ProyectoRepuestos.settings'
# application = get_wsgi_application()
# from ProyectoRepuestos.wsgi import *
from django.template.loader import get_template
# from weasyprint import HTML
from django.shortcuts import render, HttpResponse

# def printPrueba():
#     template=get_template("Repuestosapp/prueba.html")
#     context={"name":"Luis Velasco"}
#     html_template=template.render(context)
#     HTML(string=html_template).write_pdf(target="Repuestosapp/prueba.pdf")

# printPrueba()


from io import BytesIO
from django.http import HttpResponse
from django.views import View
from xhtml2pdf import pisa
