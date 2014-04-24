`django-longer-username` provides a migration and a monkeypatch to make the Django auth.user username field longer, instead of the arbitrarily short 30 characters. It's designed to be a simple include-and-forget project that makes a little headache go away.  Enjoy, and pull requests welcome!

Note that [Django 1.5 or newer already includes support for custom `User` models][releasenotes15] (read [this tutorial][tutorial] and the [official documentation about *Substituting a custom User model*][documentation15]). So, you only need `django-longer-username` if you use an older Django version, or if you don't want to create your own User model for some reason.

[tutorial]: http://procrastinatingdev.com/django/using-configurable-user-models-in-django-1-5/
[releasenotes15]: https://docs.djangoproject.com/en/1.5/releases/1.5/#configurable-user-model
[documentation15]: https://docs.djangoproject.com/en/1.5/topics/auth/customizing/#auth-custom-user

Usage
=====
Step 1. Install django-longer-username. 
-------------------------------------

- `pip install longerusername` 

You will also need to install [south]() to use the migration. 

- `pip install south` 


Step 2. Add `longerusername` to your installed apps.
-------------------------
Add 'longerusername' to the top of your `INSTALLED_APPS` in settings.py

settings.py

```python
INSTALLED_APPS = ("longerusername",) + INSTALLED_APPS
```

Step 3. (Optional) Specify a custom username length
------------------------------------------------
If you want to specify a custom length, add it to settings.py. The default is 255 characters.

settings.py

```python
MAX_USERNAME_LENGTH = 100  # optional, default is 255.
```



Step 4. Run the migration
------------------------------------------------
```
$ python manage.py migrate longerusername
```

That's it, you should be good to go!


Notes about the built-in forms
==============================
This app also automatically monkey patches the User forms in the Django admin to remove the 30 character limit.

It provides a suitable replacement for the standard AuthenticationForm as well, but due to the implementation you must manually utilize it.

urls.py

```python
from longerusername.forms import AuthenticationForm

urlpatterns = patterns('',
    # ...
    (r'^accounts/login/$', 'django.contrib.auth.views.login', {'authentication_form': AuthenticationForm}),
)
```

Credits
=======

The monkeypatch for this is very largely based on [celement's answer on stackoverflow][so]

[so]: http://stackoverflow.com/questions/2610088/can-djangos-auth-user-username-be-varchar75-how-could-that-be-done
