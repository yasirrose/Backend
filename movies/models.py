from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.name}"


class Movie(models.Model):
    name = models.CharField(max_length=40)
    slug = models.CharField(max_length=50, unique=True)
    created_at = models.DateField()
    released_at = models.DateField()
    downloads = models.IntegerField(default=0)
    # views=models.IntegerField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    brand = models.OneToOneField("Brand", on_delete=models.CASCADE)
    poster = models.CharField(max_length=100)
    tags = models.ManyToManyField("Tag")

    def __str__(self) -> str:
        return f"{self.name}"


class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f"{self.name}"
