from django.views.generic import View
from django.shortcuts import render,get_object_or_404
import json
from django.core.serializers import serialize
from .models import Activity_Periods,Members

class SerializeMixin(object):
    model = None
    def serialize(self,*args,**kwargs):
        data = {
            "ok":True,
            "members":[
                
            ]
        }
        obj_list            = self.model.objects.all()
        qs_json             = serialize('json', obj_list)
        json_data           = json.loads(qs_json)
        json_list           = []
        for item in json_data:
            field_data = item['fields']
            json_list.append(data)
            obj = get_object_or_404(self.model,id=item['pk'])
            data.get('members').append({"id":item.get('pk'),"real_name":field_data['real_name'],"tz":field_data['tz'],"activity_period":self.get_activities(obj)})
        json_data = json.dumps(json_list)
        return data

    def get_activities(self,obj):
        qs_json             = serialize('json', obj.activities.all())
        json_data           = json.loads(qs_json)
        activity_json_list           = []    
        for item in json_data:
            field_data  = item['fields']
            activity_json_list.append(field_data)
        return activity_json_list
            