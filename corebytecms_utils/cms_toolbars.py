from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

@toolbar_pool.register
class SiteConfigEditToolbar(CMSToolbar):

    def populate(self):
        menu = self.toolbar.get_or_create_menu(
            key='admin',
            verbose_name=_('Admin'),
            position=1
        )
        config_url = '/admin/corebytecms_modules/siteconfiguration'

        menu.add_modal_item(name=_('Dashboard'),
                            url=reverse('corebytecms_admin:index'))
        if 'corebytecms_utils.contrib.siteconf' in settings.INSTALLED_APPS:
            menu.add_break()
            menu.add_modal_item(_('Site configuration'), url=reverse(
                "admin:siteconf_siteconfiguration_change"))
        menu.add_break()
        menu.add_modal_item(_('Media library'), url='/admin/filer/folder/')
        menu.add_modal_item(_('Filled in forms'),
                            url='/admin/aldryn_forms/formsubmission/')

        if 'corebytecms_utils.contrib.team' in settings.INSTALLED_APPS:
            menu.add_modal_item(
                name=_('Employees'),
                url=reverse("admin:team_teamemployee_changelist")
            )
        if 'corebytecms_utils.contrib.faq' in settings.INSTALLED_APPS:
            menu.add_modal_item(
                name=_('Frequently asked questions'),
                url=reverse("admin:faq_faq_changelist")
            )
