from django.db import models


class PersonModel(models.Model):
    person_id = models.CharField(blank = True, max_length=200)
    mini_mode = models.BooleanField(blank = True, default=False)
    
class TaskModel(models.Model):
    personId = models.CharField(max_length=50, blank = True)
    header = models.CharField(max_length=200, blank = True)
    description = models.CharField(max_length=200, blank = True)
    task_date = models.CharField(max_length=20, blank = True)
    task_time = models.CharField(max_length=20, blank = True)
    important = models.BooleanField(blank = True, default=False)
    remind_date = models.CharField(max_length=20, blank = True)
    remind_time = models.CharField(max_length=20, blank = True)
    one_day = models.BooleanField(blank = True, default=False)
    one_hour = models.BooleanField(blank = True, default=False)
    minutes = models.BooleanField(blank = True, default=False)
    pred_del = models.BooleanField(blank = True, default=False)
