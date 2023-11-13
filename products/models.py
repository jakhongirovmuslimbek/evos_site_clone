from django.db import models
from django.utils.text import slugify

class CategoryModel(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            count = 1
            while CategoryModel.objects.filter(slug=self.slug).exists():
                self.slug = f"{slugify(self.title)}-{count}"
                count += 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class ProductModel(models.Model):
    category = models.ForeignKey(CategoryModel, related_name="category", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="images/%y%m%d", blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

