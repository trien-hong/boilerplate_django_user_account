from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index_view'),
    path('login/', views.login_view, name='login_view'),
    path('signup/', views.signup_view, name='signup_view'),
    path('index/', views.index_view, name='index_view'),
    path('logout_user/', views.logout_user, name='logout_user')
]