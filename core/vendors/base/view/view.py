from django.views import View
from ...mixins.view import ContextDataMixin
from django.views.generic import (
    TemplateView,
)


class BaseView(ContextDataMixin, View):
    pass


class BaseTemplateView(ContextDataMixin, TemplateView):
    pass