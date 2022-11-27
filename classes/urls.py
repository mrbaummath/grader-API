from django.urls import path
from .views.course_views import CourseListCreateView, CourseRUDView
from .views.section_views import SectionListCreateView, SectionRUDView, StudentSectionList

urlpatterns = [
    path("", CourseListCreateView.as_view(), name='courses' ),
    path("<int:pk>/", CourseRUDView.as_view(), name='course'),
    path("<int:course_id>/sections/", SectionListCreateView.as_view(), name='course_sections'),
    path("<int:course_id>/sections/<int:pk>", SectionRUDView.as_view(), name='course_sections'),
    path("myclasses/", StudentSectionList.as_view(), name="student_classes")
]







