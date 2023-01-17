from django.shortcuts import redirect
from django.views import View

class Index(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return redirect('login')