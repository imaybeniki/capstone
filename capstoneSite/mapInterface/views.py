from django.shortcuts import render
from django.views.generic import TemplateView

import psycopg2
from capstoneSite.settings import DATABASES

# Create your views here.
class HomePageView(TemplateView):
	def get(self, request, **kwargs):
		successFlag = 'SUCCEED'
		try:
			connectionString = "dbname='%(NAME)s' user='%(USER)s' host='%(HOST)s' password='%(PASSWORD)s'" % DATABASES['default']
			connection = psycopg2.connect(connectionString)
			print('success')
		except:
			successFlag = 'FAILED'
			print('fail')
		
		return render(request, 'index.html', {'testVar': successFlag})
