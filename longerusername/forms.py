from django.utils.translation import ugettext as _
from django.contrib.auth import forms as auth_forms
from django import forms

from longerusername import MAX_USERNAME_LENGTH

class UserCreationForm(auth_forms.UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].max_length = MAX_USERNAME_LENGTH()
        self.fields['username'].help_text = _("Required. Only letters, numbers, and @, ., +, -, or _ characters.")

class UserChangeForm(auth_forms.UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        self.fields['username'].max_length = MAX_USERNAME_LENGTH()
        self.fields['username'].help_text = _("Required. Only letters, numbers, and @, ., +, -, or _ characters.")

class AuthenticationForm(auth_forms.AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(AuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].max_length = MAX_USERNAME_LENGTH()
        self.fields['username'].help_text = _("Required. Only letters, numbers, and @, ., +, -, or _ characters.")
