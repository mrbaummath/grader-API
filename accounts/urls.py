from django.urls import path
from .views.auth_views import AccountsList, LoginView, LogoutView, SignupView
from .views.teacher_views import TeachersView

urlpatterns = [
    path('', AccountsList.as_view(), name='accounts'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('teachers/', TeachersView.as_view(), name='teachers' )
]
