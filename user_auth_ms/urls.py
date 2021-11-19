from django.contrib import admin
from django.urls import path
from users  import views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user-customer/', views.UserCreateView.as_view()),
    path('user-admin/', views.UserCreateView.as_view()),     
    path('verifyToken/',   views.VerifyTokenView.as_view()),
    path('refresh/',   TokenRefreshView.as_view()),
    path('login/',         TokenObtainPairView.as_view()),
]