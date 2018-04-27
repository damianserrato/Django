# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import datetime
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def register(self, name, username, email, password, confirm):
        errors = []
        if len(name) < 2:
            errors.append("Name must be 2 characters or more")

        if len(username) <2:
            errors.append("Username must be 2 characters or more")

        if len(email) <2:
            errors.append("Email must be 2 characters or more")
        elif not EMAIL_REGEX.match(email):
            errors.append("Invalid email")
        else:
            usersMatchingEmail = User.objects.filter(email=email)
            if len(usersMatchingEmail) > 0:
                errors.append("Email already in use")

        if len(password)<1:
            errors.append("Password is required")
        elif len(password)<8:
            errors.append("Password must be 8 characters or more")
        if len(confirm) <1:
            errors.append("Confirm Password is required")
        elif password != confirm:
            errors.append("Confirm Password must match Password")

        response = {
            "errors": errors,
            "valid": True,
            "user": None
        }

        if len(errors) >0:
            response["valid"] = False
            return response
        response["user"] = User.objects.create(
            name = name,
            username = username,
            email = email,
            password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        )
        return response

    def login(self, email, password):
        errors = []

        if len(email) <1:
            errors.append("Email field cannot be empty!")
        elif not EMAIL_REGEX.match(email):
            errors.append("Invalid email")
        else:
            usersMatchingEmail = User.objects.filter(email=email)
            if len(usersMatchingEmail) == 0:
                errors.append("Unknown email")

        if len(password)<1:
            errors.append("Password is required")
        elif len(password)<6:
            errors.append("Password must be 6 characters or more")

        response = {
            "errors": errors,
            "valid": True,
            "user": None,
        }

        if len(errors) == 0:
            if bcrypt.checkpw(password.encode(), usersMatchingEmail[0].password.encode()):
                response["user"] = usersMatchingEmail[0]
            else:
                errors.append("Incorrect Password")

        if len(errors) > 0:
            response["errors"] = errors
            response["valid"] = False

        return response
    
class MessageManager(models.Manager):
    def make(self, message, users_id):
        response = {
            "text": None
        }

        response["text"] = Message.objects.create(
            message=message,
            users_id=users_id
        )

        return response

class CommentManager(models.Manager):
    def make_comment(self, comment, users_id, id):
        Comment.objects.create(
            comment=comment,
            comments_id=id,
            text_id=users_id
        )



class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    confirm = models.CharField(max_length=255)

    objects = UserManager()

class Message(models.Model):
    message = models.CharField(max_length=1000)
    users = models.ForeignKey(User, related_name="manyusers")

    objects = MessageManager()
    class Meta:
        ordering = ['-id']

class Comment(models.Model):
    comment = models.CharField(max_length=1000)
    comments = models.ForeignKey(Message, related_name="messages", null=True)
    text = models.ForeignKey(User, related_name="users", null=True)
    # this_id = models.CharField(max_lendgth=255)

    objects = CommentManager()

    class Meta:
        ordering = ['-id']
