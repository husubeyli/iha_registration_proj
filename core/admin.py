from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin
from core import models as core_models


admin.site.register(core_models.IHA)
admin.site.register(core_models.CategoryIHA)
admin.site.register(core_models.Marka)

