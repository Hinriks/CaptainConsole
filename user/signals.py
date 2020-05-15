from django.db.models.signals import post_save
from .models import User ,Order
from cart.models import Cart
from django.dispatch import receiver

#reciever

@receiver(post_save, sender=Order)
def remove_user_from_cart(sender, instance, created, **kwargs):
    if created:
        Cart.objects.filter(id=instance.cart.id).update(user=None)


#@receiver(post_save, sender=User)
#def save_cart(sender, instance, **kwargs):
#    instance.cart.save()