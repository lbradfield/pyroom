from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    return HttpResponse("Hello world, you're at the accounts index!")

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/profile.html"
