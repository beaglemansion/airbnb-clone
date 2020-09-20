from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """ Custom Uer Model :) """

    GENDER_MALE = "Male"
    GENDER_FEMALE = "Female"
    GENDER_OTHER = "Other"
    GENDER_CHOICES = (
        (GENDER_MALE, "Male11"),  # 이 값이 화면에서 보여지는 값임
        (GENDER_FEMALE, "Female11"),
        (GENDER_OTHER, "other11"),
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREA = "kr"
    LANGUAGE_CHOICES = ((LANGUAGE_ENGLISH, "English"), (LANGUAGE_KOREA, "Korean"))

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"
    CURRENCY_CHOICES = (
        (CURRENCY_USD, "USD"),
        (CURRENCY_KRW, "KRW"),
    )

    avatar = models.ImageField(blank=True)
    gender = models.CharField(
        max_length=10, choices=GENDER_CHOICES, blank=True
    )  # CharField는 항상 max_length필수
    bio = models.TextField(blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, blank=True)
    superhost = models.BooleanField(default=False)
