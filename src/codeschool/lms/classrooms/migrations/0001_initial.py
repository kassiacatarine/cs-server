# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-25 20:44
from __future__ import unicode_literals

import codeschool.lms.classrooms.models.classroom
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import wagtail.contrib.wagtailroutablepage.models
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('academic', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wagtailcore', '0032_add_bulk_delete_page_permission'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('weekly_lessons', models.BooleanField(default=False, help_text='If true, the lesson spans a whole week. Otherwise, each lesson would correspond to a single day/time slot.', verbose_name='weekly lessons')),
                ('accept_subscriptions', models.BooleanField(default=True, help_text='Set it to false to prevent new student subscriptions.', verbose_name='accept subscriptions')),
                ('is_public', models.BooleanField(default=True, help_text='If true, all students will be able to see the contents of the course. Most activities will not be available to non-subscribed students.', verbose_name='is it public?')),
                ('subscription_passphrase', models.CharField(blank=True, default=codeschool.lms.classrooms.models.classroom.random_subscription_passphase, help_text='A passphrase/word that students must enter to subscribe in the course. Leave empty if no passphrase should be necessary.', max_length=140, verbose_name='subscription passphrase')),
                ('short_description', models.CharField(max_length=140)),
                ('description', wagtail.wagtailcore.fields.RichTextField()),
                ('template', models.CharField(blank=True, choices=[('programming-beginner', 'A beginner programming course'), ('programming-intermediate', 'An intermediate programming course'), ('programming-marathon', 'A marathon-level programming course')], max_length=20)),
                ('discipline', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='academic.Discipline')),
                ('staff', models.ManyToManyField(blank=True, related_name='classrooms_as_staff', to=settings.AUTH_USER_MODEL)),
                ('students', models.ManyToManyField(blank=True, related_name='classrooms_as_student', to=settings.AUTH_USER_MODEL)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='classrooms_as_teacher', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail.contrib.wagtailroutablepage.models.RoutablePageMixin, 'wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='ClassroomList',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail.contrib.wagtailroutablepage.models.RoutablePageMixin, 'wagtailcore.page'),
        ),
    ]