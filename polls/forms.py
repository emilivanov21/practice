from django import forms
from .models import Deepthought
 
class deepform(forms.ModelForm):
    class Meta:
        model = Deepthought
        fields='__all__' 
            