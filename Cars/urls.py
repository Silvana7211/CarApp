from django.urls import path
from Cars import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('Cars/', views.CarList.as_view()),
    path('Cars/<int:pk>/', views.CarDetail.as_view()),
    path('Seller/', views.SellerList.as_view()),
    path('Seller/<int:pk>/', views.SellerDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)