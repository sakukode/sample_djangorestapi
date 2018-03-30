from rest_framework import serializers

from user.serializers import UserSerializer
from .models import Courses


class CoursesSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(required=False)

    class Meta:
        model = Courses
        fields = ('__all__')

