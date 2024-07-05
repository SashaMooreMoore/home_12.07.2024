from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'help/?$', views.PageHelp.as_view(), name="urlPageHelp"),
    path('new/<int:id>', views.PageNew.as_view(), name="urlPageNew"),
    path('', views.PageStatic.as_view(), name="urlPageStatic"),
]