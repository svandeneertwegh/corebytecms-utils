from django.conf import settings
from django.contrib.sites.models import Site

from .models import SiteConfiguration


def config_settings(request):
    schema = getattr(settings, "META_SITE_PROTOCOL", "http")

    if schema == 'https':
        schem = 'https://'
    else:
        schem = 'http://'

    canonical_url = request.build_absolute_uri(request.path)

    site_url = schem + Site.objects.first().domain

    return {'conf': SiteConfiguration.get_solo(),
            'canonical_url': canonical_url,
            'site_url': site_url}
