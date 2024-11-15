from django.contrib import admin
from audit.models import DomainPreference, PortScan, Port, Vulnerability

admin.site.register(DomainPreference)
admin.site.register(PortScan)
admin.site.register(Port)
admin.site.register(Vulnerability)