# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-19 02:04
from __future__ import unicode_literals

import codeschool.questions.models
import codeschool.vendor.wagtailmarkdown.blocks
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import wagtail.contrib.wagtailroutablepage.models
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('activities', '0010_auto_20161215_2101'),
        ('wagtailcore', '0030_index_on_pagerevision_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='NumericFeedback',
            fields=[
                ('feedback_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='activities.Feedback')),
            ],
            options={
                'abstract': False,
            },
            bases=(codeschool.questions.models.QuestionMixin, 'activities.feedback'),
        ),
        migrations.CreateModel(
            name='NumericProgress',
            fields=[
                ('progress_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='activities.Progress')),
            ],
            options={
                'abstract': False,
            },
            bases=(codeschool.questions.models.QuestionMixin, 'activities.progress'),
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('base_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='NumericQuestion',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('short_description', models.CharField(help_text='A short textual description to be used in titles, lists, etc.', max_length=140, verbose_name='short description')),
                ('points_total', models.IntegerField(blank=True, help_text="Points may be awarded in specific contexts (e.g., associated with a quiz or in a list of activities) and in Codeschool's generic ranking system.", verbose_name='value')),
                ('stars_total', models.DecimalField(blank=True, decimal_places=1, default=0.0, help_text='Number of stars the activity is worth (fractional stars are accepted). Stars are optional bonus points for special accomplishments that can be used to trade "special powers" in codeschool.', max_digits=5, verbose_name='stars')),
                ('difficulty', models.IntegerField(blank=True, choices=[(0, 'Trivial'), (1, 'Very Easy'), (2, 'Easy'), (3, 'Regular'), (4, 'Hard'), (5, 'Very Hard'), (6, 'Challenge!')])),
                ('author_name', models.CharField(blank=True, help_text="The author's name, if not the same user as the question owner.", max_length=100, verbose_name="Author's name")),
                ('visible', models.BooleanField(default=bool, help_text='Makes activity invisible to users.', verbose_name='Invisible')),
                ('closed', models.BooleanField(default=bool, help_text='A closed activity does not accept new submissions, but users can see that they still exist.', verbose_name='Closed to submissions')),
                ('group_submission', models.BooleanField(default=bool, help_text='If enabled, submissions are registered to groups instead of individual students.', verbose_name='Group submissions')),
                ('max_group_size', models.IntegerField(default=6, help_text='If group submission is enabled, define the maximum size of a group.', verbose_name='Maximum group size')),
                ('disabled', models.BooleanField(default=bool, help_text='Activities can be automatically disabled when Codeshool encounters an error. This usually produces a message saved on the .disabled_message attribute.', verbose_name='Disabled')),
                ('disabled_message', models.TextField(blank=True)),
                ('has_submissions', models.BooleanField(default=bool)),
                ('has_correct_submissions', models.BooleanField(default=bool)),
                ('body', wagtail.wagtailcore.fields.StreamField((('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('markdown', codeschool.vendor.wagtailmarkdown.blocks.MarkdownBlock()), ('html', wagtail.wagtailcore.blocks.RawHTMLBlock())), blank=True, help_text='Describe what the question is asking and how should the students answer it as clearly as possible. Good questions should not be ambiguous.', null=True, verbose_name='Question description')),
                ('comments', wagtail.wagtailcore.fields.RichTextField(blank=True, help_text='(Optional) Any private information that you want to associate to the question page.', verbose_name='Comments')),
                ('import_file', models.FileField(blank=True, help_text='Fill missing fields from question file. You can safely leave this blank and manually insert all question fields.', null=True, upload_to='question-imports', verbose_name='import question')),
                ('correct_answer', models.FloatField(help_text='The expected numeric answer for question.', verbose_name='Correct answer')),
                ('tolerance', models.FloatField(default=0, help_text='If tolerance is zero, the responses must be exact.', verbose_name='Tolerance')),
                ('label', models.CharField(default='Answer', help_text='The label text that is displayed in the submission form.', max_length=100, verbose_name='Label')),
            ],
            options={
                'permissions': (('download_question', 'Can download question files'),),
                'abstract': False,
            },
            bases=(wagtail.contrib.wagtailroutablepage.models.RoutablePageMixin, 'wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='NumericSubmission',
            fields=[
                ('submission_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='activities.Submission')),
                ('value', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
            bases=(codeschool.questions.models.QuestionMixin, 'activities.submission'),
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('base_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]
