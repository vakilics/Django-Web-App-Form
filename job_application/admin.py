from django.contrib import admin
from .models import Form

# Enough to just do below code!
#admin.site.register(Form)

# To customize more:
class FormAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "occupation")
    search_fields = ("first_name", "last_name", "email", "occupation")
    list_filter = ("date", "occupation")
    ordering = ("first_name",)
    #ordering = ("-first_name",)  # sort reverse!
    readonly_fields = ("occupation",)
admin.site.register(Form, FormAdmin)
