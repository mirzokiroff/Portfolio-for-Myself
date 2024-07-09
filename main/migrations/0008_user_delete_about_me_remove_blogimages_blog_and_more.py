# Generated by Django 5.0.6 on 2024-07-09 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_skill_percentage'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='personal_pics/')),
                ('name', models.CharField(max_length=222)),
                ('tel_num', models.CharField(max_length=77)),
                ('job', models.CharField(max_length=77)),
                ('email', models.EmailField(max_length=111)),
                ('about_me', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='About_me',
        ),
        migrations.RemoveField(
            model_name='blogimages',
            name='blog',
        ),
        migrations.DeleteModel(
            name='PersonalInfo',
        ),
        migrations.RemoveField(
            model_name='projectimages',
            name='project',
        ),
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='1', upload_to='blog_pics/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='portfolioinfo',
            name='image',
            field=models.ImageField(default='1', upload_to='profile_pics/'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='BlogImages',
        ),
        migrations.DeleteModel(
            name='ProjectImages',
        ),
    ]
