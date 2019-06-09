from django.db import models

# Create a blog model
# Title
# Publication Date
# Text
# Image

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    text = models.TextField()
    image = models.ImageField(upload_to='images/')

# Add blog app to settings

# Create a migration

# Migrate

# Add to admin
