# Generated by Django 3.2.15 on 2022-11-27 14:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('cmsplugin_ptr',
                 models.OneToOneField(auto_created=True,
                                      on_delete=django.db.models.deletion.CASCADE,
                                      parent_link=True,
                                      primary_key=True,
                                      related_name='faq_faq',
                                      serialize=False,
                                      to='cms.cmsplugin')),
                ('question',
                 models.CharField(max_length=255, verbose_name='Vraag')),
                ('answer', models.TextField(verbose_name='Answer')),
            ],
            options={
                'verbose_name': 'Veelgestelde vragen',
                'verbose_name_plural': 'FAQs',
            },
            bases=('cms.cmsplugin',),
        ),
    ]
