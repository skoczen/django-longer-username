import django
from django.core.validators import MaxLengthValidator
from django.utils.translation import ugettext as _
from django.db.models.signals import class_prepared
from django.conf import settings
from longerusername import MAX_USERNAME_LENGTH

def longer_username_signal(sender, *args, **kwargs):
    if (sender.__name__ == "User" and
        sender.__module__ == "django.contrib.auth.models"):
        patch_user_model(sender)
class_prepared.connect(longer_username_signal)

def patch_user_model(model):
    field = model._meta.get_field("username")

    field.max_length = MAX_USERNAME_LENGTH()
    field.help_text = _("Required, %s characters or fewer. Only letters, "
                        "numbers, and @, ., +, -, or _ "
                        "characters." % MAX_USERNAME_LENGTH())

    # patch model field validator because validator doesn't change if we change
    # max_length
    for v in field.validators:
        if isinstance(v, MaxLengthValidator):
            v.limit_value = MAX_USERNAME_LENGTH()

from django.contrib.auth.models import User

# https://github.com/GoodCloud/django-longer-username/issues/1
# django 1.3.X loads User model before class_prepared signal is connected
# so we patch model after it's prepared

# check if User model is patched
if User._meta.get_field("username").max_length != MAX_USERNAME_LENGTH():
    patch_user_model(User)