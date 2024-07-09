from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class User(models.Model):
    image = models.ImageField(upload_to='personal_pics/')
    name = models.CharField(max_length=222)
    tel_num = models.CharField(max_length=77)
    job = models.CharField(max_length=77)
    email = models.EmailField(max_length=111)
    about_me = models.TextField()

    def __str__(self):
        return self.name


class PortfolioInfo(models.Model):
    name = models.CharField(max_length=111, null=True, blank=True)
    category = models.CharField(max_length=222, null=True, blank=True)
    client = models.CharField(max_length=222, null=True, blank=True)
    client_url = models.CharField(max_length=222, null=True, blank=True)
    project_date = models.CharField(verbose_name='loyiha vaqti misol uchun: 2024-07-08\nyoki 2024-07-08 20:48:50', max_length=77, null=True, blank=True)
    project_url = models.URLField(max_length=222, null=True, blank=True)
    example_detail = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.category


class PortfolioImage(models.Model):
    portfolio = models.ForeignKey('main.PortfolioInfo', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='portfolio_pics/')

    def __str__(self):
        return f"{self.portfolio.name} Image"


class Skill(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return self.name


class Services(models.Model):
    name = models.CharField(max_length=111)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    name = models.CharField(max_length=222)
    category = models.CharField(max_length=222)
    description = models.TextField()
    upload_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog_pics/')

    def __str__(self):
        return self.name


class BlogSingle(models.Model):
    title = models.CharField(max_length=222)
    name = models.CharField(max_length=222)
    job = models.CharField(max_length=111)
    comment = models.PositiveIntegerField()
    article = models.TextField()
    main_data = models.CharField(max_length=9999)

    def __str__(self):
        return self.name


class Priz(models.Model):
    title = models.CharField(max_length=222)
    amount = models.PositiveIntegerField()
    upload_to = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class CustomerOpinion(models.Model):
    name = models.CharField(max_length=111)
    description = models.TextField()
    upload_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    fullname = models.CharField(max_length=128, blank=True, null=True)
    email = models.EmailField(max_length=128, blank=True, null=True)
    post_id = models.ForeignKey('main.Blog', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
