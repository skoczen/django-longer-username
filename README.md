`django-longer-username` provides a migration and a monkeypatch to make the django auth.user username field longer, instead of the arbitrarily short 30 characters. 

It's designed to be a simple include-and-forget project that makes a little headache go away.  Enjoy, and pull requests welcome!

Usage
=====
Step 1. Install django-longer-username. 
-------------------------------------
Right now, you can either:

- Download and install, or
- `pip install -e git://github.com/GoodCloud/django-longer-username.git#egg=longerusername` it from here. If there's 
demand, I'll look into pypi.

You will also need to install [south]() to use the migration. 

 - `pip install south` 


Step 2. Add `longerusername` to your installed apps.
-------------------------
Add 'longerusername' to you installed apps in settings.py

settings.py
```
INSTALLED_APPS += (
    "longerusername",
)
```

Step 3. (Optional) Specify a custom username length
------------------------------------------------
If you want to specify a custom length, add it to settings.py. The default is 255 characters.

settings.py
```
MAX_USERNAME_LENGTH = 100  # optional, default is 255.
```



Step 4. Run the migration
------------------------------------------------
```
$ python manage.py migrate longerusername
```

That's it, you should be good to go!


Credits
=======

The monkeypatch for this is very largely based on [celement's answer on stackoverflow](http://stackoverflow.com/questions/2610088/can-djangos-auth-user-username-be-varchar75-how-could-that-be-done)