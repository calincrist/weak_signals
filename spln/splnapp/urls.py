from django.conf.urls import url
from django.contrib import admin

from views import UploadFileView, SourceView, TopicsView
from . import views

urlpatterns = [
    # url(r'^$', views.index),
    url(r'^upload/(?P<filename>[^/]+)$', UploadFileView.as_view()),
    url(r'source/$', SourceView.as_view()),
    url(r'topics/$', TopicsView.as_view()),
]