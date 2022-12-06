from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin
from core import models as core_models



# admin.site.register(CalculateTable)
# admin.site.register(SatisHesabat)

admin.site.register(core_models.IHA)
admin.site.register(core_models.CategoryIHA)
admin.site.register(core_models.Marka)



# class CalculateTableResource(resources.ModelResource):
#     class Meta:
#         model = CalculateTable
#         fields = ('satis_hesabat__fullname', 'month', 'amount', 'pay_date', 'status',)
        
# @admin.register(CalculateTable) 
# class CalculateTableImportExport(ImportExportActionModelAdmin): 
#     resource_class = CalculateTableResource

# class CalculateTableTabularInline(admin.TabularInline):
#     model = CalculateTable
#     fields = ('month', 'pay_date', 'amount', 'status',)
#     # read
#     extra = 0
    
    
# class SatisHesabatAdmin(admin.ModelAdmin):
    
#     list_display = ('fullname', 'product', 'price', 'created_at',)
#     list_filter = ('created_at', 'fullname', 'product',)
#     inlines = [CalculateTableTabularInline,]
#     search_fields = ('fullname', 'product',)
#     # actions = ('credit_date_export_to_excel_action',)
#     ordering = ('-created_at',)
#     date_hierarchy = 'created_at'
    
    
#     # def credit_date_export_to_excel_action(self, queryset):
#     #     pass

#     # credit_date_export_to_excel_action.short_description = 'Odeme cedvelini skan edin'
    
# admin.site.register(SatisHesabat, SatisHesabatAdmin)
