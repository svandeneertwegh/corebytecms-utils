from django.db import models
from django.utils.translation import gettext as _
from filer.fields.image import FilerImageField


class TeamEmployee(models.Model):
    full_name = models.CharField(verbose_name=_('Full name'), max_length=255)
    function = models.CharField(verbose_name=_('Function'), max_length=255)

    description = models.TextField(verbose_name=_('Description'))

    picture = FilerImageField(verbose_name=_('Picture'), null=True, blank=True,
                            related_name='team_picture',
                            on_delete=models.CASCADE)

    linkedin = models.URLField(blank=True, verbose_name=_('LinkedIn page'))
    twitter = models.URLField(blank=True, verbose_name=_('Twitter page'))
    email = models.EmailField(blank=True, verbose_name=_('Email address'))

    def __str__(self):
        return f"{self.full_name}"

    class Meta:
        verbose_name = _('Employee')
        verbose_name_plural = _('Employees')
