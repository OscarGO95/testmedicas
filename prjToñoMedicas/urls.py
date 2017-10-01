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
from django.conf.urls import url,include
from django.contrib import admin
from appToñoMedicas import views
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('', include('social.apps.django_app.urls', namespace="social")),
    url(r'^$',views.Views.index, name="index"),
    url(r'^dashboard$', views.Views.dashboard, name="dashboard"),
    url(r'^user$', views.Views.profile, name="user"),
    url(r'^login$', views.Views.login, name="login"),
    url(r'logout$', views.Views.logout)
]
'''
    url(r'^table$', views.Views.table, name="table"),
    url(r'^typography$', views.Views.typography, name="typography"),
    url(r'^icons$', views.Views.icons, name="icons"),
    url(r'^maps$', views.Views.maps, name="maps"),
    url(r'^notifications$', views.Views.notifications, name="notifications"),
    url(r'^upgrade$', views.Views.upgrade, name="upgrade"),
    '''