from django.urls import path
from .views.auth_views import AccountsList, LoginView, LogoutView

urlpatterns = [
    path('', AccountsList.as_view(), name='accounts'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]