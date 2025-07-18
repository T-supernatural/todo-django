from django.urls import path
from .views import home_page, add_form

urlpatterns = [
    path('', home_page, name='home'),
    path('add/', add_form, name='add'),
]