from django.urls import re_path

from .views import TeamPageView

app_name = 'team'

urlpatterns = [
    re_path(r'^$', TeamPageView.as_view(), name='team_list'),
    # re_path(r'^archive/$', archive_view),
]
