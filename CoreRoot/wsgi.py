#! /usr/bin/env python
"""
------------------------------------------------------------------------------------------------------------------------
                  ____        __  __                   __  __               __
                 / __ \__  __/ /_/ /_  ____  ____     / / / /__  ____ _____/ /__  _____
 ____________   / /_/ / / / / __/ __ \/ __ \/ __ \   / /_/ / _ \/ __ `/ __  / _ \/ ___/  ____________
/_____/_____/  / ____/ /_/ / /_/ / / / /_/ / / / /  / __  /  __/ /_/ / /_/ /  __/ /     /_____/_____/
              /_/    \__, /\__/_/ /_/\____/_/ /_/  /_/ /_/\___/\__,_/\__,_/\___/_/
                    /____/
------------------------------------------------------------------------------------------------------------------------
:FILE:      DjangoBackend-ReactFrontend/CoreRoot/wsgi.py
:AUTHOR:    Nathan E White, PhD
:ABOUT:     Sets up Python Web Service Gateway Interface (WSGI) for Django project
:NOTES:     For more information on this file, see:
                            https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
                            https://wsgi.readthedocs.io/en/latest/
------------------------------------------------------------------------------------------------------------------------
"""
# <BOF>

#   Imports --- Django Package Import: WSGI application module
from django.core.wsgi import get_wsgi_application

#   Imports --- Python STL Import:  OS modules for environment
import os


#   Set env needed by Django for WSGI
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CoreRoot.settings')

#   Call WSGI interface
application = get_wsgi_application()

# ----------------------------------------------------------------------------------------------------------------------
# <EOF>
