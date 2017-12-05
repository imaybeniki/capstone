from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import JsonResponse

from math import sin, cos, sqrt, atan2, radians

import psycopg2
from capstoneSite.settings import DATABASES
from .forms import LoginForm
import algorithm

useDatabase = True

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        # Row = Location name, lat, long, weight, capacity, flag
        rows = [
            [1, 'Location 1', 'City', 'State', 'zip', -25.363, 131.044, 50, 10, 'weight', 'R'],
            [2, 'Location 2', 'City', 'State', 'zip', -24.363, 135.044, 50, 40, 'weight', 'G']
        ]

        try:
            connectionString = "dbname='%(NAME)s' user='%(USER)s' host='%(HOST)s' password='%(PASSWORD)s'" % DATABASES['default']
            connection = psycopg2.connect(connectionString)

            cur = connection.cursor()
            cur.execute('select * from LOCATIONS')
            if useDatabase:
                rows = cur.fetchall()
            # Clean rows TODO
            for row in rows:
                print(row)
            print('success')
        except Exception as e:
            print(e)

        print(len(rows))
        numberOfRows = len(rows)

        latSum = 0
        longSum = 0

        for row in rows:
            # Add lat
            latSum += row[5]
            # Add Long
            longSum += row[6]
        center = {'lat': latSum / numberOfRows, 'long': longSum / numberOfRows}
        return render(request, 'index.html', {'rows': rows, 'numberOfRows': numberOfRows, 'center': center})

# View for registering a new user
def register(request):
    # If POST
    if request.method == 'POST':
        # Create form instance and populate from request
        form = LoginForm(request.POST)

        if form.is_valid():
            # Create user and login
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            newUser = User.objects.create_user(username, email, password)
            newUser.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect(reverse('homepage'))

    # If GET, create default form
    else:
        form = LoginForm()

    return render(request, 'register.html', {'form': form})

# View for the about page
def about(request):
    return render(request, 'about.html')

def profile(request):
    return render(request, 'profile.html')

# View for getting points
def get_points(request):
    id = request.GET.get('id', None)
    points_data = algorithm.talkToSite(id)

    return JsonResponse(points_data)

# View for updating user's points
def update_user_points(request):
    points = int(request.GET.get('points', None))

    # Distance calc
    lat1 = request.GET.get('lat1', None)
    lat2 = request.GET.get('lat2', None)
    lng1 = request.GET.get('long1', None)
    lng2 = request.GET.get('long2', None)

    if request.user.is_authenticated():
        # Add points
        request.user.profile.points += points
        message = 'You earned ' + str(points) + ' points!'

        rlat1 = radians(float(lat1))
        rlat2 = radians(float(lat2))

        rlng1 = radians(float(lng1))
        rlng2 = radians(float(lng2))

        dlat = rlat1 - rlat2
        dlng = rlng1 - rlng2

        getA = sin(dlat / 2)**2 + cos(rlat2) * sin(dlng / 2) ** 2
        getC = 2 * atan2(sqrt(getA), sqrt(1 - getA))

        distance = 6373.0 * getC

        request.user.profile.distance += distance
        request.user.save()

    else:
        message = 'You could have earned ' + str(points) + ' points... Please login or register!'

    response = {
        'message': message
    }

    return JsonResponse(response)

