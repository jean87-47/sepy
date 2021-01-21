from django.urls import path
from . import views

app_name='games'

urlpatterns=[
    path('', views.index,name='index'),
    path('lotto/',views.lotto,name='lotto'),
    path('pick_present/',views.pick_present,name='pick_present'),
    path('hi/<str:name>/',views.hi,name='hi'),
    path('add/<int:a>/<int:b>/',views.add, name='add'),
    path('number/',views.number,name='number'),
    path('posts/<int:id>/',views.posts,name='posts'),


]