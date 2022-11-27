from cms.admin.placeholderadmin import PlaceholderAdminMixin
from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _

from .models import Faq


class FaqPluginModel(admin.ModelAdmin):
    list_display = ("question", "answer",)


admin.site.register(Faq, FaqPluginModel)
