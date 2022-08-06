from django.contrib.contenttypes.models import ContentType

from user_opinion_controller.models import AppealToUser



class AppealManager:
    """
        Class for management Appeal model
    """

    @classmethod
    def create_appeal_to_user( cls, sender, receiver, content ):
        """
            Create appeal to user
        """

        if sender.is_authenticated != True:
            return False

        AppealToUser.objects.create(
            sender = sender,
            receiver = receiver,

            content = content,
        )
