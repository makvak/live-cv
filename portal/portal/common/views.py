import json
from django.contrib.auth import (
    authenticate,
    login
)
from django.http import HttpResponse
from django.views.generic import TemplateView

from rest_framework.status import (
    HTTP_200_OK,
    HTTP_401_UNAUTHORIZED
)

class HomeView(TemplateView):
    template_name = 'index.html'


class SignInView(TemplateView):

    template_name = 'common/signin.html'

    def post(self, request, *args, **kwargs):
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            return HttpResponse(json.dumps({'success': True}), status=HTTP_200_OK, content_type='application/json')
        else:
            return HttpResponse(json.dumps({'success': False}), status=HTTP_401_UNAUTHORIZED, content_type='application/json')
