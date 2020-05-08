from django.db import models

# Create your models here.

class Author(models.Model):
    full_name = models.TextField()
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)

    def __str__(self):
        # return "{}, {}".format(self.full_name, self.birth_year) # Проверял ответ на задание
        return self.full_name

class Redaction(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Friend(models.Model):
    FriendName = models.CharField(max_length=60)

    def __str__(self):
        return self.FriendName


class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField()
    description = models.TextField()
    year_release = models.SmallIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="book_author")
    copy_count = models.SmallIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    redaction = models.ForeignKey('Redaction', on_delete=models.CASCADE, null=True, blank=True, related_name='books')
    take_friend = models.ForeignKey('Friend', on_delete=models.CASCADE, null=True, blank=True, related_name='books')
    book_image = models.ImageField(upload_to='book_images/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.title




