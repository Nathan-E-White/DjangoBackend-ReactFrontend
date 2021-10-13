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
:FILE:      DjangoBackend-ReactFrontend/core/apps.py
:AUTHOR:    Nathan E White, PhD
:ABOUT:     Defines a app-config manager for the core app
:NOTES:     For more information on this file, see:
                            https://docs.djangoproject.com/en/3.2/ref/applications/
------------------------------------------------------------------------------------------------------------------------
"""
# <BOF>

#   Imports --- Django Package Imports: Imports an admin class for a pluggable app
from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'core'
    label = 'core'
