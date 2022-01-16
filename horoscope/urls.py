from django.urls import path, register_converter
from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, 'yyyy')
register_converter(converters.MyFloatConverter, 'my_float')
register_converter(converters.MyDateConverter, 'my_date')

urlpatterns = [
    path('', views.index, name='horoscope-index'),
    path('type', views.view_zodiac_types),
    path('type/<str:zodiac_type>', views.get_info_about_zodiac_type, name='zodiac-type'),
    path('<my_date:sign_zodiac>', views.get_my_date_converters),
    path('<yyyy:sign_zodiac>', views.get_yyyy_converters),
    path('<int:sign_zodiac>', views.get_info_about_sign_zodiac_by_number),
    path('<my_float:sign_zodiac>', views.get_my_float_converters),
    path('<str:sign_zodiac>', views.get_info_about_sign_zodiac, name='horoscope-name'),
    path('<int:month>/<int:day>', views.get_info_by_date),
]