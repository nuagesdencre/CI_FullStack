from django.db import models

frequency_options = (
    ('Once / Gift', 'Once / Gift'),
    ('Twice Yearly', 'Twice Yearly'),
    ('Once every 3 months', 'Once every 3 months'),
    ('Once every 4 months', 'Once every 4 months'),
    ('Once every 2 months', 'Once every 2 months'),
)


class Product(models.Model):
    name = models.CharField(max_length=300, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to="product_imgs")
    frequency = models.CharField(max_length=300,choices=frequency_options, default=4)

    def __str__(self):
        return self.name
