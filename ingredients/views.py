import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.template import Template
from django.template.loader import get_template, render_to_string
from django.urls import reverse
from django.views import View
from django.views.decorators.csrf import csrf_protect
from django.views.generic import DeleteView, UpdateView, TemplateView, FormView

from .models import Ingredient


# Create your views here.


class IndexView(FormView):
    template_name = "ingredients/index.html"
    model = Ingredient
    successful_template = 'ingredients/successful.html'

    def get(self, request, **kwargs):
        ing = self.model.objects.all()
        total_count = 0
        for i in ing:
            if 'cents' in i.price_per_unit:
                total_count += float(i.price_per_unit.split()[0]) * i.available / 100
            else:
                total_count += float(i.price_per_unit[:-1]) * i.available
        context = {'ingredients': ing, 'total_count': round(total_count, 2)}
        return render(self.request, template_name=self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        return render(request, self.successful_template)

    # def post(self, request, *args, **kwargs):
    #     # decoding bytes from js-fetch request to python-dict
    #     json_data = request.body.decode('utf-8')
    #     data = json.loads(json_data)
    #     template = render_to_string(self.successful_template)
    #     # print(template)
    #     response = {'HtmlPage': template}  # for ok
    #     return JsonResponse(response)


class SuccessfulView(TemplateView):
    template_name = "ingredients/successful.html"
