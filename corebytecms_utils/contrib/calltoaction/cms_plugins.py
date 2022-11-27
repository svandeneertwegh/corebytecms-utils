# coding: utf-8
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from .models import CallToAction


class CallToActionPlugin(CMSPluginBase):
    model = CallToAction
    name = _("Call to action")
    render_template = 'corebytecms_calltoaction/calltoaction.html'
    cache = True

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        context['obj'] = instance
        return context


plugin_pool.register_plugin(CallToActionPlugin)
