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
:FILE:      DjangoBackend-ReactFrontend/core/routers.py
:AUTHOR:    Nathan E White, PhD
:ABOUT:     Defines a router to define paths/links through the api for the site
:NOTES:     For more information on this file, see:
                            https://www.django-rest-framework.org/tutorial/quickstart/#urls
------------------------------------------------------------------------------------------------------------------------
"""
# <BOF>

from rest_framework.routers import SimpleRouter
from core.user.viewsets import UserViewSet
from core.auth.viewsets import LoginViewSet, RegistrationViewSet, RefreshViewSet


routes = SimpleRouter()

# AUTHENTICATION
routes.register(r'auth/login', LoginViewSet, basename='auth-login')
routes.register(r'auth/register', RegistrationViewSet, basename='auth-register')
routes.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')

# USER
routes.register(r'user', UserViewSet, basename='user')


urlpatterns = [
    *routes.urls
]
