from django.db import models

class DomainPreference(models.Model):
    name = models.CharField(max_length=255, unique=True)
    ip = models.CharField(max_length=255, blank=True, null=True, unique=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    registration_date = models.DateField(blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)
    dns_servers = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class PortScan(models.Model):
    target = models.ForeignKey(DomainPreference, on_delete=models.CASCADE, blank=True, null=True)
    scan_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"PortScan for {self.target.name}"

class Port(models.Model):
    port_scan = models.ForeignKey(PortScan, on_delete=models.CASCADE)
    service = models.CharField(max_length=255)
    version_service = models.CharField(max_length=255)

    def __str__(self):
        return f"Port {self.service} ({self.version_service})"

class Vulnerability(models.Model):
    port = models.ForeignKey(Port, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    cvss_score  = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return f"Vulnerability: {self.name} (CVSS: {self.cvss_score})"
