from rest_framework import viewsets
from exam_management_app.models import College
from exam_management_app.serializers import CollegeSerializer

class CollegeViewSet(viewsets.ModelViewSet):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer