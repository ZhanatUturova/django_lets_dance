from django.urls import path
from . import views

urlpatterns = [
    path('rectangle/<int:width>/<int:height>', views.get_rectangle_area, name='get-rectangle-area'),
    path('get_rectangle_area/<int:width>/<int:height>', views.new_get_rectangle_area),
    path('square/<int:width>', views.get_square_area, name='get-square-area'),
    path('get_square_area/<int:width>', views.new_get_square_area),
    path('circle/<int:radius>', views.get_circle_area, name='get-circle-area'),
    path('get_circle_area/<int:radius>', views.new_get_circle_area),
]
