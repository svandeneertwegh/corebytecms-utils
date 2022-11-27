from cms.models import CMSPlugin
from cms.models.fields import PageField
from django.db import models
from django.utils.translation import ugettext_lazy as _

CallToActionStyles = (
    ('default', 'Default'),
    ('primary', 'Primary'),
    ('secondary', 'Secondary'),
    ('tertiary', 'Tertiary'),
    ('quaternary', 'Quaternary'),
)


class CallToAction(CMSPlugin):
    title = models.CharField(verbose_name=_('Title'), max_length=255)
    subtitle = models.CharField(verbose_name=_('Subtitle'), max_length=255)

    link_name = models.CharField('Link naam', max_length=255)
    link_page = PageField(
        verbose_name=_('CMS Page'),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    style = models.CharField(choices=CallToActionStyles, default='default',
                             max_length=255)

    featured = models.BooleanField('Featured', default=False)
    animated = models.BooleanField('Animated', default=True)
    borders = models.BooleanField('Borders', default=True)

    class Meta:
        ordering = ['pk']
        verbose_name = _('Call to action')
        verbose_name_plural = _('Call to actions')

    def __str__(self):
        return f'{self.title}'
