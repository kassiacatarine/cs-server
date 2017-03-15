# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-12-07 02:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import model_utils.fields
import wagtail.contrib.wagtailroutablepage.models
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0030_auto_20160806_1503'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ScrumProject',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('description', wagtail.wagtailcore.fields.RichTextField()),
                ('workday_duration', models.IntegerField(default=2)),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail.contrib.wagtailroutablepage.models.RoutablePageMixin, 'wagtailcore.page'),
        ),
        migrations.CreateModel(
            name='Sprint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('start_date', models.DateTimeField()),
                ('due_date', models.DateTimeField()),
                ('duration_weeks', models.IntegerField(default=1)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scrum.ScrumProject')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', model_utils.fields.StatusField(choices=[(0, 'backlog'), (1, 'todo'), (2, 'doing'), (3, 'done')], default=0, max_length=100, no_check_for_status=True)),
                ('description', wagtail.wagtailcore.fields.RichTextField()),
                ('duration_hours', models.IntegerField()),
                ('assigned_to', models.ManyToManyField(related_name='_task_assigned_to_+', to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='scrum.ScrumProject')),
                ('sprint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scrum.Sprint')),
            ],
        ),
    ]
