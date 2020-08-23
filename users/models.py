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

    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(
        max_length=10, null=True, choices=GENDER_CHOICES, blank=True
    )  # CharField는 항상 max_length필수
    bio = models.TextField(default="", blank=True)
    pass
