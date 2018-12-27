# response cycle
# process_exception() is only executed if a exception occurs inside the view function
# process_template_response() is only executed if there is a template in the response.
# process_response()

# request cycle
# process_request() and process_view() methods.

from django.conf import settings
import requests

class IsAuthorMiddleware(object):
    
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response