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
:FILE:      DjangoBackend-ReactFrontend/CoreRoot/asgi.py
:AUTHOR:    Nathan E White, PhD
:ABOUT:     Sets up Python Asynchronous Server Gateway Interface (ASGI) for Django Project
:NOTES:     For more information on this file, see:
                            https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
                            https://asgi.readthedocs.io/en/latest/
------------------------------------------------------------------------------------------------------------------------
"""
# <BOF>


#   Imports --- Django Package Imports: Get/create the ASGI module(s)
from django.core.asgi import get_asgi_application

#   Imports --- Python STL Imports: For getting/setting environment defaults
import os

#   Set environmental defaults needed by the ASGI module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CoreRoot.settings')

#   Call/create ASGI
application = get_asgi_application()

# ----------------------------------------------------------------------------------------------------------------------
# <EOF>
