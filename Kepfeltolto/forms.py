from django.forms import forms, ModelForm
from .models import Picture


class UploadFileForm(forms.Form):
    file = forms.FileField(label="Válassz ki egy képet")


class FileForm(ModelForm):
    class Meta:
        model = Picture
        fields = ['file_name', 'image', 'visibility']