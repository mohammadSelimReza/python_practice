from django.urls import path
from . import views
urlpatterns = [
    path("add/", views.home),
    path('edit/<int:id>', views.edit_post, name='edit'),
    path('delete/<int:id>', views.delete_post, name='delete'),
]
