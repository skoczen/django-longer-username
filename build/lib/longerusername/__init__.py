from django.conf import settings

def MAX_USERNAME_LENGTH():
    if hasattr(settings,"MAX_USERNAME_LENGTH"):
        return settings.MAX_USERNAME_LENGTH
    else:
        return 255
