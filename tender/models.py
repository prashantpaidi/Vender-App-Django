from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_save
from datetime import date
from django.core.validators import MinValueValidator
from django import forms



# Create your models here.
class Tender(models.Model): 
    tender_name = models.CharField(max_length=100)
    tender_description = models.CharField(max_length=500)
    start_date = models.DateField(
        validators=[MinValueValidator(limit_value=date.today)]
    )
    
    end_date = models.DateField()



class Bid(models.Model):
    bid_price = models.PositiveIntegerField()
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    tender = models.ForeignKey(Tender, default=None, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('user', 'tender',)




class Tenderwinner(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE, editable=False, null=True, blank=True)
    tender = models.OneToOneField(Tender, default=None, on_delete=models.CASCADE)
  




@receiver(pre_save, sender=Tenderwinner)
def set_tender_winner(instance, **kwargs):
    
    bids = Bid.objects.filter(tender_id=instance.tender_id)
    bid = bids.order_by('bid_price').first()
    print(instance.tender_id)
    instance.user_id = bid.user_id

@receiver(pre_save, sender=Tender) 
def set_tender_winner(instance, **kwargs):
    # get the minmal bidded user
    if(instance.start_date > instance.end_date):
        raise forms.ValidationError('End Date should to greater than strat date')
   