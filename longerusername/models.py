from django.utils.translation import ugettext as _
from django.db.models.signals import class_prepared
from longerusername import MAX_USERNAME_LENGTH

def longer_username(sender, *args, **kwargs):
    if sender.__name__ == "User" and sender.__module__ == "django.contrib.auth.models":
        sender._meta.get_field("username").max_length = MAX_USERNAME_LENGTH
        sender._meta.get_field("username").help_text = _("Required. Only letters, numbers, and @, ., +, -, or _ characters.")

class_prepared.connect(longer_username)