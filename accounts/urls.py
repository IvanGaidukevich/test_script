from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('profile/', views.profile_view, name='profile_view'),
]