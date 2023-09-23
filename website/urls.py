from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('record/<int:pk>/', views.customer_record, name='record'),
    path('record/delete/<int:pk>/', views.delete_record, name='delete_record'),
    path('record/add/', views.add_record, name='add_record'),  # Add this line
    path('record/edit/<int:pk>/', views.edit_record, name='edit_record'),



]
