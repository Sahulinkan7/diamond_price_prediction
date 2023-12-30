from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("training/",views.training_view,name="training"),
    path("prediction/",views.prediction_view,name="prediction"),
]
