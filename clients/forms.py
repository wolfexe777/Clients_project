from django.forms.widgets import DateInput
from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['photo'].widget.attrs['class'] = 'form-control-file'

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.cleaned_data['photo']:
            instance.photo = self.cleaned_data['photo']
        if commit:
            instance.save()
        return instance
class SearchForm(forms.Form):
    query = forms.CharField(label='Поиск', max_length=40)

class CustomDateInput(DateInput):
    input_type = 'date'
    format = '%d.%m.%Y'