from django.conf.urls import url
from django.contrib import admin

from views import UploadFileView, SourceView, TopicsView, NERView, SentimentsView
from . import views

urlpatterns = [
    # url(r'^$', views.index),
    url(r'^upload/(?P<filename>[^/]+)/$', UploadFileView.as_view()),
    url(r'source/(?P<fileId>[^/]+)/$', SourceView.as_view()),
    url(r'topics/(?P<fileId>[^/]+)/$', TopicsView.as_view()),
    url(r'ner/(?P<fileId>[^/]+)/$', NERView.as_view()),
    url(r'sentiments/(?P<fileId>[^/]+)/$', SentimentsView.as_view())
]
