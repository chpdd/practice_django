from django.urls import include, path

from . import views

app_name = "app1"

urlpatterns = [
    path('', views.index, name="index"),
    path('semester/<int:semester_number>', views.semester, name="semester"),
    path('semester/<int:semester_number>/task/<str:task_name>', views.task, name="task"),
    path('jquery_test', views.jquery_test, name="jquery_test")
]