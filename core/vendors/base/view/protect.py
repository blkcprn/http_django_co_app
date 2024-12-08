from django.views import View
from ...mixins.view import (
    ContextDataMixin, 
    ProtectViewMixin,
)
from django.views.generic import (
    TemplateView,
)


class BaseProtectView(ContextDataMixin, ProtectViewMixin, View):
    pass


class BaseProtectTemplateView(ContextDataMixin, ProtectViewMixin, TemplateView):
    pass