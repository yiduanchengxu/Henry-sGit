from django.db import models
from django.contrib import admin

# Create your models here.
class BlogPost(models.Model):
	"""docstring for BlogPost"""
	title = models.CharField(max_length=150)
	body = models.TextField()
	timestamp = models.DateTimeField()

	class Meta:
		"""docstring for Meta"""
		ordering = ('-timestamp',)

class BlogPostAdmin(admin.ModelAdmin):
	"""docstring for BlogPostAdmin"""""
	list_display = ('title', 'timestamp')
		
admin.site.register(BlogPost, BlogPostAdmin)
