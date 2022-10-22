from django.contrib import admin
from .models import iletisim, yazilar
# Register your models here.

class messagesAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    list_display_links = ['name']
    
    class Meta:
        model = iletisim

class yaziAdmin(admin.ModelAdmin):
    list_display = ['baslik']
    list_filter = ['baslik']
    list_display_links = ['baslik']
    
    class Meta:
        model = yazilar
    
admin.site.register(iletisim, messagesAdmin)
admin.site.register(yazilar, yaziAdmin)