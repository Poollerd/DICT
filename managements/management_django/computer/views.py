from django.contrib.auth.models import User

from django.shortcuts import render

from rest_framework import viewsets, status, filters
from rest_framework.pagination import PageNumberPagination

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


from team.models import Team

from .models import Computer, Upgradecomputer
from .serializers import ComputerSerializer, UpgradecomputerSerializer

class ComputerPagination(PageNumberPagination):
    page_size = 10

class ComputerViewSet(viewsets.ModelViewSet):
    serializer_class = ComputerSerializer
    queryset = Computer.objects.all()
    pagination_class = ComputerPagination

    filter_backends = (filters.SearchFilter,)
    search_fields = ('computer_install_place', 'computer_type', 'computer_name', 'computer_brand')

    def get_queryset(self):
        team_name = Team.objects.filter(members__in=[self.request.user]).first()

        return self.queryset.filter(team_name=team_name)
    
    def perform_create(self, serializer):
        team_name = Team.objects.filter(members__in=[self.request.user]).first()

        serializer.save(team_name=team_name, created_by=self.request.user)

class ComputerAllViewSet(viewsets.ModelViewSet):
    serializer_class = ComputerSerializer
    queryset = Computer.objects.all()
    pagination_class = ComputerPagination

    # filter_backends = (filters.SearchFilter,)
    # search_fields = ('computer_install_place', 'computer_type', 'computer_name', 'computer_brand')


class UpgradecomputerViewSet(viewsets.ModelViewSet):
    serializer_class = UpgradecomputerSerializer
    queryset = Upgradecomputer.objects.all()

    def get_queryset(self):
        team_name = Team.objects.filter(members__in=[self.request.user]).first()
        computer_id = self.request.GET.get('computer_id')

        return self.queryset.filter(team_name=team_name).filter(computer_id=computer_id)

    def perform_create(self, serializer):

        team_name = Team.objects.filter(members__in=[self.request.user]).first()
        computer_id = self.request.data['computer_id']

        serializer.save(team_name=team_name, created_by=self.request.user, computer_id=computer_id)