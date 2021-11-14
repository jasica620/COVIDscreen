from os import name
from django.db import models
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9copy.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
	def basic_validator(self, postData):
		errors={}
		if len(postData['first_name']) < 2:
			errors['first_name'] = "First name cannot be less than 2 characters"
		elif len(postData['last_name']) < 2:
			errors['last_name'] = "Last name cannot be less than 2 characters"
		elif not EMAIL_REGEX.match(postData['email']):
			errors['email'] = "Invalid email"
		elif len(postData['password1']) < 8:
			errors['password1'] = "Invalid password"
		elif postData['password1'] != postData['password2']:
			errors['password2'] = "Passwords do not match"
		return errors

    def login_validation(self, postData):
		errors={}
		user = User.objects.get(email = postData['loginemail'])
		if not bcrypt.checkpw(postData['loginpw'].encode(), user.password.encode()):
			errors['fail'] = "Cannot log in"
		return errors


class Employer(models.Model):
    company = models.CharField(max_length=200)
    first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects=UserManager()

class Employee(models.Model)
    company_name = models.ForeignKey(company_name, on_delete=models.CASCADE )
    first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=200)
    birthday = models.DateField
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # body_temp = models.IntegerField(default=92)
    # Question_1 = models.BooleanField
    # Question_2 = models.BooleanField
    # Question_3 = models.BooleanField
    # Question_4 = models.BooleanField
    # Question_5 = models.BooleanField

    objects=UserManager()
