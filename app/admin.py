from django.contrib import admin


from .models import TestSerializerModel
from .views import TestParserModel

admin.site.register(TestSerializerModel)
admin.site.register(TestParserModel)
