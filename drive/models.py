from django.db import models
from django.utils import timezone
# Create your models here.

class Directory(models.Model):
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    path = models.TextField(null=True, blank=True)
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Directory, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class File(models.Model):
    parent = models.ForeignKey(Directory, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    extension = models.CharField(max_length=200, null=True, blank=True)
    path = models.TextField(null=True, blank=True, unique=True)
    filetype = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(File, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
