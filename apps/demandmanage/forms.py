__author__ = 'zaxlct'
__date__ = '2017/4/6 下午12:14'

import re

from django import forms
from .models import ImportFile


class FileFieldForm(forms.Form):
    # price = forms.CharField(required=True, min_length=2, max_length=20)
    
    class Meta:
        model = ImportFile
        fields = ['upload_file', 'upload_time', 'editor']

