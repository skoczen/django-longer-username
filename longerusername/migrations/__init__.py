from django.conf import settings

@property
def MAX_USERNAME_LENGTH():
    if "MAX_USERNAME_LENGTH" in settings:
        return settings.MAX_USERNAME_LENGTH
    else:
        return 255
