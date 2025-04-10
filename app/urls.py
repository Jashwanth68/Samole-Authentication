from django.urls import path
from .views import home, verify_token

urlpatterns = [
    path('', home, name='home'),
    path('verify-token/', verify_token, name='verify-token'),
]
