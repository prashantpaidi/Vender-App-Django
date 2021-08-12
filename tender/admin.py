from django.contrib import admin
from .models import Tender, User, Tenderwinner
from django import forms
from django.db import connection
from django.db.models.signals import post_save
from django.dispatch import receiver
from importlib import import_module, reload
from django.conf import settings
from django.urls import clear_url_caches




# Register your models here.
class TenderAdmin(admin.ModelAdmin):
    list_display = ('id', 'tender_name', 'tender_description','start_date','end_date')

admin.site.register(Tender, TenderAdmin)

# admin.site.register(Bid)


class TenderwinnerForm(forms.ModelForm):
   
    cursor = connection.cursor()
    cursor.execute("SELECT derivedTable.id,derivedTable.id || ' - ' || tender_name FROM (SELECT * FROM tender_tender WHERE tender_tender.end_date < current_date) AS derivedTable LEFT JOIN tender_tenderwinner ON derivedTable.id = tender_tenderwinner.tender_id WHERE user_id is NULL")
    data = cursor.fetchall()
    tender = forms.ChoiceField(choices=data)

class TenderwinnerAdmin(admin.ModelAdmin):
    fields = ('tender',)
    list_display = ('tender_name','user_name')
    def tender_name(self, instance):
        return instance.tender.tender_name
    def user_name(self, instance):
        user = User.objects.get(id=instance.user_id)
        return user

    form = TenderwinnerForm
    

admin.site.register(Tenderwinner, TenderwinnerAdmin)



@receiver(post_save, sender=Tenderwinner) # this is called after a User model is saved.
def set_tender_winner(instance,created, **kwargs):
    if created:
        print('running')
        admin.site.unregister(Tenderwinner)
        class TenderwinnerForm(forms.ModelForm):
            cursor1 = connection.cursor()
            cursor1.execute("SELECT derivedTable.id,derivedTable.id || ' - ' || tender_name FROM (SELECT * FROM tender_tender WHERE tender_tender.end_date < current_date) AS derivedTable LEFT JOIN tender_tenderwinner ON derivedTable.id = tender_tenderwinner.tender_id WHERE user_id is NULL")
            data = cursor1.fetchall()
            print(data)
            MY_CHOICES = data
            tender = forms.ChoiceField(choices=MY_CHOICES)
        class TenderwinnerAdmin(admin.ModelAdmin):
            fields = ('tender',)
            list_display = ('tender',)
            form = TenderwinnerForm
        
        admin.site.register(Tenderwinner, TenderwinnerAdmin)

        reload(import_module(settings.ROOT_URLCONF))
        clear_url_caches()

