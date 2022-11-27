# Generated by Django 3.2.15 on 2022-11-27 13:43

import django.db.models.deletion
import filer.fields.image
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teamemployee',
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees'},
        ),
        migrations.RemoveField(
            model_name='teamemployee',
            name='image',
        ),
        migrations.RemoveField(
            model_name='teamemployee',
            name='name',
        ),
        migrations.AddField(
            model_name='teamemployee',
            name='full_name',
            field=models.CharField(
                default='John Doe',
                max_length=255,
                verbose_name='Full name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teamemployee',
            name='picture',
            field=filer.fields.image.FilerImageField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='team_picture',
                to=settings.FILER_IMAGE_MODEL,
                verbose_name='Picture'),
        ),
        migrations.AlterField(
            model_name='teamemployee',
            name='description',
            field=models.TextField(verbose_name='Beschrijving'),
        ),
        migrations.AlterField(
            model_name='teamemployee',
            name='email',
            field=models.EmailField(
                blank=True,
                max_length=254,
                verbose_name='E-mailadres'),
        ),
        migrations.AlterField(
            model_name='teamemployee',
            name='function',
            field=models.CharField(max_length=255, verbose_name='Function'),
        ),
        migrations.AlterField(
            model_name='teamemployee',
            name='linkedin',
            field=models.URLField(blank=True, verbose_name='LinkedIn page'),
        ),
        migrations.AlterField(
            model_name='teamemployee',
            name='twitter',
            field=models.URLField(blank=True, verbose_name='Twitter page'),
        ),
    ]
