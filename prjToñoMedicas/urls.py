"""prjToñoMedicas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from appToñoMedicas import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.Views.index, name="index"),
    url(r'^dashboard$', views.Views.dashboard, name="dashboard"),
    url(r'^user$', views.Views.profile, name="user"),
    url(r'^table$', views.Views.table, name="user"),
    url(r'^typography$', views.Views.typography, name="user"),
    url(r'^icons$', views.Views.icons, name="user"),
    url(r'^maps$', views.Views.maps, name="user"),
    url(r'^notifications$', views.Views.notifications, name="user"),
    url(r'^upgrade$', views.Views.upgrade, name="user")
]
