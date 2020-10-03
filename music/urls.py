from django.conf.urls import url
from . import views

# Index of section
urlpatterns = [
    url(r'^$', views.index, name='index'),
]
