from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

days_dict = {
    'monday': 'список дел, запланированных на понедельник',
    'tuesday': 'список дел, запланированных на вторник',
    'wednesday': 'список дел, запланированных на среду',
    'thursday': 'список дел, запланированных на четверг',
    'friday': 'список дел, запланированных на пятницу',
    'saturday': 'список дел, запланированных на субботу',
    'sunday': 'список дел, запланированных на воскресенье'
}


def get_info_about_day_works(request, day_name: str):
    description = days_dict.get(day_name)
    if description:
        return HttpResponse(description)
    else:
        return HttpResponseNotFound('Нет такого дня недели')


def get_todo_week_index(request):
    return render(request, 'week_days/greeting.html')


def get_number_of_day_works(request, day_number: int):
    days = list(days_dict)
    if day_number > len(days):
        return HttpResponseNotFound(f'Неверный номер дня - {day_number}')
    day = days[day_number - 1]
    redirect_url = reverse("todo-day-name", args=(day,))
    return HttpResponseRedirect(redirect_url)
