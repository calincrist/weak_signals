from django.shortcuts import render

from LocalModules.FileHandlersModule import file_handler


def index(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']

        response = file_handler.handle_file(myfile)

        return render(request, 'index.html', {
            'uploaded_file_url': myfile.name,
            'status' : response['status'],
            'message': response['message']
        })

    return render(request, 'index.html')

