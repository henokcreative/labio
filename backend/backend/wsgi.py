"""
WSGI config for backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

# backend/wsgi.py
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

application = get_wsgi_application()

# Auto-run migrations on Render
if os.environ.get("RENDER"):
    try:
        from django.core.management import call_command
        call_command("migrate", interactive=False)
        print("✅ Database migrated successfully on Render.")
    except Exception as e:
        print(f"⚠️ Migration skipped or failed: {e}")