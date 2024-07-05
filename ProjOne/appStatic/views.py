from django.shortcuts import render, redirect
from django.views import View
from .models import FormHelp, InfoNews


class PageStatic(View):
    def get(self, request):
        return render(request, 'appStatic/home/index.html', {
            'news': InfoNews.objects.all()
        })

class PageNew(View):
    def get(self, request, id):
        return render(request, 'appStatic/new/index.html', {
            'info': InfoNews.objects.filter(id=id)
        })
    
# http://127.0.0.1:8000/static_site/new/123
class PageHelp(View):
    def get(self, request):
        return render(request, 'appStatic/help/index.html')

    def post(self, request):
        FormHelp.objects.create(
            name=request.POST['first_name'],
            email=request.POST['email'],
            text=request.POST['text'],
        )
        return redirect('urlPageHelp')
