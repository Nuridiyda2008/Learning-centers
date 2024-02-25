from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import  reverse_lazy
from django.views.generic import ListView, TemplateView, UpdateView, DeleteView, CreateView
from .models import News

# Create your views here.


def news_detail(request, id):
    # id ni urniga news yozuldi
    detail_context = get_object_or_404(News, id=id)
    context = {
        "detail_context": detail_context,
    }
    return render(request, 'news/news_detail.html', context)

def news_list_View(request):
    news_list = News.objects.all()
    context = {
        'news_list': news_list,
    }
    return render(request,'news/news_list.html', context)

class NewsUpdateView(UpdateView):
    model = News
    fields = ['title', 'body', 'image']
    template_name = 'crud/news_edit.html'
    success_url = reverse_lazy('all_news_list')

class NewsDeleteView(DeleteView):
    model = News
    template_name = 'crud/news_delete.html'
    success_url = reverse_lazy('all_news_list')

class NewsCreateView(CreateView):
    model = News
    template_name = 'crud/news_create.html'
    fields = ['title','body', 'image', ]
    success_url = reverse_lazy('all_news_list')