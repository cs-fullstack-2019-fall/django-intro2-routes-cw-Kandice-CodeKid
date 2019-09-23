from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('gogetthegood/', views.goge, name='goge'),
    path('happyhappyjoyjoy/', views.happyJoy, name='happyjoy'),
    path('something/<str:words>', views.words_test),
]