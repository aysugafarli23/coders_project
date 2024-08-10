from django.db import models

# Create your models here.

class Portfolio(models.Model):
    author=models.ForeignKey("auth.User", on_delete=models.CASCADE)
    portfolio_image=models.FileField(upload_to="portfolio_image",blank=True,null=True,verbose_name="Portfolio Image")
    cretae_date=models.DateTimeField(auto_now_add=True)
    portfolio_name=models.CharField(max_length=30,blank=True,null=True)
    portfolio_image_detail=models.TextField()
    portfolio_detail=models.TextField()
    portfolio_about=models.TextField()
    
    def __str__(self):
        return self.portfolio_name
    
    
    
class Product(models.Model):
    product_image = models.ImageField(upload_to="product_images/", blank=True, null=True, verbose_name="Product Image")
    product_name = models.CharField(max_length=30,blank=True,null=True)
    product_status=models.CharField(max_length=10,blank=True,null=True)
    product_location = models.CharField(max_length=30,blank=True,null=True)
    product_type = models.CharField(max_length=30,blank=True,null=True)
    product_about = models.TextField(blank=True, null=True)
    product_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    product_bath_count = models.IntegerField(default=0)
    product_bed_count = models.IntegerField(default=0)
    product_ft = models.IntegerField(default=0)
    product_build_year = models.IntegerField(default=0)

    def __str__(self):
        return self.product_name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    
    class Meta:
        ordering = ['id']
   
class Agent(models.Model):
    agent_image=models.FileField(upload_to="product_image",blank=True,null=True,verbose_name="Product Image")   
    agent_name=models.CharField(max_length=30,blank=True,null=True)
    agent_surname=models.CharField(max_length=30,blank=True,null=True)
    agent_job_title=models.CharField(max_length=30,blank=True,null=True) 
    agent_about=models.TextField(blank=True,null=True)
    agent_details=models.TextField(blank=True,null=True)
    agent_img_detail=models.TextField(blank=True,null=True)
    
    def __str__(self):
        return self.agent_name
    
    
class Service(models.Model):
    service_name=models.CharField(max_length=30,blank=True,null=True)
    service_about=models.TextField(blank=True,null=True)
    
    def __str__(self):
        return self.service_name
    
class Customer(models.Model):
    customer_name=models.CharField( max_length=20,blank=True,null=True)
    customer_surname=models.CharField( max_length=20,blank=True,null=True)
    customer_email=models.EmailField(max_length=40)
    customer_coupon=models.IntegerField(default=0)
    customer_phone=models.IntegerField(default=0)
    customer_service=models.CharField(max_length=30,blank=True,null=True)
    customer_country=models.CharField(max_length=20,blank=True,null=True)
    customer_street=models.CharField(max_length=20,blank=True,null=True)
    customer_apartment=models.CharField(max_length=20,blank=True,null=True)
    customer_state=models.CharField(max_length=20,blank=True,null=True)
    customer_zip=models.CharField(max_length=20,blank=True,null=True)
    customer_cash=models.DecimalField(max_digits=10, decimal_places=3, default=0)
    customer_note=models.TextField(blank=True,null=True)
    
    def __str__(self):
        return self.customer_name
    