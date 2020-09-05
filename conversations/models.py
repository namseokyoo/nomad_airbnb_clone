from django.db import models
from core import models as core_model


class Conversation(core_model.TimeStampedModel):

    """ Conversation Model Definition """

    participants = models.ManyToManyField("users.User", blank=True)

    def __str__(self):
        return str(self.created)


class Message(core_model.TimeStampedModel):

    """ Message Model Definition """

    message = models.TextField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    conversation = models.ForeignKey("Conversation", on_delete=models.CASCADE)


def __str__(self):
    return f"{self.user} say : {self.text}"