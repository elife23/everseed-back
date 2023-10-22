from django.urls import path
from . import views 
from .views import MyTokenObtainPairView  
from rest_framework_simplejwt.views import (
    #TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('SignUp/', views.SignUp), # Enregistrer un user
    path('SignIn/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'), # Authentifier un user avec génération d'un token de connexion
    path('SignIn/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # Mettre à jour le token de connexion
    path('ViewUser/<int:pkUser>/', views.ViewUser), # Afficher les informations d'utilisateur
    path('LaunchMeeting/', views.LaunchMeeting), # Lancer un meeting
    path('SettingMeeting/<int:roomName>/', views.SettingMeeting), # Paramètrer une salle de réunion
    path('JoinMeeting/<int:roomName>/', views.JoinMeeting), # Rejoindre un meeting
    path('AddCommentMeeting/<int:roomName>/Participant/<int:pkUser>/', views.AddCommentMeeting), # Ajouter un commentaire dans le meeting
    path('ViewCommentMeeting/<int:roomName>/', views.ViewCommentMeeting), # Voir tous les commentaires d'un meeting
    path('LaunchWhiteboard/', views.LaunchWhiteboard), # Lancer un whiteboard
    path('ViewCommentWhiteboard/<int:whiteName>/', views.ViewCommentWhiteboard), # Lancer un whiteboard
]