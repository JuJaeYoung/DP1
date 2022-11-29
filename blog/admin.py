from django.contrib import admin
from .models import Facinfo
from .models import Essay
from .models import Music

#class QuestionAdmin(admin.ModelAdmin):
#    search_fields = ['fTitle']

# Register your models here.
admin.site.register(Facinfo)
admin.site.register(Essay)
admin.site.register(Music)