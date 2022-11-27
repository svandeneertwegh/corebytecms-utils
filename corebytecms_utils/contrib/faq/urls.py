from django.urls import re_path

from .views import FAQView

app_name = 'faq'

urlpatterns = [
    re_path(r'^$', FAQView.as_view(), name='faq_list'),
]
