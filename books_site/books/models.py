from django.db import models



class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField('birthday')

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=500)  # hey, I've seen longer LN titles
    num_pages = models.IntegerField(default=0)
    date_published = models.DateField('date published')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title