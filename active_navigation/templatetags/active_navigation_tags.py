from classytags.core import Tag, Options
from classytags.arguments import Argument
from classytags.helpers import AsTag
from django import template

register = template.Library()

class ActiveTag(AsTag):
    options = Options(
        Argument('request', required=True),
        Argument('url', required=True),
        Argument('active_class', required=False, default='active'),
        'as',
        Argument('variable', required=False, resolve=False)
    )

class Active(ActiveTag):
    def get_value(self, context, request, url, active_class):
        import re

        if re.search(url, request.path):
            return active_class
        return ''

class ActiveExact(ActiveTag):
    def get_value(self, context, request, url, active_class):
        if request.path == url:
            return active_class
        return ''

register.tag(Active)
register.tag(ActiveExact)

class ReverseTag(AsTag):
    options = Options(
        Argument('request', required=True),
        Argument('url_name', required=True),
        Argument('active_class', required=False, default='active'),
        'as',
        Argument('variable', required=False, resolve=False)
    )

class ReverseActive(ReverseTag):
    def get_value(self, context, request, url_name, active_class):
        import re
        from django.core.urlresolvers import reverse

        if re.search(reverse(url_name), request.path):
            return active_class
        return ''


class ReverseActiveExact(ReverseTag):
    def get_value(self, context, request, url_name, active_class):

        from django.core.urlresolvers import reverse

        if request.path == reverse(url_name):
            return active_class
        return ''

register.tag(ReverseActive)
register.tag(ReverseActiveExact)
