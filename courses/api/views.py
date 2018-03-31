from rest_framework import viewsets, status
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from ..models import Courses
from ..serializers import CoursesSerializer


class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
    filter_backends = {
        DjangoFilterBackend,
        SearchFilter,
    }
    filter_fields = ('title', 'price',)
    search_fields = ('title', 'subtitle', 'price')

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
