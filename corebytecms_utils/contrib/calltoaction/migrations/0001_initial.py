# Generated by Django 3.2.15 on 2022-11-27 12:23

import cms.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='CallToAction',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='calltoaction_calltoaction', serialize=False, to='cms.cmsplugin')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('subtitle', models.CharField(max_length=255, verbose_name='Subtitle')),
                ('link_name', models.CharField(max_length=255, verbose_name='Link naam')),
                ('style', models.CharField(choices=[('default', 'Default'), ('primary', 'Primary'), ('secondary', 'Secondary'), ('tertiary', 'Tertiary'), ('quaternary', 'Quaternary')], default='default', max_length=255)),
                ('featured', models.BooleanField(default=False, verbose_name='Featured')),
                ('animated', models.BooleanField(default=True, verbose_name='Animated')),
                ('borders', models.BooleanField(default=True, verbose_name='Borders')),
                ('link_page', cms.models.fields.PageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms.page', verbose_name='CMS Page')),
            ],
            options={
                'verbose_name': 'Call to action',
                'verbose_name_plural': 'Call to actions',
                'ordering': ['pk'],
            },
            bases=('cms.cmsplugin',),
        ),
    ]
