from django.shortcuts import render
from .models import Driver, Result, Race, Team, Standing
from django.http import HttpResponse, HttpResponseRedirect, Http404
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import *


def driver_list(request):
    drivers = Driver.objects.all()
    return render(request, 'racechart/driver_list.html', {'drivers': drivers})

def driver_detail(request, pk):
    driver = Driver.objects.get(id=pk)
    return render(request, 'racechart/driver_detail.html', {'driver': driver})

def team_list(request):
    teams = Team.objects.all()
    return render(request, 'racechart/team_list.html', {'teams': teams})

def team_detail(request, pk):
    team = Team.objects.get(id=pk)
    return render(request, 'racechart/team_detail.html', {'team': team})

def race_list(request):
    races = Race.objects.all()
    return render(request, 'racechart/race_list.html', {'races': races})

def race_detail(request, pk):
    race = Race.objects.get(id=pk)
    return render(request, 'racechart/race_detail.html', {'race': race})

def graphs(request):
    standings = Standing.objects.all()
    results = Result.objects.all()
    return render(request, 'racechart/graph.html', {'standings': standings, 'results': results})

def standing_list(request):
    standings = Standing.objects.all()
    return render(request, 'racechart/static_page.html', {'standings': standings})

def standing_detail(request, pk):
    standings = Standing.objects.get(id=pk)
    return render(request, 'racechart/static_page.html', {'standing': standing})

def result_list(request):
    results = Result.objects.all()
    return render(request, 'racechart/result_list.html', {'results': results})

def result_detail(request, pk):
    print('hit function')
    result = Result.objects.get(id=pk)
    return render(request, {'result': result})

def error_404(request, exception):
        data = {}
        return render(request,'racechart/error_404.html', data)

def error_500(request, exception):
        data = {}
        return render(request,'racechart/error_500.html', data)


class RaceList(generics.ListCreateAPIView):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer

class RaceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer

class TeamList(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class StandingList(generics.ListCreateAPIView):
    queryset = Standing.objects.all()
    serializer_class = StandingSerializer

class StandingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Standing.objects.all()
    serializer_class = StandingSerializer

class ResultList(generics.ListCreateAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

class ResultDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer


class DriverList(generics.ListCreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

class DriverDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
