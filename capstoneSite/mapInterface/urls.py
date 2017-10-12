from django.conf.urls import url
from mapInterface import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
]