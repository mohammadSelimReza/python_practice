from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog_app.urls')),  
    path('blog/',include('blog.urls')),
    path('character/',include('character.urls')),
    path('login/',include("userImp.urls")),
]
