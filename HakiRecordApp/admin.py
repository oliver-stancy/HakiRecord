from django.contrib import admin
from .models import Statement,Contact

class StatementAdmin(admin.ModelAdmin):
    list_display = ( 'Last_Name', 'ID_Number', 'incident_type', 'incident_location','incident_date')
    search_fields = ('Last_Name', 'ID_Number', 'incident_location')
    list_filter = ('recorded_at',)

admin.site.register(Statement, StatementAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('contact_name', 'contact_email')
    search_fields = ('contact_name', 'contact_email')

admin.site.register(Contact,ContactAdmin)






# Register your models here.



# Register your models here.
