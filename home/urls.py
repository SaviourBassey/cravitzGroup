from . import views
from django.urls import path

app_name = "home"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home_view"),
    path("about-us/", views.AboutView.as_view(), name="about_view"),
    path("contact-us/", views.ContactView.as_view(), name="contact_view"),
    path("our-services/", views.ServicesView.as_view(), name="services_view"),
    path("blog/", views.NewsView.as_view(), name="news_view"),
]
