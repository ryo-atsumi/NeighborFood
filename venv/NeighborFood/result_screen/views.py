from django.shortcuts import render
from django.views.generic import TemplateView
from opening_screen.models import Result
from django.views import generic


# Create your views here.

#ListViewとページング機能を使用するための定義
class ResultList(generic.ListView):
    model = Result
    template_name = 'result_screen/result_list.html'
    paginate_by = 30 #ページング単位を指定