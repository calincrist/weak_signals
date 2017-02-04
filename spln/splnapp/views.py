from django.core.files import File
from django.shortcuts import render
from rest_framework.parsers import FileUploadParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from django.conf import settings

from LocalModules.FileHandlersModule import file_handler
from LocalModules.FileHandlersModule.file_handler import FileHandler

import logging
logger = logging.getLogger('root')
FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
logging.basicConfig(format=FORMAT)
logger.setLevel(logging.DEBUG)

class UploadFileView(APIView):
    parser_classes = (FileUploadParser,)

    def put(self, request, filename, format=None):

        if not request.session.session_key:
            print('create session')
            request.session.create()

        try:

            file_name = ''
            if request.FILES['file']:
                myfile = request.FILES['file']
                file_name = filename
                file_handler.upload_file(myfile)

            # if not 'filename' in request.session:
            request.session['filename'] = file_name
            # else:
            #     print(file_name + ' already in session.')

        except (RuntimeError, TypeError, NameError, AttributeError) as e:
            logger.error("Error: {0}".format(e))
            return Response(status=400)

        # response_file, response_source, response_ner, response_sent = file_handler.handle_file(file_obj)
        # response_params = {
        #     'uploaded_file_url': filename,
        #     'status': response_file['status'],
        #     'message': response_file['message'],
        #
        #     'status_source': response_source['status'],
        #     'message_source': response_source['message'],
        #     'data_source': response_source['data'],
        #
        #     'status_ner': response_ner['status'],
        #     'message_ner': response_ner['message'],
        #     'data_ner': response_ner['data'],
        #
        #     'status_sentiment': response_sent['status'],
        #     # 'message_sentiment': response_sent['message'],
        #     'data_sentiment': response_sent['data']
        # }


        # return Response(response_params, status=204)
        return Response(status=204)

class SourceView(APIView):

    def get(self, request):

        path = settings.MEDIA_ROOT + '/' + request.session['filename']
        file_handler = FileHandler(path)
        response = file_handler.check_source()

        return Response(response, status=200)
