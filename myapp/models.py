from django.db import models

# Create your models here.
class Job(models.Model):
    job_title = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    description = models.TextField()
    openings = models.PositiveIntegerField()
    location = models.CharField(max_length=100)
    contact_email = models.EmailField()
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"