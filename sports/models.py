from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
	name = models.CharField(max_length=30)

	def __str__(self):
		return str(self.name)

class LPost(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(unique=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	content = models.TextField()
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	size_1 = models.ImageField(upload_to='size_1/', null=True, blank=True)
	size_2 = models.ImageField(upload_to='size_2/', null=True, blank=True)

	class Meta:
		unique_together = ('title', 'slug')
		ordering = ['-created']

	def __str__(self):
		return str(self.title)

class CPost(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(unique=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	content = models.TextField()
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	size_1 = models.ImageField(upload_to='size_1/', null=True, blank=True)
	size_2 = models.ImageField(upload_to='size_2/', null=True, blank=True)

	class Meta:
		unique_together = ('title', 'slug')
		ordering = ['-created']

	def __str__(self):
		return str(self.title)

class MiniCPost(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(unique=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	content = models.TextField()
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	size_1 = models.ImageField(upload_to='size_1/', null=True, blank=True)
	size_2 = models.ImageField(upload_to='size_2/', null=True, blank=True)

	class Meta:
		unique_together = ('title', 'slug')
		ordering = ['-created']

	def __str__(self):
		return str(self.title)


class RPost(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(unique=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	content = models.TextField()
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	size_1 = models.ImageField(upload_to='size_1/', null=True, blank=True)
	size_2 = models.ImageField(upload_to='size_2/', null=True, blank=True)

	class Meta:
		unique_together = ('title', 'slug')
		ordering = ['-created']

	def __str__(self):
		return str(self.title)

class AsiaPost(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(unique=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	content = models.TextField()
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	size_1 = models.ImageField(upload_to='size_1/', null=True, blank=True)
	size_2 = models.ImageField(upload_to='size_2/', null=True, blank=True)

	class Meta:
		unique_together = ('title', 'slug')
		ordering = ['-created']

	def __str__(self):
		return str(self.title)