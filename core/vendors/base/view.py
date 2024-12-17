from django.views import View
from django.views.generic import TemplateView
from ..mixins.view import (
    ContextDataMixin,
    ProtectViewMixin,
)


class BaseView(ContextDataMixin, View):
    """Base view class."""
    pass


class BaseTemplateView(ContextDataMixin, TemplateView):
    """Base template view class."""
    pass


class BaseProtectView(ContextDataMixin, ProtectViewMixin, View):
    """Base protect view class."""
    pass


class BaseProtectTemplateView(ContextDataMixin, ProtectViewMixin, TemplateView):
    """Base protect template view class."""
    pass