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

import logging
logger = logging.getLogger('root')
FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
logging.basicConfig(format=FORMAT)
logger.setLevel(logging.DEBUG)


class UploadFileView(APIView):
    parser_classes = (FileUploadParser,)

    # def options(self, request):
    #     response = {}
    #     response["Access-Control-Allow-Origin"] = "*"
    #     response["Access-Control-Allow-Methods"] = "POST, OPTIONS"
    #     response["Access-Control-Max-Age"] = "1000"
    #     response["Access-Control-Allow-Headers"] = "*"
    #
    #     print('Headers: ' + str(response))
    #
    #     return Response(headers=response, status=200)

    def post(self, request, filename, format=None):

        if not request.session.session_key:
            print('create session')
            request.session.create()

        try:

            file_name = ''
            if request.FILES['file']:
                myfile = request.FILES['file']
                file_name = filename
                file_handler.upload_file(myfile)

            if not 'filename' in request.session:
                request.session['filename'] = ''

            path = settings.MEDIA_ROOT + '/' + request.session['filename']

            request.session['filename'] = file_name
            request.session['path'] = path

        except (RuntimeError, TypeError, NameError, AttributeError) as e:
            logger.error("Error: {0}".format(e))
            return Response(status=400)

        response = {}
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"

        print('Headers: ' + str(response))

        return Response(headers=response, status=204)

class SourceView(APIView):

    def get(self, request):
        path = request.session['path']
        fileHandler = FileHandler(path)
        response = fileHandler.check_source()

        if not response['data']:
            Response(response, status=404)

        return Response(response, status=200)

class TopicsView(APIView):

    def get(self, request):
        path = request.session['path']
        fileHandler = FileHandler(path)

        response = fileHandler.get_topics()
        return Response(response, status=200)


class NERView(APIView):

    def get(self, request):
        path = request.session['path']
        fileHandler = FileHandler(path)

        response = fileHandler.ner()
        return Response(response, status=200)
