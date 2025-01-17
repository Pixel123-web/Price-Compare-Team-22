from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse


class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"

    name = models.CharField(max_length=255, default='')
    slug = models.SlugField(blank=True, default='')

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save()

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.slug)])



class Store(models.Model):
    name = models.CharField(max_length=255, default='')
    website = models.CharField(max_length=255, default='')
    image = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, default='')
    slug = models.SlugField(blank=True, default='')
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, null=True, on_delete=models.CASCADE)
    price = models.CharField(max_length=225, default='')
    image = models.CharField(max_length=255, default='')
    url = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save()

    def get_absolute_url(self):
        return reverse('detail', kwargs={"p_slug": self.slug, "c_slug": self.category.slug})


class Comment(models.Model):
    content = models.TextField(max_length = 200, default = True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.content, self.name)

