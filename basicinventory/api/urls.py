from django.conf.urls import url
from api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^machines/(?P<serial>.+)/$', views.MachineDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
