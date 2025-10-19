"""
WSGI config for HakiRecord project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""


import os
import sys
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HakiRecord.settings')

print("🚀 Starting Django on Render...")

try:
    application = get_wsgi_application()
    print("✅ Django application loaded successfully.")
except Exception as e:
    print("💥 Django failed to start:")
    import traceback
    traceback.print_exc()
    sys.stdout.flush()
    raise




# Keep the existing code below this
