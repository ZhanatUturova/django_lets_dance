from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

from dataclasses import dataclass


zodiac_dict = {
    "aries": {
        'description': "Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).",
        'date': ((3, 4), (21, 20))
    },
    "taurus": {
        'description': "Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).",
        'date': ((4, 5), (21, 21))
    },
    "gemini": {
        'description': "Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).",
        'date': ((5, 6), (22, 21))
    },
    "cancer": {
        'description': "Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).",
        'date': ((6, 7), (22, 22))
    },
    "leo": {
        'description': "Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).",
        'date': ((7, 8), (23, 21))
    },
    "virgo": {
        'description': "Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).",
        'date': ((8, 9), (22, 23))
    },
    "libra": {
        'description': "Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).",
        'date': ((9, 10), (24, 23))
    },
    "scorpio": {
        'description': "Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).",
        'date': ((10, 11), (24, 22))
    },
    "sagittarius": {
        'description': "Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).",
        'date': ((11, 12), (23, 22))
    },
    "capricorn": {
        'description': "Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).",
        'date': ((12, 1), (23, 20))
    },
    "aquarius": {
        'description': "Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).",
        'date': ((1, 2), (21, 19))
    },
    "pisces": {
        'description': "Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).",
        'date': ((2, 3), (20, 20))
    }
}


zodiac_types = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces']
}


def index(request):
    context = {
        'zodiac_dict': zodiac_dict
    }
    return render(request, 'horoscope/index.html', context=context)


def get_info_about_sign_zodiac(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac).get('description')
    data = {
        'description_zodiac': description,
        'sign': sign_zodiac,
        'zodiac_dict': zodiac_dict,
    }
    return render(request, 'horoscope/info_zodiac.html', context=data)


def view_zodiac_types(request):
    li_elements = ''
    for t in zodiac_types.keys():
        redirect_path = reverse("zodiac-type", args=(t,))
        li_elements += f"<li><a href='{redirect_path}'>{t.title()}</a></li>"
    response = f"""
    <ul>
        {li_elements}
    </ul>
    """
    return HttpResponse(response)


def get_info_about_zodiac_type(request, zodiac_type: str):
    zodiac_type_list = zodiac_types.get(zodiac_type)
    if zodiac_type_list:
        li_elements = ''
        for elem in zodiac_type_list:
            redirect_path = reverse("horoscope-name", args=(elem,))
            li_elements += f"<li><a href='{redirect_path}'>{elem.title()}</a></li>"
        response = f"""
        <ul>
            {li_elements}
        </ul>
        """
        return HttpResponse(response)
    else:
        return HttpResponseNotFound(f'У знаков зодиака нет такой стихии - {zodiac_type}')


@dataclass
class Person:
    name: str
    age: int

    def __str__(self):
        return f'This is {self.name}'


def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound(f'Неправильный порядковый номер знака зодиака - {sign_zodiac}')
    name_zodiac = zodiacs[sign_zodiac - 1]
    redirect_url = reverse("horoscope-name", args=(name_zodiac,))
    return HttpResponseRedirect(redirect_url)


def get_info_by_date(request, month: int, day: int):
    if (1 <= month <= 12) and (1 <= day <= 31):
        for zodiac in zodiac_dict:
            if (month == zodiac_dict[zodiac]['date'][0][0] or month == zodiac_dict[zodiac]['date'][0][1]) \
                and (zodiac_dict[zodiac]['date'][1][0] >= day <= zodiac_dict[zodiac]['date'][1][1]):
                redirect_url = reverse('horoscope-name', args=(zodiac, ))
                return HttpResponse(f'<h2><a href={redirect_url}>{zodiac}</a></h2>')
    else:
        return HttpResponseNotFound(f'вы ввели неверные данные')


def get_yyyy_converters(request, sign_zodiac: int):
    return HttpResponse(f'Вы передали число из 4х цифр - {sign_zodiac}')


def get_my_float_converters(request, sign_zodiac):
    return HttpResponse(f'Вы передали вещественное число - {sign_zodiac}')


def get_my_date_converters(request, sign_zodiac):
    return HttpResponse(f'Вы передали дату - {sign_zodiac}')
