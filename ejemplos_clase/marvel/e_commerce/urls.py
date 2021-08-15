from django.urls import path
from e_commerce.api.marvel_api_views import *

# Importamos las API_VIEWS:
from e_commerce.views import *

urlpatterns = [
    # e_commerce base:
    path('base', PruebaView.as_view()),
    path('text', TextView.as_view()),
    path('links', LinksView.as_view()),
    path('lists', ListsView.as_view()),
    path('button', ButtonsView.as_view()),
    path('table', TableView.as_view()),
    path('form', FormView.as_view()),
    path('image', ImageView.as_view()),
    path('example', ExampleView.as_view()),
    ]