#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.files import File
import docx2txt
from LocalModules.ApiClientModule import api_client
from LocalModules.Topics.topics import *
from LocalModules.NER import ner

import logging

logger = logging.getLogger('root')
FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
logging.basicConfig(format=FORMAT)
logger.setLevel(logging.DEBUG)


def run_command(command):
    p = Popen(command,
                     stdout=PIPE, stderr=STDOUT,
                     shell=True)
    return p.stdout
    # return iter(.read, b'')


class FileHandler(object):
    def __init__(self, file_path):

        self.path = file_path
        with open(file_path, 'r') as f:
            self.file_object = File(f)
            self.filename = self.file_object.name
            self.big_response = {}
            self.read_contents()

    def handle_file(self):
        '''Check by content-type and treat accordingly.'''
        if not self.filename.lower().endswith(('.txt','.doc', '.docx', '.py')):
            return { 'status' : 'ERROR',
                     'message' : 'Wrong file type.'}

        self.read_contents()

    def sentiment_analysis(self):

        response_content = api_client.sentiments('simpleSA', self.contents)
        print(response_content)

        response = []
        try:
            response.append(response_content)
        except (RuntimeError, TypeError, NameError) as e:
            logger.error("Error: {0}".format(e))
            pass

        if response == []:
            return {'status': 'ERROR',
                    'status_code': 404,
                    'message': 'No sentiments found :(',
                    'data': response
                    }

        return {'status': 'OK',
                'status_code': 200,
                'message': 'These are possible sentiments.',
                'data': [response[0]]
                }


    def ner(self):
        response = ner.get_ner([self.contents])

        if response:
            return {'status': 'OK',
                    'status_code': 200,
                    'message': 'These are possible news sources.',
                    'data': response
                    }

        return {'status': 'ERROR',
                'status_code': 404,
                'message': 'No NER found :(',
                }


    def read_contents(self):
        contents = ''

        if self.filename.lower().endswith('.txt'):
            self.contents = self.read_txt()

        if self.filename.lower().endswith(('.docx', '.doc')):
            self.contents = self.read_docx()

    def read_docx(self):
        return docx2txt.process(self.path)

    def read_txt(self):
        if not self.file_object.multiple_chunks():
            with open(self.path, 'r') as f:
                return f.read()


    def check_source(self):
        response_content = api_client.check_source(self.contents)
        response_title = api_client.check_source(self.filename)
        response = []

        print(response_content)
        print(response_title)

        try:
            if response_title or response_content:
                response = {x['Url']:x for x in response_content + response_title}.values()
        except (RuntimeError, TypeError, NameError) as e:
            logger.error("Error: {0}".format(e))
            pass

        if response == []:
            return {'status': 'ERROR',
                    'status_code': 404,
                    'message': 'No sources found :(',
                    'data': response
                    }

        return {'status': 'OK',
                'status_code': 200,
                'message': 'These are possible news sources.',
                'data': [response[0]]
                }

    def get_topics(self):
        response = retrieve_topics(self.contents)

        if response:
            return {'status': 'OK',
                    'status_code': 200,
                    'message': 'Here are the topics.',
                    'data': response
                    }

        return {'status': 'ERROR',
                'status_code': 404,
                'message': 'No topics found :(',
                }



def upload_file(file):
    path = settings.MEDIA_ROOT + '/' + file.name
    destination = open(path, 'wb+')
    print(destination)
    for chunk in file.chunks():
        destination.write(chunk)
    destination.close()

    with open(path, 'r') as fin:
        data = fin.read().splitlines(True)
    with open(path, 'w') as fout:
        fout.writelines(data[4:])

    import os
    with open(path, 'r+') as f:
      f.seek(0, os.SEEK_END)
      while f.tell() and f.read(1) != '\n':
        f.seek(-2, os.SEEK_CUR)
      f.truncate()
