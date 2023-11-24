from django.urls import path, include, re_path
from random_digits.views import HomePage, AuthorizationPage, UserLogin



urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('authorization/', AuthorizationPage.as_view(), name='authorization'),
    path('login/', UserLogin.as_view(), name='login'),
]