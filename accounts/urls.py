from django.urls import path
from .views.auth_views import AccountsList, LoginView, LogoutView, UserSignupView
from .views.teacher_views import TeacherListCreateView, TeacherDetailView

urlpatterns = [
    path('', AccountsList.as_view(), name='accounts'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('teachers/', TeacherListCreateView.as_view(), name='teachers' ),
    path('teachers/<int:pk>', TeacherDetailView.as_view(), name='teacher'),
]
