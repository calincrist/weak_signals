from django.core.files import File
from django.shortcuts import render
from rest_framework.parsers import FileUploadParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse

from django.conf import settings

from LocalModules.FileHandlersModule import file_handler
from LocalModules.FileHandlersModule.file_handler import FileHandler
import json

from models import FileModel

import logging
logger = logging.getLogger('root')
FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
logging.basicConfig(format=FORMAT)
logger.setLevel(logging.DEBUG)


class UploadFileView(APIView):
    parser_classes = (FileUploadParser,)

    def post(self, request, filename, format=None):

        if not request.session.session_key:
            print('create session')
            request.session.create()

        try:

            file_name = ''
            if request.FILES['file']:
                myfile = request.FILES['file']
                file_name = 'filename'
                file_handler.upload_file(myfile)

            if not 'filename' in request.session:
                request.session['filename'] = ''

            request.session['filename'] = file_name

            path = settings.MEDIA_ROOT + '/' + request.session['filename']
            if not 'path' in request.session:
                request.session['path'] = path
            request.session['path'] = path


            file = FileModel(name=filename, path=path)
            file.save()




        except (RuntimeError, TypeError, NameError, AttributeError) as e:
            logger.error("Error: {0}".format(e))
            return Response(status=400)

        response = {
            'fileId' : file.file_id
        }

        return Response(response, status=200)

class SourceView(APIView):

    def get(self, request, fileId):

        file = FileModel.objects.get(file_id=fileId)

        fileHandler = FileHandler(file.path)
        response = fileHandler.check_source()

        if not response['data']:
            Response(response, status=404)

        return Response(response, status=200)

class TopicsView(APIView):

    def get(self, request, fileId):

        file = FileModel.objects.get(file_id=fileId)
        fileHandler = FileHandler(file.path)

        response = fileHandler.get_topics()
        return Response(response, status=200)


class SentimentsView(APIView):

    def get(self, request, fileId):

        file = FileModel.objects.get(file_id=fileId)
        fileHandler = FileHandler(file.path)

        response = fileHandler.sentiment_analysis()
        return Response(response, status=200)

class NERView(APIView):

    def get(self, request, fileId):

        file = FileModel.objects.get(file_id=fileId)
        fileHandler = FileHandler(file.path)

        response = fileHandler.ner()
        return Response(response, status=200)
