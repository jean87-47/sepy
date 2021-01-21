from django.urls import path
from . import views

app_name='articles'

urlpatterns=[
   path('', views.index,name='index'),
   path('create/',views.create,name='create'),
   path('new/',views.new,name='new'),
   path('new_create/',views.new_create,name='new_create'),
   path('list/',views.list,name='list'),
   path('<int:pk>/',views.detail,name='detail'),
   path('<int:pk>/like/',views.like,name='like'),
   path('<int:pk>/delete/',views.delete,name='delete'),
   path('<int:pk>/edit/',views.edit,name='edit'),
   path('<int:pk>/edit_get/',views.edit_get,name='edit_get'),
   path('<int:pk>/update_get/',views.update_get,name='update_get'),
   path('<int:pk>/comments/',views.comments,name='comments'),
   path('comments/<int:pk>/delete/',views.comment_delete,name='comment_delete'),
   path('<int:pk>/like/',views.like,name='like'),




]