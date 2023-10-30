from django.urls import path
from . import views 
from .views import MyTokenObtainPairView  


urlpatterns = [
    path('SignUp/', views.SignUp), # Enregistrer un user
    path('SignIn/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'), # Authentifier un user avec génération d'un token de connexion
    path('ViewUser/<int:pkUser>/', views.ViewUser), # Afficher les informations d'utilisateur
    path('LaunchMeeting/', views.LaunchMeeting), # Lancer un meeting
    path('SettingMeeting/<int:roomName>/', views.SettingMeeting), # Paramètrer une salle de réunion
    path('JoinMeeting/<int:roomName>/', views.JoinMeeting), # Rejoindre un meeting
    path('AddCommentMeeting/<int:roomName>/Participant/<int:pkUser>/', views.AddCommentMeeting), # Ajouter un comment dans le meeting
    path('ViewCommentMeeting/<int:roomName>/', views.ViewCommentMeeting), # Voir tous les comments d'un meeting
    path('LaunchWhiteboard/', views.LaunchWhiteboard), # Lancer un whiteboard
    path('AddCommentWhiteboard/<int:whiteName>/', views.AddCommentWhiteboard), # Ajouter un comment dans le whiteboard
    path('ViewCommentWhiteboard/<int:whiteName>/', views.ViewCommentWhiteboard), # Voir tous les comments d'un whiteboard
]