#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.files.storage import FileSystemStorage
import docx2txt
from subprocess import Popen, PIPE, STDOUT

import json

from LocalModules.ApiClientModule import api_client
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
    def __init__(self, file):
        self.fs = FileSystemStorage()
        self.file_object = file
        self.filename = self.fs.save(file.name, file)
        self.big_response = {}

    def handle_file(self):
        '''Check by content-type and treat accordingly.'''
        if not self.filename.lower().endswith(('.txt','.doc', '.docx', '.py')):
            return { 'status' : 'ERROR',
                     'message' : 'Wrong file type.'}

        self.read_contents()
        source_content = self.check_source()
        self.sentiment_analysis()
        entities = ner.get_ner(self.contents)
        polarity = self.sentiment_analysis()
        resp_polarity = {
            'status': 'OK',
            'data': polarity['polarity'].upper()
        }

        return {'status': 'OK',
                'message': 'You successfully uploaded the input file.'}, source_content, entities, resp_polarity


    def sentiment_analysis(self):

        logger.debug('pwd: ')
        logger.debug(run_command('pwd').read())

        logger.debug('ls: ')
        logger.debug(run_command('ls').read())

        cmd = 'java -jar ./LocalModules/ProiectSentA/Five-PointScaleAlgorithm.jar "' + str(self.contents) + '"'

        try:
            sentiment = run_command(cmd).read()
            logger.debug('===========')
            logger.debug(sentiment)
            sentiments = json.loads(sentiment)
            return sentiments
        except (RuntimeError, TypeError, NameError) as e:
            logger.error("Error: {0}".format(e))
            return {}


    def read_contents(self):
        contents = ''

        if self.filename.lower().endswith('.txt'):
            self.contents = self.read_txt()

        if self.filename.lower().endswith(('.docx', '.doc')):
            self.contents = self.read_docx()

    def read_docx(self):
        return docx2txt.process(self.fs.path(self.file_object))

    def read_txt(self):
        if not self.file_object.multiple_chunks():
            with open(self.fs.path(self.file_object), 'r') as f:
                return f.read()


    def check_source(self):
        response_content = api_client.check_source(self.contents)
        response_title = (api_client.check_source(self.filename))
        response = []

        try:
            response = {x['Url']:x for x in response_content + response_title}.values()
        except (RuntimeError, TypeError, NameError) as e:
            logger.error("Error: {0}".format(e))
            pass

        if response == []:
            return {'status': 'ERROR',
                    'message': 'No sources found :(',
                    'data': response
                    }

        return {'status': 'OK',
                'message': 'These are possible news sources.',
                'data': [response[0]]
                }



def handle_file(file):
    return FileHandler(file).handle_file()
