#!/usr/bin/env python
from django.core.files.storage import FileSystemStorage

from LocalModules.ApiClientModule import api_client


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
        self.check_source()

        return {'status': 'OK',
                'message': 'You successfully uploaded the input file.'}


    def read_contents(self):
        contents = ''
        if not self.file_object.multiple_chunks():
            with open(self.fs.path(self.file_object), 'r') as f:
                contents = f.read()
        print(contents)

        self.contents = contents

    def check_source(self):
        response = api_client.check_source('Google has confirmed it will hit its target of offsetting 100% of the energy used at its data centres and offices against power from renewable sources.')
        if response == {}:
            return {'status': 'ERROR',
                    'message': 'Could not verify the news sources.'}
        else:
            return {'status': 'OK',
                    'message': 'These are possible news sources.',
                    'data': response
                    }



def handle_file(file):
    return FileHandler(file).handle_file()