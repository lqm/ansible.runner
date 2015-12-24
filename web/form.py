#!/usr/bin/env python
#coding:utf-8

from projectdb.models import *

class TablesForm(forms.Form):
    models = models.get_models()
    select = forms.ChoiceField(choices=models)