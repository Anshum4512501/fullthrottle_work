from django.views.generic import View
from django.shortcuts import render
import json
from django.core.serializers import serialize
from .models import Activity_Periods,Members

class SerializeMixin(object):
    model = None
    def serialize(self,*args,**kwargs):
        obj_list            = self.model.objects.all()
        qs_json             = serialize('json', obj_list,use_natural_foreign_keys=True, fields=['members','start_time','end_time'], indent=4)
        json_data           = json.loads(qs_json)
        json_list           = []
        for item in json_data:
            data = item['fields']
            json_list.append(data)
        json_data = json.dumps(json_list)
        return json_list