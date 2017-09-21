from django.shortcuts import render

class Views:

    def index(request):
        return render(request, "ppalTemplate/index.html")

    def dashboard(request):
        return render(request, "dashAdmin/dashboard.html")

    def profile(request):
        return render(request, "dashAdmin/user.html")

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