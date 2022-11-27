from django.views.generic import ListView

from .models import Faq


class FAQView(ListView):
    model = Faq
    template_name = 'faq/page.html'
