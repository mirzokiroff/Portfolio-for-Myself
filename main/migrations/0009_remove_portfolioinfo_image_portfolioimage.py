# Generated by Django 5.0.6 on 2024-07-09 08:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_user_delete_about_me_remove_blogimages_blog_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolioinfo',
            name='image',
        ),
        migrations.CreateModel(
            name='PortfolioImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='portfolio_pics/')),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='main.portfolioinfo')),
            ],
        ),
    ]