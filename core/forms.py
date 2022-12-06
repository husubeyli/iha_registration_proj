from django import forms
from core.models import IHA



class IHACreateForm(forms.ModelForm):
    class Meta:
        model = IHA
        fields = '__all__'
        exclude = ('slug',)
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'required': True
            }),
            
            'weight': forms.NumberInput(attrs={
                'class': 'form-control',
                'required': True
            }),
            
            'categories': forms.Select(attrs={
                'class': 'form-control',
                'required': True
            }),
            
            'markas': forms.Select(attrs={
                'class': 'form-control',
                'required': True
            }),
        }