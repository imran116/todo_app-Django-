from django.urls import path

from todo import views

urlpatterns = [
    path('', views.home, name='home' ),
    path('add-task/', views.add_task, name='add-task' ),
    path('update-task/<str:pk>/', views.edit_task, name='update-task' ),
    path('delete-task/<str:pk>/', views.delete_task, name='delete-task' ),


]