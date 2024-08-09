from django.db import models

# Create your models here.

class Portfolio(models.Model):
    author=models.ForeignKey("auth.User", on_delete=models.CASCADE)
    portfolio_image=models.FileField(upload_to="portfolio_image",blank=True,null=True,verbose_name="Portfolio Image")
    cretae_date=models.DateTimeField(auto_now_add=True)
    portfolio_name=models.TextField()
    portfolio_image_detail=models.TextField()
    portfolio_detail=models.TextField()
    portfolio_about=models.TextField()
    
    def __str__(self):
        return self.portfolio_name
    
    
    
class Product(models.Model):
    product_image=models.FileField(upload_to="product_image",blank=True,null=True,verbose_name="Product Image")    
    product_status=models.TextField(blank=True,null=True)
    product_name=models.TextField(blank=True,null=True)
    product_location=models.TextField(blank=True,null=True)
    product_about=models.TextField(blank=True,null=True)
    product_type=models.TextField(blank=True,null=True)
    product_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    product_bath_count = models.IntegerField(default=0)
    product_bed_count=models.IntegerField(default=0)
    product_ft=models.IntegerField(default=0)
    product_build_year=models.IntegerField(default=0)
    def __str__(self):
        return self.product_name
    
   
class Agent(models.Model):
    agent_image=models.FileField(upload_to="product_image",blank=True,null=True,verbose_name="Product Image")   
    agent_name=models.TextField(blank=True,null=True)
    agent_job_title=models.TextField(blank=True,null=True) 
    agent_about=models.TextField(blank=True,null=True)
    agent_details=models.TextField(blank=True,null=True)
    agent_img_detail=models.TextField(blank=True,null=True)
    
    def __str__(self):
        return self.agent_name
    
    
class Service(models.Model):
    service_name=models.TextField(blank=True,null=True)
    service_about=models.TextField(blank=True,null=True)
    
    def __str__(self):
        return self.service_name
    
    
    