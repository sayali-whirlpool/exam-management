from rest_framework import serializers
from exam_management_app.models import College

class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = ['id', 'name', 'address', 'registered_by']