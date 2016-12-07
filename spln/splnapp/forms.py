from django import forms


class FileFieldForm(forms.Form):
    """Simple way to upload a file"""
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

