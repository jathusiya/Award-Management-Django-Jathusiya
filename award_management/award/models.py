from django.db import models
from django.contrib.auth.models import User

class School(models.Model):
    id = models.AutoField
    name = models.TextField(null=True)  
    def __str__(self):
        return self.name

class Student(models.Model):
    id = models.AutoField
    fullname = models.TextField(null=True)  
    def __str__(self):
        return self.fullname

class Subject(models.Model):
    id = models.AutoField
    subject = models.TextField(null=True) 
    subject_score = models.IntegerField(null=True) 
    def __str__(self):
        return self.subject,self.subject_score

class Award(models.Model):
    id = models.AutoField
    award = models.TextField(null=True)  
    def __str__(self):
        return self.award

class Answer(models.Model):
    id = models.AutoField
    answer = models.TextField(null=True)  
    def __str__(self):
        return self.answer

class Assessment(models.Model):
    id = models.AutoField
    assessment_name = models.TextField(null=True)  
    def __str__(self):
        return self.assessment_name
    
class Classes(models.Model):
    id = models.AutoField
    classes = models.CharField(max_length=50)  
    def __str__(self):
        return self.classes

class Summary(models.Model):
    id = models.AutoField(primary_key=True)  # Use primary_key=True for AutoField
    school_name = models.TextField(null=True)
    student_id = models.IntegerField()
    class_name = models.CharField(max_length=50)
    subject = models.CharField(max_length=250)
    answer = models.CharField(max_length=250)
    assessment_areas = models.CharField(max_length=255) 
    award = models.CharField(max_length=250)
    sydney_participants = models.IntegerField()
    sydney_percentile = models.DecimalField(max_digits=5, decimal_places=2)  # DecimalField
    correct_answer = models.CharField(max_length=255)
    correct_answer_percentage_per_class = models.DecimalField(max_digits=5, decimal_places=2)  # DecimalField
    participant = models.CharField(max_length=255)
    student_score = models.DecimalField(max_digits=5, decimal_places=2)  # Assuming it's a DecimalField
    year_level = models.CharField(max_length=50)

    def __str__(self):
        return self.correct_answer  # Access the name attribute of the related School model

