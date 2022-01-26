from django.conf import settings
from django.http import HttpResponse


class HealthCheckMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method in (
            "GET", "HEAD"
        ) and request.path == settings.HEALTH_CHECK_PATH:
            return self.liveliness(request)
        return self.get_response(request)

    def liveliness(self, request):
        return HttpResponse("OK")
