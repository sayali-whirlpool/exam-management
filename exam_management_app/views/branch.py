from rest_framework import viewsets
from exam_management_app.models import Branch
from exam_management_app.serializers import BranchSerializer

class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer