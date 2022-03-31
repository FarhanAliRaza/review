
from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('review/<str:id>/', views.review, name='review'),
    path('review_store/ajax/', views.review_store, name='review_store'),
    path('admin_view/', views.admin_view, name='admin_view'),
    path('download_customer_csv/', views.download_customer_csv, name='download_customer_csv'),
    path('download_store_csv/', views.download_store_csv, name='download_store_csv'),



   

   



]

