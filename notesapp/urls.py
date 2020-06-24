from django.urls import path
from . import views

app_name = 'notesapp'

urlpatterns = [
    path('', views.login, name = 'login'),
    path('register/', views.register, name = 'register'),
    
    path('logout/', views.logout, name = 'logout'),
    path('list/', views.list, name = 'list'),
    path('create', views.create, name = 'create'),
    path('addnew', views.list),
    path('list/delete/<int:id>', views.delete, name='delete'),
    path('list/edit/<int:id>', views.edit, name='edit'),
    #path('finish/edit/addnew', views.saving),


]