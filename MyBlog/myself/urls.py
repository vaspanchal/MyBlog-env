from django.urls import path
from . import views  # it means from (same current package) import views, = `from myself import views`, both are same
urlpatterns = [
    path("",views.home,name="home"),
]