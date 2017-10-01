# -*- coding: utf-8 -*-
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


class Views:

    def index(request):
        return render(request, "ppalTemplate/index.html")

    @login_required(login_url='login')
    def dashboard(request):
        return render(request, "views/index.html")

    @login_required(login_url='login')
    def profile(request):
        return render(request, "views/user.html")

    def login(request):
        return render(request, "loginTemplate/login.html")

    def logout(request):
        logout(request)
        return redirect("/")
'''
    def table(request):
        return render(request, "dashAdmin/table.html")

    def typography(request):
        return render(request, "dashAdmin/typography.html")

    def icons(request):
        return render(request, "dashAdmin/icons.html")

    def maps(request):
        return render(request, "dashAdmin/maps.html")

    def notifications(request):
        return render(request, "dashAdmin/notifications.html")

    def upgrade(request):
        return render(request, "dashAdmin/upgrade.html")
'''