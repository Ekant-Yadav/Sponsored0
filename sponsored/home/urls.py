from home import views
from django.urls import path
from profiles_api import views as apiviews
from organiser import views as orgviews

urlpatterns = [
    path('',views.index,name="index"),
    path("login/<str:slug>",apiviews.loginuser,name="login"),
    path("signup",apiviews.signupuser,name="signup"),
    path("organiser", orgviews.events, name="organiser"),
    path("logout", apiviews.logoutuser, name="logout")
]
 