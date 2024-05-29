from django.db import models

# Create your models here.
class UserDetails(models.Model):
    userid  = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='USERID')
    first_name = models.CharField('FirstName', max_length=50)
    last_name = models.CharField('LastName', max_length=50)
    user_name = models.CharField("UserName", max_length=50, unique=True)
    email = models.EmailField('EmailID',max_length=50)
    password = models.CharField('Password',max_length=50)

    def __str__(self):
        return f"{self.userid}-{self.first_name}-{self.last_name}"
    
class ShareDetails(models.Model):
    shareid = models.BigAutoField(auto_created=True,primary_key=True, serialize=False, verbose_name='SHAREID')
    dop = models.DateField('DateofPurchase', auto_now_add=True)
    comp_name = models.CharField("CompanyName", max_length=50)
    price = models.IntegerField('Price')
    quantity = models.IntegerField('Quantity')
    userid = models.ForeignKey(UserDetails, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.shareid}-{self.dop}-{self.comp_name}"