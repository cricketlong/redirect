"""
WSGI config for redirect project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import sys
import site
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "redirect.settings")

site.addsitedir("/var/www/redirect_env/lib/python3.8/site-packages")

# Add the app's directory to the PYTHONPATH
sys.path.append('/var/www/redirect_env/redirect')
sys.path.append('/var/www/redirect_env/redirect/redirect')

django.setup()

# Activate your virtual env
activate_env=os.path.expanduser("/var/www/redirect_env/bin/activate_this.py")
exec(compile(open(activate_env, "rb").read(), activate_env, 'exec'), dict(__file__=activate_env))

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
