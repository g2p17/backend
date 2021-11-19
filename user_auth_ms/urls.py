from django.contrib import admin
from django.urls import path
from users  import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user-customer/', views.UserCreateView.as_view()),
    path('verifyToken/',   views.VerifyTokenView.as_view()), 
]