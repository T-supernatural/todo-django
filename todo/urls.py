from django.urls import path
from .views import home_page, add_form, details_home, update_view

urlpatterns = [
    path('', home_page, name='home'),
    path('add/', add_form, name='add'),
    path('task/<int:book_id>/', details_home, name='details_page'),
    path('update/<int:book_id>/', update_view, name='update_page')
]