"""
URL configuration for practice_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.apps import apps

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
]

for app in apps.get_app_configs():
    app_name = app.name
    if app_name == "home" or "django" in app_name:
        continue
    urlpatterns.append(
        path(f'{app_name}/', include(f'{app_name}.urls'))
    )
    # try:
    #     reverse(f"{app_name}")
    #     app_names.append(app_name)
    # except NoReverseMatch:
    #     continue
