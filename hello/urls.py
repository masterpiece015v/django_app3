from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('<int:num>',views.index,name='index'),
    path('find/',views.find,name='find'),
    path('check/',views.check,name='check'),
    path('message/',views.message,name='message'),
    path('message/<int:page>',views.message,name='message'),
]