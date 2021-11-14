from rest_framework import viewsets , permissions
from django.shortcuts import render
from .models import Footballer
from .serializers import FootballSerializer


def madrid_list(request):
    player = Footballer.objects.all().order_by('name')
    return render(request, "players/madrid_list.html", {"players":player})


def madrid_detail(request,slug):
    players = Footballer.objects.get(slug=slug)
    return render(request, "players/madrid_detail.html", {"players": players})


class FootballView(viewsets.ModelViewSet):
    queryset = Footballer.objects.all()
    serializer_class = FootballSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

