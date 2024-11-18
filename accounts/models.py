from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from orders.models import Order


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    tel = models.CharField(max_length=11, blank=True)
    postal_code = models.CharField(max_length=6, blank=True)
    city = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.user.username}'

    class Meta:
        verbose_name = 'Профайл'
        verbose_name_plural = 'Профайлы'

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def update_profile(sender, instance, **kwargs):
    instance.profile.save()




