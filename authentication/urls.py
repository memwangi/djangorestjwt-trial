from django.urls import path, include, re_path
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token


from .views import RegistrationAPIView
router = routers.DefaultRouter()

app_name = "authentication"

urlpatterns = [
    re_path(r'register/', RegistrationAPIView.as_view()),
    re_path(r'^login/', obtain_jwt_token, name='get-token'),
    re_path(r'^token-refresh/', refresh_jwt_token),
    re_path(r'^token-verify/', verify_jwt_token),   
]
