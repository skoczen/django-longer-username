from django.conf import settings


class MAX_USERNAME_LENGTH(object):
    @property
    def __call__(self):
        if "MAX_USERNAME_LENGTH" in settings:
            return settings.MAX_USERNAME_LENGTH
        else:
            return 255
