# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
from datetime import datetime
<<<<<<< HEAD

EMAILCHECK = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
=======
>>>>>>> acc6c86b4a858c4579e59c4a8b072febee7dca30

class UserManager(models.Manager):
    def registration(self, name, email, password, confirm_password):
        errorlist = []
        count = 0
        now = datetime.now()
        if len(name) < 2:
            errorlist.append("First name is too short")
            count += 1
        if len(email) < 1:
            errorlist.append("Email is required!")
            count += 1
<<<<<<< HEAD
        elif not  EMAILCHECK.match(email):
            errorlist.append('Please enter a valid email')
            count += 1
=======
            
>>>>>>> acc6c86b4a858c4579e59c4a8b072febee7dca30
