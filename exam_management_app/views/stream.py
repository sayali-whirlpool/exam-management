from rest_framework import viewsets
from exam_management_app.models import Stream
from exam_management_app.serializers import StreamSerializer

class StreamViewSet(viewsets.ModelViewSet):
    queryset = Stream.objects.all()
    serializer_class = StreamSerializer