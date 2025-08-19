from django.db import models
# Create your models here.
class Customers(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    mobile = models.CharField(max_length=12, default=10)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.username}, {self.password}"
    
class Restarunts(models.Model):
    res_name = models.CharField(max_length=100)
    Food_cat = models.CharField(max_length=100)
    rating  = models.FloatField()
    img = models.URLField(default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR7KBKxKUEmumbhS_sR7eCr-s1likOF0RHtOvAbPXSA70O1ATMHQwZxbCCNwCYCtGQjTVo&usqp=CAU")
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.res_name
    

class Menu(models.Model):
    res = models.ForeignKey(
        Restarunts,
        on_delete = models.CASCADE
    )
    item_name = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    is_available = models.BooleanField(default=True)
    category = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.item_name} - {self.res.res_name}"


class Cart(models.Model):
    customer = models.ForeignKey( 
        Customers,
        on_delete=models.CASCADE
    )
    items = models.ManyToManyField('Menu')

    def total_price(self):
        return sum(item.price for item in self.items.all())
    
    def __str__(self):
        return f"{self.customers.username} {self.total_price()}"
    