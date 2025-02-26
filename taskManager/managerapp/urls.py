from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:task_id>/", views.detail, name="detail"),
    path("<int:task_id>/results/", views.results, name="results"),
    path("<int:task_id>/results/complete/", views.complete, name="complete"),
]
