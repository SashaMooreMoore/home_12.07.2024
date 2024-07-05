from django.urls import path
from . import views
urlpatterns = [
    path('', views.PageHome.as_view(), name="urlPageHome"),
    path('test', views.PageTestAnnotations.as_view(), name="urlPageTestAnnotations"),
    path('bank', views.PageBank.as_view(), name="urlPageBank"),
]
