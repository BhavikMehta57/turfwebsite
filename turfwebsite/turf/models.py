from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

max_sizes = (
    ("0", "0"),
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
)


class User(models.Model):
    name = models.CharField(max_length=200, default='')
    emailid = models.EmailField(('email address'), unique=True)
    phone_number = models.PositiveIntegerField(max_length=10)

    def __str__(self):
        return self.name


class Turf_List(models.Model):
    turf_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, default='')
    address = models.CharField(max_length=500, default='')
    image = models.ImageField(default='', upload_to="../media")
    facilities = models.CharField(max_length=500, default='')
    emergency = models.CharField(max_length=500, default='')
    events = models.CharField(max_length=500, default='')
    num_5v5 = models.CharField(max_length=1, choices=max_sizes, default="0")
    price_per_hour_5v5 = models.IntegerField(default=500)
    num_7v7 = models.CharField(max_length=1, choices=max_sizes, default="0")
    price_per_hour_7v7 = models.IntegerField(default=700)
    num_7v7_5v5 = models.CharField(
        max_length=1, choices=max_sizes, default="0")
    num_12v12 = models.CharField(max_length=1, choices=max_sizes, default="0")
    price_per_hour_12v12 = models.IntegerField(default=1200)

    def __str__(self):
        return self.name


# Reservation Model
size_choices = (
    ("5v5", "5v5"),
    ("7v7", "7v7"),
    ("12v12", "12v12"),
)


class Booking(models.Model):
    startTime = models.DateField(default=timezone.now)
    endTime = models.DateField()
    size = models.CharField(max_length=3, choices=size_choices, default="5v5")
    booked_turf_id = models.ForeignKey(Turf_List, default=1)
    # booker_mail = models.ForeignKey()

# # creating a form
# class DetailsForm(forms.Form):

#     first_name = forms.CharField(max_length = 50)
#     last_name = forms.CharField(max_length = 50)
#     phone_number = forms.IntegerField
#     ground_name = forms.CharField(max_length = 50)
#     ground_address = forms.CharField(max_length = 200)


class Contact(models.Model):
    name = models.CharField(max_length=200, default='')
    emailid = models.EmailField(max_length=254, default='')
    message = models.CharField(max_length=2000, default='')

    def __str__(self):
        return self.name
