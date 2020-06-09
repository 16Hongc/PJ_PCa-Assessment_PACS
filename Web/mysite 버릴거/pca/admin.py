from django.contrib import admin
from pca.models import *


# Register your models here.
# admin.site.register(patient_info)
# admin.site.register(treatment_list)


# 06.08 수정본

@admin.register(patient_info)
class patient_info_Admin(admin.ModelAdmin):
    list_display = ['patient_id', 'name', 'birth_date', 'address', 'phone_number']
    list_display_links = ['patient_id', 'name', 'birth_date', 'address', 'phone_number']

@admin.register(treatment_list)
class treatment_list_Admin(admin.ModelAdmin):
    list_display = ['patient_id', 'visit_date']
    list_display_links = ['patient_id', 'visit_date']