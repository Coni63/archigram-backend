from django.db import models
from project.models import Project
from django.db.models import Max

# Create your models here.
class POCModel(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    version = models.IntegerField()
    data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-version']
        unique_together = ['project', 'version']
        indexes = [
            models.Index(fields=['project', '-version']),
        ]

    def save(self, *args, **kwargs):
        if not self.version:
            # Get the max version for this project and increment
            max_version = POCModel.objects.filter(
                project=self.project
            ).aggregate(Max('version'))['version__max']
            self.version = (max_version or 0) + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f"POC {self.project.id} - v{self.version}"