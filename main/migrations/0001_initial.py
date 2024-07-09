# Generated by Django 4.2.3 on 2023-07-24 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About_me',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_me', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=222)),
                ('category', models.CharField(max_length=222)),
                ('description', models.TextField()),
                ('upload_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='BlogSingle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=222)),
                ('name', models.CharField(max_length=222)),
                ('job', models.CharField(max_length=111)),
                ('comment', models.PositiveIntegerField()),
                ('article', models.TextField()),
                ('main_data', models.CharField(max_length=9999)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerOpinion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=111)),
                ('description', models.TextField()),
                ('upload_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='GetInTouch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instagram', models.CharField(max_length=111)),
                ('facebook', models.CharField(max_length=111)),
                ('linkedin', models.CharField(max_length=111)),
                ('twitter', models.CharField(max_length=111)),
                ('about_it', models.CharField(max_length=111)),
                ('location', models.CharField(max_length=111)),
                ('phone', models.CharField(max_length=111)),
                ('email', models.CharField(max_length=111)),
            ],
        ),
        migrations.CreateModel(
            name='MainPortfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=222)),
                ('category', models.CharField(max_length=222)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='personal_pics/')),
                ('profile', models.CharField(max_length=222)),
                ('tel_num', models.CharField(max_length=77)),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=111)),
                ('category', models.CharField(max_length=222)),
                ('client', models.CharField(max_length=222)),
                ('project_date', models.DateTimeField(auto_now_add=True)),
                ('project_url', models.URLField(max_length=222)),
                ('example_detail', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Priz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=222)),
                ('amount', models.PositiveIntegerField()),
                ('upload_to', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=111)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('percentage', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ProjectImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='profile_pics/')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='main.portfolioinfo')),
            ],
        ),
        migrations.CreateModel(
            name='BlogImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='blog_pics/')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='main.blog')),
            ],
        ),
    ]