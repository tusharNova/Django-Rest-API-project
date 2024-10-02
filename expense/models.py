from django.db import models

# Create your models here.

class Transaction(models.Model):
    titel = models.CharField( max_length=100)
    amount = models.FloatField()
    tranaction_type = models.CharField( max_length=100 ,choices=(("Credit" , "Credit") , ("Debit" , "Debit")))
    
    
    def save(self , *args, **kwargs):
        if self.tranaction_type == "Debit":
            self.amount = self.amount * -1
            
        return super().save(*args, **kwargs)