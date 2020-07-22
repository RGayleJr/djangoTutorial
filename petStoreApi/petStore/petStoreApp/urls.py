from django.urls import path
from petStoreApp import views

urlpatterns = [
    path('animals/<str:animal>/', views.animal_list),
    path('animals/<str:animal>/<int:pk>/', views.animal_detail),
    path('users/1/', views.admin_list),
    path('users/0/', views.user_only_list),
    path('users/1/<int:pk>', views.admin_detail),
    path('users/0/<int:pk>', views.user_only_detail)
]