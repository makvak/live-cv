from django.urls import path
from .views import (
    HomeView,
    SignInView
)


urlpatterns = [
    path(r'', HomeView.as_view(), name='home'),
    path('signin/', SignInView.as_view(), name='common.signin'),
]