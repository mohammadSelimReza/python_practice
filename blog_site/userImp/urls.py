from django.urls import path
from . import views

urlpatterns = [
    path("signup/",views.registerPage,name="signup"),
    path('login/',views.userLogin,name='loginPage'),
    path('logout/',views.userLogout,name='userLogOut')
    
]
