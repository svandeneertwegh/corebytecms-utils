from django.db import models
from django.utils.translation import ugettext_lazy as _
from solo.models import SingletonModel


class SiteConfiguration(SingletonModel):
    site_title = models.CharField(verbose_name=_('Site title'), max_length=255,
                                  blank=True)
    site_author = models.CharField(verbose_name=_('Author'), blank=True,
                                   null=True, max_length=255)

    social_facebook = models.URLField(verbose_name=_('Facebook address'),
                                      blank=True)
    social_twitter = models.URLField(
        verbose_name=_('Twitter address'), blank=True)
    social_linkedin = models.URLField(verbose_name=_('LinkedIn adsreas'),
                                      blank=True)

    mail_address = models.EmailField(verbose_name=_('Email address'), null=True,
                                     blank=True, max_length=255)
    phone = models.CharField(verbose_name=_('Phone number'), null=True,
                             blank=True, max_length=255)

    def __str__(self):
        return self.site_title

    class Meta:
        verbose_name = _('Site configuration')
