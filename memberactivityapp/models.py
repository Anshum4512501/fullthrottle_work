import uuid
from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
# Create your models here.
import pytz

class Members(models.Model):
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
    id              = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,unique=True)   
    real_name       = models.CharField(null=True,blank=False,max_length=20)
    tz              = models.CharField(null=True,blank=True,max_length=100,choices=TIMEZONES)

    def __str__(self):
        return self.real_name

    def natural_keys(self):
        return self.real_name

class Activity_Periods(models.Model):
    members         = models.ForeignKey(Members,on_delete=models.CASCADE,related_name='activities')
    start_time      = models.DateTimeField()
    end_time        = models.DateTimeField()    

    class Meta:
        pass
    def __str__(self):
       return str(self.start_time)
