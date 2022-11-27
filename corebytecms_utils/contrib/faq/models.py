from cms.models.pluginmodel import CMSPlugin
from django.db import models
from django.utils.translation import ugettext as _


class Faq(CMSPlugin):
    question = models.CharField(
        _("Question"),
        max_length=255,
    )
    answer = models.TextField(
        _("Answer"),
    )

    def get_page_url(self):
        return self.page.get_absolute_url()

    class Meta:
        verbose_name = _("Faq")
        verbose_name_plural = _('FAQs')

    def __str__(self):
        return f"{self.question}"
