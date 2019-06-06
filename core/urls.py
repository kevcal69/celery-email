
from django.conf.urls import url

from . import views

urlpatterns = [
    url('email-queue', views.EmailView.as_view(), name='send-email')
]
