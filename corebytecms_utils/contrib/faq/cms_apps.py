from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import gettext as _


class FAQAppHook(CMSApp):
    app_name = "corebytecms_utils.contrib.faq"
    name = _("FAQ page")
    _urls = [f"{app_name}.urls"]

    def get_urls(self, page=None, language=None, **kwargs):
        return [
            f"{self.app_name}.urls"
        ]


apphook_pool.register(FAQAppHook)

