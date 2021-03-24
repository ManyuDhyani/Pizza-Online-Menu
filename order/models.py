from django.db import models
from django.urls import reverse
from .utils import unique_slug_generator
from django.db.models.signals import pre_save

class Category(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Prize(models.Model):
    prize = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return str(self.prize)

class Size(models.Model):
    size = models.CharField(max_length=30)

    def __str__(self):
        return self.size

class Topping(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        verbose_name_plural = 'Toppings'

    def __str__(self):
        return self.name


class Pizza(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    description = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to='images/pizza', default='images/gallery-img1.jpg')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    topping = models.ManyToManyField(Topping, blank=True)
    gallery = models.BooleanField(default=False)
    offer = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Pizza'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={
            'slug': self.slug
        })

def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender=Pizza)

class Prizesize(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    prize = models.ForeignKey(Prize, on_delete=models.SET_NULL, null=True)
    size = models.ForeignKey(Size, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = 'Pizza Prizes & Sizes'

    def __str__(self):
        title = self.pizza.name + " " + str(self.prize.prize) + " " + self.size.size
        return title

class About(models.Model):
    head1 = models.CharField(max_length=30)
    head2 = models.CharField(max_length=30)
    content = models.TextField()
    photo = models.ImageField(upload_to='images/about', default='images/gallery-img1.jpg')

    class Meta:
        verbose_name_plural = 'About'

class Contact(models.Model):
    address = models.CharField(max_length=50)
    mobile1 = models.CharField(max_length=50)
    mobile2 = models.CharField(max_length=50)
    email = models.EmailField()
    time = models.CharField(max_length=30)
    day = models.CharField(max_length=30)
    menu = models.FileField(upload_to='menu', null=True)

    class Meta:
        verbose_name_plural = 'Contact'