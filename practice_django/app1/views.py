from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    context = {
        "semester_numbers": [3, 4]
    }
    return render(request, template_name="app1/index.html", context=context)


def semester(request, semester_number):
    context = {
        "semester_number": semester_number
    }
    if 3 <= semester_number <= 4:
        if semester_number == 3:
            context["task_numbers"] = range(1, 9)
        elif semester_number == 4:
            pass
        return render(request,
                      template_name=f"app1/semester.html",
                      context=context)
    else:
        return HttpResponse("Нет семестра с таким номером")


def task(request, semester_number, task_number):
    context = {
        "semester_number": semester_number
    }
    if task_number == 7:
        context["jpg_names"] = [f'app1/media/{i}.jpg' for i in range(1, 9)]
    if 1 <= task_number <= 8:
        return render(request,
                      template_name=f"app1/task{task_number}.html",
                      context=context)
    else:
        return HttpResponse("Нет задачи с таким номером")


def jquery_test(request):
    return render(request, template_name="app1/jquery_test.html")
