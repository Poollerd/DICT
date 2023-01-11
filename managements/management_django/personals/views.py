from django.shortcuts import render

from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination


from .models import Personal
from .serializers import PersonalSerializer

class PersonalPagination(PageNumberPagination):
    page_size = 10

class PersonalViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalSerializer
    queryset = Personal.objects.all()
    pagination_class = PersonalPagination

    filter_backends = (filters.SearchFilter,)
    search_fields = ('rank', 'first_name', 'last_name', 'mobile', 'phone_rtaf', 'department')

    def get_queryset(self):
        return self.queryset.filter()
        # return self.queryset.filter(created_by=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)