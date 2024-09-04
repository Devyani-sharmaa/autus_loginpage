from django.urls import path
from myauth import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name = "home"),
    path("about", views.about, name = "about"),
    path("login", views.loginpage, name = "loginpage"),
    path("signup", views.signuppage, name = "signuppage"),
    path("lets-logout", views.logutnow, name = "logout"),
   
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
