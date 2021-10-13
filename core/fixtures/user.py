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
:FILE:      DjangoBackend-ReactFrontend/core/fixtures/user.py
:AUTHOR:    Nathan E White, PhD
:ABOUT:     Initializes data for the core.user app
------------------------------------------------------------------------------------------------------------------------
:NOTES:     For more information on this file, see:
                            https://docs.djangoproject.com/en/3.2/howto/initial-data/
------------------------------------------------------------------------------------------------------------------------
"""
# <BOF>

#   Imports --- User Model Imports: Imports our user model so we can set some initial data for it
from core.user.models import User

#   User model initial data
data_user = {
    "email": "testuser@example.com",
    "password": "Password123456789",
    "username": "testuser"
}

#   Call the logic for creating the user
User.objects.create_user(**data_user)

# ----------------------------------------------------------------------------------------------------------------------
# <EOF>
