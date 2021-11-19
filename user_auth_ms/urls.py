from django.contrib import admin
from django.urls import path
from users  import views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)


from django.urls import re_path
from rest_framework import permissions
from drf_yasg2.views import get_schema_view
from drf_yasg2 import openapi


#Configuración Swagger 
schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('user-customer/create/', views.UserCreateView.as_view()),
    path('user-admin/', views.UserCreateView.as_view()),  
    path('user-customer/detail/<int:pk>/', views.UserDetailView.as_view()),
    path('user-customer/update/<int:pk>/', views.UserUpdateView.as_view()),
    path('user-customer/delete/<int:pk>/', views.UserDeleteView.as_view()),
    path('verifyToken/',   views.VerifyTokenView.as_view()),
    path('refresh/',   TokenRefreshView.as_view()),
]