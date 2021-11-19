from django.contrib import admin
from django.urls import path
from users  import views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user-customer/', views.UserCreateView.as_view()),
    path('user-admin/', views.UserCreateView.as_view()),
    path('user-customer/detail/<int:pk>/', views.UserDetailView.as_view()),
    path('user-customer/update/<int:pk>/', views.UserUpdateView.as_view()),
    path('user-customer/delete/<int:pk>/', views.UserDeleteView.as_view()),      
    path('verifyToken/',   views.VerifyTokenView.as_view()),
    path('refresh/',   TokenRefreshView.as_view()),
    path('login/',         TokenObtainPairView.as_view()),
]