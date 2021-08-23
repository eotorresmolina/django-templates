from django.shortcuts import render

from django.views.generic import TemplateView

# Create your views here.

class TableView(TemplateView):
    template_name = 'e_commerce/table.html'

class ListView(TemplateView):
    template_name = 'e_commerce/list.html'

class FormView(TemplateView):
    template_name = 'e_commerce/form.html'

class TextView(TemplateView):
    template_name = 'e_commerce/text.html'

class ImageView(TemplateView):
    template_name = 'e_commerce/image.html'

class PostComicView(TemplateView):
    template_name = "e_commerce/form_comic.html"
