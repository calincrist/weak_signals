from django.shortcuts import render

from LocalModules.FileHandlersModule import file_handler


def index(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']

        response_file, response_source, response_ner = file_handler.handle_file(myfile)

        response_params = {
            'uploaded_file_url': myfile.name,
            'status' : response_file['status'],
            'message': response_file['message'],

            'status_source': response_source['status'],
            'message_source': response_source['message'],
            'data_source': response_source['data'],

            'status_ner': response_ner['status'],
            'message_ner': response_ner['message'],
            'data_ner': response_ner['data']
        }

        print(response_params)

        return render(request, 'index.html', response_params)

    return render(request, 'index.html')
