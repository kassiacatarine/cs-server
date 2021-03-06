from django.utils.translation import ugettext_lazy as _

import bricks.rpc
from codeschool import blocks
from codeschool import mixins
from codeschool import models
from codeschool.lms.activities.models import Activity, Submission, Progress
from codeschool.lms.activities.models.feedback import Feedback

QUESTION_BODY_BLOCKS = [
    ('paragraph', blocks.RichTextBlock()),
    ('heading', blocks.CharBlock(classname='full title')),
    ('markdown', blocks.MarkdownBlock()),
    ('html', blocks.RawHTMLBlock()),
]


class Question(models.DecoupledAdminPage,
               mixins.ShortDescriptionPage,
               Activity):
    """
    Base abstract class for all question types.
    """

    class Meta:
        abstract = True
        permissions = (("download_question", "Can download question files"),)

    body = models.StreamField(
        QUESTION_BODY_BLOCKS,
        blank=True,
        null=True,
        verbose_name=_('Question description'),
        help_text=_(
            'Describe what the question is asking and how should the students '
            'answer it as clearly as possible. Good questions should not be '
            'ambiguous.'
        ),
    )
    comments = models.RichTextField(
        _('Comments'),
        blank=True,
        help_text=_('(Optional) Any private information that you want to '
                    'associate to the question page.')
    )
    import_file = models.FileField(
        _('import question'),
        null=True,
        blank=True,
        upload_to='question-imports',
        help_text=_(
            'Fill missing fields from question file. You can safely leave this '
            'blank and manually insert all question fields.'
        )
    )

    def get_navbar(self, user):
        """
        Returns the navbar for the given question.
        """

        from .components import navbar_question

        return navbar_question(self, user)

    # Serve pages
    def get_context(self, request, *args, **kwargs):
        context = dict(
            super().get_context(request, *args, **kwargs),
            question=self,
            form_name='response-form',
            navbar=self.get_navbar(request.user)
        )
        return context

    #
    # Ajax submissions for user responses
    #
    def render_from_submission(self, submission):
        """
        Render a user-facing message from the supplied submission.
        """

        if submission.recycled and submission.feedback:
            feedback = submission.feedback
            return feedback.render_message()
        elif self._meta.instant_feedback:
            feedback = submission.auto_feedback()
            return feedback.render_message()
        else:
            return 'Your submission is on the correction queue!'

    def serve_ajax_submission(self, client, **kwargs):
        """
        Serve AJAX request for a question submission.
        """

        submission = self.submit_with_user_payload(client.request, kwargs)
        data = self.render_from_submission(submission)
        client.dialog(html=data)

    @bricks.rpc.route(r'^submit-response.api/$', name='submit-ajax')
    def route_ajax_submission(self, client, **kwargs):
        return self.serve_ajax_submission(client, **kwargs)


class QuestionMixin:
    """
    Shared properties for submissions, progress and feedback models.
    """

    question = property(lambda x: x.activity)
    question_id = property(lambda x: x.activity_id)


class QuestionSubmission(QuestionMixin, Submission):
    """
    Abstract class for submissions to questions.
    """

    class Meta:
        abstract = True


class QuestionProgress(QuestionMixin, Progress):
    """
    Abstract class for keeping up with the progress of student responses.
    """

    class Meta:
        abstract = True


class QuestionFeedback(QuestionMixin, Feedback):
    """
    Abstract class for representing feedback to users.
    """

    class Meta:
        abstract = True


# Update the Question._meta attribute
Question._meta.submission_class = QuestionSubmission
Question._meta.progress_class = QuestionProgress
Question._meta.feedback_class = QuestionFeedback
