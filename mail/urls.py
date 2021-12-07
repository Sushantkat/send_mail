from django.urls import path
from . import views

app_name = 'mail'
urlpatterns = [
    path('', views.email_save_send, name='save_send_email'),
]
