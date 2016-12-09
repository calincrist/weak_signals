from django.shortcuts import render

from LocalModules.FileHandlersModule import file_handler


def index(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']

        response_file, response_source, response_ner, response_sent = file_handler.handle_file(myfile)

        response_params = {
            'uploaded_file_url': myfile.name,
            'status' : response_file['status'],
            'message': response_file['message'],

            'status_source': response_source['status'],
            'message_source': response_source['message'],
            'data_source': response_source['data'],

            'status_ner': response_ner['status'],
            'message_ner': response_ner['message'],
            'data_ner': response_ner['data'],

            # 'status_sentiment': response_sent['status'],
            # 'message_sentiment': response_sent['message'],
            'data_sentiment': response_sent['data']
        }

        return render(request, 'index.html', response_params)

    return render(request, 'index.html')
