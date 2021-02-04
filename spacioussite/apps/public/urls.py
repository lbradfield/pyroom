from django.urls import path
import apps.public.views

app_name = "public"
urlpatterns = [
    path("", apps.public.views.index, name="home"),
    path("about", apps.public.views.about, name="about"),
    path("contact", apps.public.views.contact, name="contact"),
]
