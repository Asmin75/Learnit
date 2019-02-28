from django.db import models

class Course(models.Model):
    title = models.CharField(max_length = 200)
    field = models.CharField(max_length = 200)
    start_date = models.DateTimeField()
    course_description = models.CharField(max_length = 500)
    image = models.ImageField(upload_to="photo")

    def __str__(self):
        return self.title

class Team(models.Model):
    name = models.CharField(max_length = 100)
    position = models.CharField(max_length = 100)
    image = models.ImageField(upload_to="photo", null = True)

    def __str__(self):
        return self.name

