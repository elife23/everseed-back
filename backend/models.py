from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class Commentmeeting(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField(db_column='dateTime')  # Field name made lowercase.
    author = models.CharField(max_length=255)
    meetingid = models.ForeignKey('Meeting', models.DO_NOTHING, db_column='meetingId')  # Field name made lowercase.
    deleted = models.IntegerField()

    class Meta:
        db_table = 'commentmeeting'


class Commentwhiteboard(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField(db_column='dateTime')  # Field name made lowercase.
    author = models.CharField(max_length=255)
    whiteboardid = models.ForeignKey('Whiteboard', models.DO_NOTHING, db_column='whiteboardId')  # Field name made lowercase.
    deleted = models.IntegerField()

    class Meta:
        db_table = 'commentwhiteboard'


class Meeting(models.Model):
    name = models.CharField(max_length=255)
    datetime = models.DateTimeField(db_column='dateTime')  # Field name made lowercase.
    duration = models.DecimalField(max_digits=10, decimal_places=0)
    deleted = models.IntegerField()
    roomname = models.BigIntegerField(default=0)

    class Meta:
        db_table = 'meeting'


class Meetingroom(models.Model):
    name = models.CharField(max_length=255)
    maxcapacity = models.IntegerField(db_column='maxCapacity')  # Field name made lowercase.
    deleted = models.IntegerField()
    meetingid = models.ForeignKey(Meeting, models.DO_NOTHING, default=1, db_column='meetingId')  # Field name made lowercase.

    class Meta:
        db_table = 'meetingroom'


class Participant(models.Model):
    status = models.CharField(max_length=255)
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userId')  # Field name made lowercase.
    meetingid = models.ForeignKey(Meeting, models.DO_NOTHING, db_column='meetingId')  # Field name made lowercase.

    class Meta:
        db_table = 'participant'


class Subscription(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()

    class Meta:
        db_table = 'subscription'


class MyUserManager(BaseUserManager):
    def create_user(self, email, firstname, lastname, deleted, password=None, **extra_fields):
        """
        Creates and saves a UserManager.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            firstname=firstname,
            lastname=lastname,
            deleted=deleted,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    

    def create_superuser(self, email, firstname, lastname, deleted, password=None, **extra_fields):
        """
        Creates and saves a superuser.
        """
        user = self.create_user(
            email=email,
            firstname=firstname,
            lastname=lastname,
            deleted=deleted,
            password=password,
            **extra_fields
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    deleted = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    last_login = None

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["firstname", "lastname", "password", "deleted"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    class Meta:
        db_table = 'user'


class Usersubscription(models.Model):
    expirationdate = models.DateTimeField(db_column='expirationDate')  # Field name made lowercase.
    userid = models.ForeignKey(User, models.DO_NOTHING, db_column='userId')  # Field name made lowercase.
    subscriptionid = models.ForeignKey(Subscription, models.DO_NOTHING, db_column='subscriptionId')  # Field name made lowercase.
    deleted = models.IntegerField()

    class Meta:
        db_table = 'usersubscription'


class Whiteboard(models.Model):
    content = models.TextField()
    whitename = models.BigIntegerField(default=0)

    class Meta:
        db_table = 'whiteboard'
