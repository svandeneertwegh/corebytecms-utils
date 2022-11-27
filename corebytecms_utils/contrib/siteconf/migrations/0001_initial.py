# Generated by Django 3.2.15 on 2022-11-27 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('site_title', models.CharField(blank=True,
                 max_length=255, verbose_name='Site title')),
                ('site_author', models.CharField(blank=True,
                 max_length=255, null=True, verbose_name='Author')),
                ('social_facebook', models.URLField(
                    blank=True, verbose_name='Facebook address')),
                ('social_twitter', models.URLField(
                    blank=True, verbose_name='Twitter address')),
                ('social_linkedin', models.URLField(
                    blank=True, verbose_name='LinkedIn adsreas')),
                ('mail_address', models.EmailField(blank=True,
                 max_length=255, null=True, verbose_name='Email address')),
                ('phone', models.CharField(blank=True, max_length=255,
                 null=True, verbose_name='Phone number')),
            ],
            options={
                'verbose_name': 'Site configuration',
            },
        ),
    ]
