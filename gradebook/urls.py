from django.urls import path
from .views.assignment_views import AssignmentListCreateView, AssignmentRUDView, StudentAssignmentView
from .views.grade_views import AssignmentGradesListCreateView, GradeRUDView

urlpatterns = [
    path("assignments/", AssignmentListCreateView.as_view(), name='assignments'),
    path("assignments/<int:pk>", AssignmentRUDView.as_view(), name="assignment"),
    path("assignments/student/", StudentAssignmentView.as_view()),
    path("assignments/<int:assignment_id>/grades/", AssignmentGradesListCreateView.as_view(), name='grades'),
    path("teacher/grades/<int:pk>", GradeRUDView.as_view(), name='teacher_grade')
]