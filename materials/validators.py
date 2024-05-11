from urllib.parse import urlparse

from rest_framework.exceptions import ValidationError


class UrlValidator:
    """validate url only from YouTube"""
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        obj = urlparse(value.get(self.field))
        if not obj.hostname == 'www.youtube.com':
            raise ValidationError('Only urls from YouTube allowed')
