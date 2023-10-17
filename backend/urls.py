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
    path('showUser/<int:pkUser>/', views.showUser), # Afficher les informations d'utilisateur
    path('StartMeet/', views.StartMeet), # générer le code d'un meeting
    path('SettingMeet/', views.SettingMeet), # Paramètrer une salle de réunion
    path('JoinMeet/', views.JoinMeet), # Rejoindre un meeting
    path('AddCommentMeeting/', views.AddCommentMeeting), # Ajouter un commentaire dans le meeting
    path('ViewCommentMeeting/<int:pkMeeting>/', views.ViewCommentMeeting), # Voir tous les commentaires d'un meeting
]