from django.urls import path
from .views.course_views import CoursesView, CourseRUDView

urlpatterns = [
    path("", CoursesView.as_view(), name='courses' ),
    path("<int:pk>/", CourseRUDView.as_view(), name='course'),
]







