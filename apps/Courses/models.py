from django.db import models

class basicValidation(models.Manager):
    def basic_validation(self, postData):
        errors = {}
        if len(postData['coursename']) < 5:
            errors['coursename'] = "The course name must be at least 5 characters long."
        if len(postData['coursedesc']) < 15:
            errors['coursedesc'] = "The description must be at least 15 characters long."
        return errors

class Courses(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = basicValidation()
class Descriptions(models.Model):
    desc = models.TextField()
    course = models.OneToOneField(Courses, on_delete=models.CASCADE, related_name="course_desc")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = basicValidation()

class Comments(models.Model):
    user = models.CharField(max_length=100)
    text = models.TextField()
    course_comment = models.ForeignKey(Courses, related_name="comments", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = basicValidation()

