SECRET_KEY = 'fake-key'  # noqa: S105
INSTALLED_APPS = ['djaa_list_filter', 'tests']
DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3'}}
PASSWORD_HASHERS = ('django.contrib.auth.hashers.MD5PasswordHasher',)
