from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_todo_week_index),
    path('<int:day_number>', views.get_number_of_day_works),
    path('<str:day_name>', views.get_info_about_day_works, name='todo-day-name'),
]