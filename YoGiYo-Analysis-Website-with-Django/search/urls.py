"""termproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from .views import searching, analysis, menu, image, keyword, imageview

app_name = 'search'

urlpatterns = [
    path('', searching, name='search'),
    path('<int:id>/', analysis, name='analysis'),
    path('<int:id>/menu/', menu, name='menu'),
    path('<int:id>/image/', image, name='image'),
    path('<int:id>/image/<int:mnid>/', imageview, name='imageview'),
    path('<int:id>/keyword/', keyword, name='keyword'),
]

