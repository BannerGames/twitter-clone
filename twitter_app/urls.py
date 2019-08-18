from django.urls import path, include
from . import views


urlpatterns = [
    # Index Page(log in gate)
    path('', views.index, name='index'),

    # Thanks Page
    path('thanks/', views.thanks, name='sucesso'),

    # Profile Page
    path('profile/', views.profile, name='perfil'),

    # Following and Followers Page
    path('follow_info/', views.follow_info, name='seguindo'),

    # Settings Page
    path('profile_settings/', views.profile_settings, name='configuracoes'),

    # Other User Page
    path('other_user/<str:username>/', views.other_user_profile, name='usuario'),

    # Other User Follow info page
    path('other_user/<str:username>/follow_info/', views.other_user_follow_info, name='usuario_seguindo'),

    # Home page for recent tweets
    path('home/', views.home, name='inicio'),

    # Explore page
    path('explore/', views.explore, name='explorar')
]
