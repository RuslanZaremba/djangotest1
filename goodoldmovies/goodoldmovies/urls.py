"""
URL configuration for goodoldmovies project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

from movies.views import movie_view, ex_view, MainView, AboutView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', movie_view, name='main'),
    path('ex/<int:text>', ex_view, name='ex_view'),
    path('', MainView.as_view()),
    path('about/', AboutView.as_view()),
]
