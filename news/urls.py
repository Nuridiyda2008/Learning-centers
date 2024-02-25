from django.urls import path
from .views import  news_detail, news_list_View, NewsCreateView, NewsUpdateView, NewsDeleteView

urlpatterns = [
    path('', news_list_View, name='all_news_list'),
    path('news/<int:id>/', news_detail, name='news_detail_page'),
    path('create/', NewsCreateView.as_view(), name='news_create'),
    path('news/<pk>/edit/', NewsUpdateView.as_view(), name='news_update'),
    path('news/<pk>/delete/', NewsDeleteView.as_view(), name='news_delete')
]