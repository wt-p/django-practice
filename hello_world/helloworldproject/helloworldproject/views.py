from django.http import HttpResponse
from django.views.generic import TemplateView

def helloworldfunction(request):
    returnedobjecct = HttpResponse('<h1>hello world</h1>')
    return returnedobjecct

class HelloWorldClass(TemplateView):
    template_name = 'hello.html'