import os

from django.conf import settings
from django.http import HttpResponse
from django.views.generic import View



class IndexView(View):
    """Render main page."""

    def get(self, request):
        """Return html for main application page."""

        abspath = open(os.path.join(os.path.dirname(settings.BASE_DIR),"master/www/index.html"), 'r')
       # abspath = os.path.join(os.path.dirname(settings.BASE_DIR),"master/www/index.html")
        return HttpResponse(content=abspath.read())
