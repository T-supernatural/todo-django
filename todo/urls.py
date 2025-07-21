from django.urls import path
from .views import home_page, create_task, task_list

urlpatterns = [
    path('', home_page, name='home'),
    path('add/', create_task, name='create_task'),
    path('update/', task_list, name='task_list'),
    # path('update/<int:book_id>/', update_view, name='update_page')
]