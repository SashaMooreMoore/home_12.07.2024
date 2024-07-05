from django.urls import path
from . import views

urlpatterns = [
    path('', views.PageSession.as_view())
]