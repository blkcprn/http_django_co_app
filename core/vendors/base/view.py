from django.views import View
from django.views.generic import TemplateView
from ..mixins.view import (
    ContextDataMixin,
    ProtectViewMixin,
)


class BaseView(ContextDataMixin, View):
    pass


class BaseTemplateView(ContextDataMixin, TemplateView):
    pass


class BaseProtectView(ContextDataMixin, ProtectViewMixin, View):
    pass


class BaseProtectTemplateView(ContextDataMixin, ProtectViewMixin, TemplateView):
    pass