from django.db import models

# Create your models here.
class BlogPost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=5000, default="")
    head1 = models.CharField(max_length=500, default="")
    chead1 = models.CharField(max_length=5000, default="")
    head2 = models.CharField(max_length=500, default="")
    chead2 = models.CharField(max_length=5000, default="")
    head3 = models.CharField(max_length=500, default="")
    chead3 = models.CharField(max_length=5000, default="")
    head4 = models.CharField(max_length=500, default="")
    chead4 = models.CharField(max_length=5000, default="")
    head5 = models.CharField(max_length=500, default="")
    chead5 = models.CharField(max_length=5000, default="")
    adminquote = models.CharField(max_length=5000, default="")
    summary = models.CharField(max_length=5000, default="")
    pub_date = models.DateField()
    thumbnail = models.ImageField(upload_to='blog/images', default="")

    def __str__(self):
        return self.title