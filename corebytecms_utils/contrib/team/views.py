from django.views.generic import ListView

from .models import TeamEmployee


class TeamPageView(ListView):
    model = TeamEmployee
    template_name = 'team/list.html'
