from django.shortcuts import render

# Importamos vistas genericas:
from django.views.generic import TemplateView
 
# Probamos la vista generica:
class PruebaView(TemplateView):
    template_name = 'e_commerce/base.html'

# NOTE: Generamos las vistas genéricas para probar bloques HTML:

class TextView(TemplateView):
    template_name = 'e_commerce/00-text.html'

class LinksView(TemplateView):
    template_name = 'e_commerce/01-links.html'

class ListsView(TemplateView):
    template_name = 'e_commerce/02-listas.html'

class ButtonsView(TemplateView):
    template_name = 'e_commerce/03-buttons.html'

class TableView(TemplateView):
    template_name = 'e_commerce/04-table.html'

class FormView(TemplateView):
    template_name = 'e_commerce/05-form.html'

class ImageView(TemplateView):
    template_name = 'e_commerce/06-images.html'

class ExampleView(TemplateView):
    template_name = 'e_commerce/example.html'
    