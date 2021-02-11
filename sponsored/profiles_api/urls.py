from profiles_api import views
from django.urls import path


urlpatterns = [
   path("login",views.loginuser,name="login"),
   path("signup", views.signupuser,name="signup")
]
