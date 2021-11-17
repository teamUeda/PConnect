from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('top/', views.Top.as_view(), name='top'),
    path('create/', views.Create_account.as_view(), name='create'),
]
