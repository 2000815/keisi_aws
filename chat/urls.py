from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views



app_name = 'chat'
urlpatterns = [
    path( 'chat', views.chat, name='chat' ),
    path('', auth_views.LoginView.as_view(template_name='registration/login.html')),

]

