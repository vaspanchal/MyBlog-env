

from blog import views
from django.urls import path


urlpatterns = [
    path("", views.blog_home, name="blog"), # empty url
    path("<int:blog_id>", views.blog_details, name="blog_details"),
    path("year/<int:year>", views.yearly_archive, name="yearwise"),
    path("month/<int:month>", views.monthly_archive, name="monthwise"),
    path("<int:blog_id>/comments", views.comment,name="comments"),
]