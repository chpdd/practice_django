from django.urls import include, path, reverse, NoReverseMatch
from django.apps import apps
from django.shortcuts import redirect

from . import views

app_name = "home"

urlpatterns = [
    path('', views.home, name='home'),
]


# def make_redirect_to_app(name):
#     return lambda request: redirect(f"{name}:index")


for app in apps.get_app_configs():
    app_name = app.name
    if "home" == app_name or "django" in app_name:
        continue
    urlpatterns.append(
        path(f'{app_name}/', include(f"{app_name}.urls"))
    )
