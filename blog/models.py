from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
   
    image = models.ImageField(null=True, upload_to='images/') 

    CATEGORY1 = 'Food'
    CATEGORY2 = 'Body'
    CATEGORY3 = 'Lifestyle'
    CATEGORY4 = 'Sport'
    CATEGORY5 = 'Other'
    CATEGORY_CHOICES = [
        (CATEGORY1, 'Food'),
        (CATEGORY2, 'Body'),
        (CATEGORY3, 'Lifestyle'),
        (CATEGORY4, 'Sport'),
        (CATEGORY5, 'Other')
    ]
    category = models.CharField(
        blank=True,
        max_length=20,
        choices=CATEGORY_CHOICES,
    )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


