from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')
	Roll_No = models.IntegerField(default='180101089')
	Department = models.CharField(default='CSE',max_length=100)

	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self, *args, **kwargs):
		super(Profile, self).save(*args, **kwargs)

		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)

class Dept(models.Model):
	Dep = models.CharField(max_length=100)
	D1P1 = models.CharField(max_length=100)
	D1P2 = models.CharField(max_length=100)
	D1P3 = models.CharField(max_length=100)
	D1P4 = models.CharField(max_length=100)
	D1P5 = models.CharField(max_length=100)
	D1P6 = models.CharField(max_length=100)
	D1P7 = models.CharField(max_length=100)



	D2P1 = models.CharField(max_length=100)
	D2P2 = models.CharField(max_length=100)
	D2P3 = models.CharField(max_length=100)
	D2P4 = models.CharField(max_length=100)
	D2P5 = models.CharField(max_length=100)
	D2P6 = models.CharField(max_length=100)
	D2P7 = models.CharField(max_length=100)


	D3P1 = models.CharField(max_length=100)
	D3P2 = models.CharField(max_length=100)
	D3P3 = models.CharField(max_length=100)
	D3P4 = models.CharField(max_length=100)
	D3P5 = models.CharField(max_length=100)
	D3P6 = models.CharField(max_length=100)
	D3P7 = models.CharField(max_length=100)

	D4P1 = models.CharField(max_length=100)
	D4P2 = models.CharField(max_length=100)
	D4P3 = models.CharField(max_length=100)
	D4P4 = models.CharField(max_length=100)
	D4P5 = models.CharField(max_length=100)
	D4P6 = models.CharField(max_length=100)
	D4P7 = models.CharField(max_length=100)


	D5P1 = models.CharField(max_length=100)
	D5P2 = models.CharField(max_length=100)
	D5P3 = models.CharField(max_length=100)
	D5P4 = models.CharField(max_length=100)
	D5P5 = models.CharField(max_length=100)
	D5P6 = models.CharField(max_length=100)
	D5P7 = models.CharField(max_length=100)


	D6P1 = models.CharField(max_length=100)
	D6P2 = models.CharField(max_length=100)
	D6P3 = models.CharField(max_length=100)
	D6P4 = models.CharField(max_length=100)
	D6P5 = models.CharField(max_length=100)
	D6P6 = models.CharField(max_length=100)
	D6P7 = models.CharField(max_length=100)
	def get_absolute_url(self):
		return reverse('timetablet')

class BRs(models.Model):
	department = models.CharField(max_length=100)
	roll_no = models.IntegerField()