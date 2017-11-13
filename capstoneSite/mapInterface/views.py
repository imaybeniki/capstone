from django.shortcuts import render
from django.views.generic import TemplateView

import psycopg2
from capstoneSite.settings import DATABASES

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
			print('success')
		except Exception as e:
			print(e)

		numberOfRows = len(rows)

		latSum = 0
		longSum = 0

		for row in rows:
			# Add lat
			latSum += row[5]
			# Add Long
			longSum += row[6]

		center = {'lat': latSum / numberOfRows,
				  'long': longSum / numberOfRows}

		print(rows)
		return render(request, 'index.html', {'rows': rows, 'numberOfRows': numberOfRows, 'center': center})
