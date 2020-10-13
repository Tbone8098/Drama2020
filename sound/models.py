from django.db import models

# Create your models here.
class LineOfScript(models.Model):
    number = models.DecimalField(max_digits=10, decimal_places=0, blank=False)
    label = models.CharField(max_length=20, blank=True)
    spoken_line = models.TextField(blank=True)
    audio_name = models.CharField(max_length=50, blank=True)
    note_description = models.TextField(blank=True)
    new_scene = models.BooleanField(default=False)
    scene_number = models.PositiveIntegerField(default=0, blank=True)
    highlight = models.BooleanField(default=False)


# Delete from here down

class Scene(models.Model):
    scene_no = models.PositiveIntegerField()
    line_number_start = models.DecimalField(max_digits=10, decimal_places=0,blank=True)


    line_number_end = models.DecimalField(max_digits=10, decimal_places=0,blank=True)

class AudioFile(models.Model):
    name = models.CharField(max_length=50, blank=True)
    file_name = models.FileField(blank=True)
    line_number = models.DecimalField(max_digits=10, decimal_places=0,blank=True)

class Note(models.Model):
    description = models.TextField(blank=True)
    line_number = models.DecimalField(max_digits=10, decimal_places=0,blank=True)

class Script(models.Model):
    script_line = models.TextField()
    line_number = models.DecimalField(max_digits=10, decimal_places=0, blank=True)
    name = models.CharField(max_length=36, blank=True)

class Page(models.Model):
    start_line_number = models.PositiveIntegerField()


