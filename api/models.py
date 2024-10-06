from django.db import models
from django.utils import timezone

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class User(TimeStampedModel):
    ROLE_CHOICES = (('free', 'Free'), ('premium', 'Premium'))
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    signup_date = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(null=True, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return self.email

class Skill(TimeStampedModel):
    skill_name = models.CharField(max_length=255)
    skill_category = models.CharField(max_length=255)
    
    def __str__(self):
        return self.skill_name

class Profile(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_name = models.CharField(max_length=255)

    def __str__(self):
        return self.profile_name

class ProfileSkill(TimeStampedModel):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    #proficiency = models.CharField(max_length=20, choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')])
    
    def __str__(self):
        return self.skill.skill_name

class Resume(TimeStampedModel):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    last_modified = models.DateTimeField(auto_now=True)
    is_template = models.BooleanField(default=False)
    template_type = models.CharField(max_length=50, choices=[('basic', 'Basic'), ('modern', 'Modern'), ('professional', 'Professional')])

class Experience(TimeStampedModel):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    present = models.BooleanField(default=False)

class Education(TimeStampedModel):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    college_name = models.CharField(max_length=255)
    university_name = models.CharField(max_length=255)
    cgpa = models.FloatField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    present = models.BooleanField(default=False)

class Achievement(TimeStampedModel):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()

class Certification(TimeStampedModel):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    link = models.URLField()
