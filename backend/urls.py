from django.urls import path
from . import views 
from .views import MyTokenObtainPairView  
from rest_framework_simplejwt.views import (
    #TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('SignUp/', views.SignUp),
    path('SignIn/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('SignIn/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('showUser/<int:pkUser>/', views.showUser),
    path('StartMeet/', views.StartMeet),
    path('SettingMeet/', views.SettingMeet),
    path('JoinMeet/', views.JoinMeet),
]