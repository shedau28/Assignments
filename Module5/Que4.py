# Explain what does django-admin.py make messages command is used for?


# django-admin.py is Django’s command-line utility for administrative tasks. This document outlines all it can do.

# In addition, manage.py is automatically created in each Django project. manage.py is a thin wrapper around django-admin.py that takes care of two things for you before delegating to django-admin.py:

# It puts your project’s package on sys.path.
# It sets the DJANGO_SETTINGS_MODULE environment variable so that it points to your project’s settings.py file.
# The django-admin.py script should be on your system path if you installed Django via its setup.py utility. If it’s not on your path, you can find it in site-packages/django/bin within your Python installation. Consider symlinking it from some place on your path, such as /usr/local/bin.

# For Windows users, who do not have symlinking functionality available, you can copy django-admin.py to a location on your existing path or edit the PATH settings (under Settings - Control Panel - System - Advanced - Environment...) to point to its installed location.

# Generally, when working on a single Django project, it’s easier to use manage.py. Use django-admin.py with DJANGO_SETTINGS_MODULE, or the --settings command line option, if you need to switch between multiple Django settings files.

# The command-line examples throughout this document use django-admin.py to be consistent, but any example can use manage.py just as well.