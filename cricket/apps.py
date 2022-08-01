from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CricketConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cricket'
    verbose_name = _('cricket')
