from django.urls import path
from .views.auth_views import AccountsList, LoginView, LogoutView, UserSignupView
from .views.teacher_views import TeacherListView, TeacherRUDView
from .views.student_views import StudentListCreateView, StudentRUDView

urlpatterns = [
    path('', AccountsList.as_view(), name='accounts'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('teachers/', TeacherListView.as_view(), name='teachers' ),
    path('teachers/<int:pk>', TeacherRUDView.as_view(), name='teacher'),
    path('students/', StudentListCreateView.as_view(), name='teachers' ),
    path('students/<int:pk>', StudentRUDView.as_view(), name='teacher'),
]
