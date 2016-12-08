#!/usr/bin/env python
from django.core.files.storage import FileSystemStorage
import docx2txt
import subprocess
from LocalModules.ApiClientModule import api_client
from LocalModules.NER import ner


def run_command(command):
    p = subprocess.Popen(command,
                     stdout=subprocess.PIPE,
                     shell=True)
    return iter(p.stdout.readline, b'')


class FileHandler(object):
    def __init__(self, file):
        self.fs = FileSystemStorage()
        self.file_object = file
        self.filename = self.fs.save(file.name, file)
        self.big_response = {}
        # self.fs.delete(filename)

    def handle_file(self):
        '''Check by content-type and treat accordingly.'''
        if not self.filename.lower().endswith(('.txt','.doc', '.docx', '.py')):
            return { 'status' : 'ERROR',
                     'message' : 'Wrong file type.'}

        self.read_contents()
        source_content = self.check_source()
        self.sentiment_analysis()
        entities = ner.get_ner(self.contents)

        return {'status': 'OK',
                'message': 'You successfully uploaded the input file.'}, source_content, entities


    def sentiment_analysis(self):
        sentiment = run_command('java -jar ../Five-PointScaleAlgorithm.jar' + self.contents)
        print('---->>')
        print(sentiment)
        print('<<----')

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

        response = {x['Url']:x for x in response_content + response_title}.values()

        if response == []:
            return {'status': 'ERROR',
                    'message': 'No sources found :(',
                    'data': response
                    }

        return {'status': 'OK',
                'message': 'These are possible news sources.',
                'data': response
                }



def handle_file(file):
    return FileHandler(file).handle_file()
