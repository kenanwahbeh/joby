from django.db import models

# Create your models here.
JOB_TYPE =[
    ('full time', 'Full Time'), 
    ('part time', 'Part Time')
    ]


class Job(models.Model):
    jop_title = models.CharField(max_length=100)
    # location = models.CharField(max_length=100)
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    job_description = models.TextField(max_length=1000)
    job_published_at = models.DateTimeField(auto_now=True)
    job_vacancy = models.IntegerField(default=1)
    job_salary = models.IntegerField(null=True, blank=True)
    job_experience = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.jop_title
