from django.db import models

# Create your models here.
class Snack(models.Model):
    name = models.CharField(max_length=64)
    rank = models.IntegerField()
    eater = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # eater = models.CharField(max_length=64, default='Ahmad')
    def __str__(self):
        return self.name



# User table   1 ------- many       Snack table
