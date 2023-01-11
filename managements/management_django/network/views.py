from django.shortcuts import render

from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination

from team.models import Team

from .models import Network
from .serializers import NetworkSerializer

class NetworkPagination(PageNumberPagination):
    page_size = 10

class NetworkViewSet(viewsets.ModelViewSet):
    serializer_class = NetworkSerializer
    queryset = Network.objects.all()
    pagination_class = NetworkPagination

    filter_backends = (filters.SearchFilter,)
    search_fields = ('network_install_place', 'network_type', 'network_brand', 'network_name', 'network_name_in_system')


    def get_queryset(self):
        team_name = Team.objects.filter(members__in=[self.request.user]).first()

        return self.queryset.filter(team_name=team_name)
    
    def perform_create(self, serializer):
        team_name = Team.objects.filter(members__in=[self.request.user]).first()

        serializer.save(team_name=team_name, created_by=self.request.user)

class NetworkAllViewSet(viewsets.ModelViewSet):
    serializer_class = NetworkSerializer
    queryset = Network.objects.all()
    pagination_class = NetworkPagination

    filter_backends = (filters.SearchFilter,)
    search_fields = ('network_install_place', 'network_type', 'network_brand', 'network_name', 'network_name_in_system')

