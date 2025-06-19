from django.urls import path
from stockapp import views

urlpatterns = [
    path('',views.home, name='home'),
    path('about/', views.about, name ="about"),
    path('addstock/', views.addstock, name="addstock"),
    path('delete/<int:pk>/',views.delete, name='delete'),
    path('delete_stock/',views.delete_stock, name='delete_stock')
]
