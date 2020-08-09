from django.forms import ModelForm
from django import forms
from memberactivityapp.models import Members,Activity_Periods
class MemberCreateForm(ModelForm):
    class Meta:
        model = Members
        fields = ['real_name','tz']


class ActivityCreateForm(ModelForm):
    class Meta:
        model = Activity_Periods
        fields = ['start_time','end_time']
        widgets = {
            'start_time': forms.DateInput(attrs={'class':'datepicker'}),
             'end_time': forms.DateInput(attrs={'class':'datepicker'}),
        }
                