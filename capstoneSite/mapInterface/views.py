from django.shortcuts import render
from django.views.generic import TemplateView

import psycopg2
from capstoneSite.settings import DATABASES

# Create your views here.
class HomePageView(TemplateView):
	def get(self, request, **kwargs):
		rows = [
			['Location 1', -25.363, 131.044],
			['Location 2', -24.363, 135.044]
		]
		numberOfRows = len(rows)
		
		latSum = 0
		longSum = 0
		
		for row in rows:
			# Add lat
			latSum += row[1]
			# Add Long
			longSum += row[2]
		
		center = {'lat': latSum / numberOfRows,
					'long': longSum / numberOfRows}
		
		print(center)
		
		try:
			connectionString = "dbname='%(NAME)s' user='%(USER)s' host='%(HOST)s' password='%(PASSWORD)s'" % DATABASES['default']
			connection = psycopg2.connect(connectionString)
			print('success')
		except:
			print('fail')
		
		return render(request, 'index.html', {'rows': rows, 'numberOfRows': numberOfRows, 'center': center})
