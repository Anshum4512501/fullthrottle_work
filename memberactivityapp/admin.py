from django.contrib import admin
from .models import Members,Activity_Periods
# Register your models here.
admin.site.register(Members)
admin.site.register(Activity_Periods)

class MembersAdmin(admin.ModelAdmin):
    class Meta:
        fields = ['__all__']