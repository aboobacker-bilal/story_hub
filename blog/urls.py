from django.urls import path
from . import views

urlpatterns = [
    path('', views.starting_page, name="start"),
    path('single_story/<int:pk>', views.single_stories, name='single-story'),
    path("all_stories", views.all_stories, name="all-story")
]
