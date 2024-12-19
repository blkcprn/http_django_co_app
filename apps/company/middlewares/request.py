from django.http import HttpRequest


class CountRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.requests_count = 0
        self.responses_count = 0
        self.exeptions_count = 0
    
    def __call__(self, request: HttpRequest):
        self.requests_count += 1
        print("request count", self.requests_count)
        response = self.get_response(request)
        self.responses_count += 1
        print("response count", self.responses_count)

        return response
    
    def process_exception(self, request: HttpRequest, exception: Exception):
        self.exeptions_count += 1
        print("exception count", self.exeptions_count)