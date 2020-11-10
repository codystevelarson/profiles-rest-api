from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserProfileManager(BaseUserManager):
    ''' Manager for user profiles '''

    def create_user(self, email, name, password=None):
        ''' Create a new user profile '''
        if not email:
            raise ValueError('Users must have an email address')

        # makes backend of email case insensitive
        email = self.normalize_email(email)
        user = self.model(email=emai, name=name)

        # Using the abstractBaseUser model's method to create a password hash
        user.set_password(password)
        # Save user in default DB
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        ''' Create and save a new super user '''
        user = self.create_user(email, name, password)
        # Inherited from permissions mixin
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    ''' Database models for users in the system '''
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    # Methods to allow us to use this custom model like the standard django user model
    def get_full_name(self):
        ''' Retrieve full name of user '''
        return self.name

    def get_short_name(self):
        ''' Retrieve short name of user '''
        return self.name

    def __str__(self):
        ''' Return string representation of user '''
        return self.email