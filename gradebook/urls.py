from django.urls import path
from .views.assignment_views import AssignmentListCreateView, AssignmentRUDView, StudentAssignmentView
from .views.grade_views import AssignmentGradesListCreateView, GradeRUDView, StudentGradesView, CourseGradesByStudentView, UpdateGradesFromTable

urlpatterns = [
    path("assignments/<int:course_id>/", AssignmentListCreateView.as_view(), name='assignments'),
    path("assignments/update/<int:pk>/", AssignmentRUDView.as_view(), name="assignment"),
    path("assignments/student/", StudentAssignmentView.as_view()),
    path("assignments/<int:assignment_id>/grades/", AssignmentGradesListCreateView.as_view(), name='grades'),
    path("grades/<int:pk>/", GradeRUDView.as_view(), name='teacher_grade'),
    path("mygrades/", StudentGradesView.as_view(), name='student_grades'),
    path("courses/<int:course_id>/", CourseGradesByStudentView.as_view(), name='course_grades'),
    path("grades/updatemany/", UpdateGradesFromTable.as_view(), name='update_table' ),
    
]