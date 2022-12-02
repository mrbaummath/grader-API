from rest_framework.permissions import DjangoModelPermissions
from rest_framework import generics, status
from ..serializers import GradeSerializer, CourseGradesByStudentSerializer, StudentGradeSerializer
from rest_framework.response import Response
from classes.models.course import Course
from ..models.grade import Grade
from accounts.models.student import Student
from ..models.assignment import Assignment
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404


#list / create grades for a given assignment
# if creating, client will provide all information 
# /gradebook/<assignment_id>/grades/
class AssignmentGradesListCreateView(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]
    serializer_class = GradeSerializer
    
    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.is_teacher:
            assignment_id = self.kwargs["assignment_id"]
            return Grade.objects.filter(assignment=assignment_id)

#view for teacher to update, read, destroy a grade which they assigned. Can also be used by a student for GET only
# /gradebook/grades/<grade_id>
class GradeRUDView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissions]
    serializer_class = GradeSerializer
    
    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Grade.objects.all()
        elif user.is_teacher:
            return Grade.objects.filter(assignment__teacher = user.teacher.id)
        elif user.is_student and self.request.method == "POST":
            return Grade.objects.filter(student=user.student.id)
        else:
            return None

#view for student to see all of their grades
#/gradebook/mygrades/
class StudentGradesView(generics.ListAPIView):
    permission_classes = [DjangoModelPermissions]
    serializer_class = StudentGradeSerializer
    
    def get_queryset(self):
        user = self.request.user
        if user.is_student:
            return Grade.objects.filter(student = user.student.id)
        else:
            return None

class CourseGradesByStudentView(generics.ListAPIView):
    serializer_class = CourseGradesByStudentSerializer
    
    def get_queryset(self):
        course_id = self.kwargs["course_id"]
        return Course.objects.get(pk=course_id).students()
    
    def get(self, request, course_id):
        assignments = Assignment.objects.filter(course=self.kwargs["course_id"]).values("id", "name")
        return Response({"assignments": assignments, "grades":self.list(request).data})

class UpdateGradesFromTable(APIView):
    
    def patch(self, request):
        user = request.user
        updates = request.data['update_pairs']
        updated = []
        
        for update in updates:
            grade = get_object_or_404(Grade, pk=update["gradeId"])
            data = {"value": update["newGradeValue"]}
            serializer = GradeSerializer(grade, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                updated.append(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'updated_grades': updates}, status=status.HTTP_200_OK)
            