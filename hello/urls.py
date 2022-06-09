from django.urls import path
from . import views

urlpatterns = [
    path('<int:num>',views.index,name='index'),
    path('find/',views.find,name='find'),
    path('check/',views.check,name='check'),
]