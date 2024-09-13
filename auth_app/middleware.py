from django.shortcuts import redirect
from django.urls import reverse

class ForcePasswordChangeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and not request.user.has_usable_password():
            if request.path != reverse('password_change'):
                return redirect('password_change')
        return self.get_response(request)