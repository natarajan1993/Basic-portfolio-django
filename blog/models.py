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

    def __str__(self):
        return self.title

    def summary(self):
        return self.text[:100] + '...'

    def pub_date_formatted(self):
        return self.pub_date.strftime('%b %e, %Y')
# Add blog app to settings

# Create a migration

# Migrate

# Add to admin
