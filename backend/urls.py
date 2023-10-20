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
    path('StartMeeting/', views.StartMeeting), # générer le code d'un meeting
    path('SettingMeeting/<int:roomName>/', views.SettingMeeting), # Paramètrer une salle de réunion
    path('JoinMeeting/<int:roomName>/', views.JoinMeeting), # Rejoindre un meeting
    path('AddCommentMeeting/Participant/<int:pkUser>/Codemeet/<int:roomName>/', views.AddCommentMeeting), # Ajouter un commentaire dans le meeting
    path('ViewCommentMeeting/<int:pkMeeting>/', views.ViewCommentMeeting), # Voir tous les commentaires d'un meeting
]