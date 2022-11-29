from django.urls import path
from .views.assignment_views import AssignmentListCreateView, AssignmentRUDView, StudentAssignmentView
from .views.grade_views import AssignmentGradesListCreateView, GradeRUDView, StudentGradesView

urlpatterns = [
    path("assignments/<int:course_id>", AssignmentListCreateView.as_view(), name='assignments'),
    path("assignments/<int:pk>", AssignmentRUDView.as_view(), name="assignment"),
    path("assignments/student/", StudentAssignmentView.as_view()),
    path("assignments/<int:assignment_id>/grades/", AssignmentGradesListCreateView.as_view(), name='grades'),
    path("grades/<int:pk>", GradeRUDView.as_view(), name='teacher_grade'),
    path("gradebook/mygrades/", StudentGradesView.as_view(), name='student_grades')
]