from django.db import models

from mptt.models import MPTTModel, TreeForeignKey

from user_controller.models import CustomUser



class Label( models.Model ):
    """
        Forum labels model class
    """

    name = models.CharField(
        max_length = 64,
    )

    creator = models.ForeignKey(
        to = CustomUser,
        on_delete = models.SET_NULL,
        related_name = 'labels',

        null = True,
    )


    def __str__(self) -> str:
        return f'Label: {self.name}'


    class Meta:
        ordering = [
            'name',
        ]


class Question( models.Model ):
    """
        Forum questions model class
    """

    title = models.CharField(
        max_length = 255,
        unique = True,
    )
    content = models.TextField()

    date_of_creation = models.DateTimeField(
        auto_now_add = True,
    )

    creator = models.ForeignKey(
        to = CustomUser,
        on_delete = models.SET_NULL,
        related_name = 'questions',

        null = True,
    )
    correct_answer = models.OneToOneField(
        to = 'Answer',
        on_delete = models.SET_NULL,
        related_name = 'correctly_answered_question',

        null = True,
    )
    labels = models.ManyToManyField(
        to = Label,
        related_name = 'questions',
    )


    def __str__(self) -> str:
        return f'Question: {self.title}'


    class Meta:
        ordering = [
            '-date_of_creation',
        ]


class Answer( MPTTModel ):
    """
        Question answers model class
    """

    content = models.TextField()

    date_of_creation = models.DateTimeField(
        auto_now_add = True,
    )

    creator = models.ForeignKey(
        to = CustomUser,
        on_delete = models.SET_NULL,
        related_name = 'answers',

        null = True,
    )
    question = models.ForeignKey(
        to = Question,
        on_delete = models.CASCADE,
        related_name = 'answers',
    )

    parent = TreeForeignKey(
        to = 'self',
        on_delete = models.CASCADE,
        related_name = 'children',

        blank = True,
        null = True,
    )


    def __str__(self) -> str:
        return f'Answer: {self.pk}'


    class MPTTMeta:
        order_insertion_by = [
            'question',
            'level',
            'tree_id',
            '-date_of_creation',
        ]
