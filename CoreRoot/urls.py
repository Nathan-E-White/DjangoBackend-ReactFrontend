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
:FILE:      DjangoBackend-ReactFrontend/CoreRoot/urls.py
:AUTHOR:    Nathan E White, PhD
:ABOUT:     Sets up routers for the Django admin site and api routes
:NOTES:     For more information on this file, see:
                            https://docs.djangoproject.com/en/3.1/topics/http/urls/
------------------------------------------------------------------------------------------------------------------------
"""
# <BOF>

#   Imports --- Django Package Imports: admin portal
from django.contrib import admin

#   Imports --- Django Package Imports: url building kit
from django.urls import include, path


#   Define the URL patterns to build
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(('core.routers', 'core'), namespace = 'core-api')),
]

# ----------------------------------------------------------------------------------------------------------------------
# <EOF>
