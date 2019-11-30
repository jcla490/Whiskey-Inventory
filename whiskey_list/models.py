from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Spirit (models.Model):
    def __str__(self):
        return self.distillery + " " + self.brand + " " + self.release
    SPIRIT_TYPES = (
        ('AMW', 'American Whiskey'),
        ('AMR', 'American Rye'),
        ('BOU', 'Bourbon Whiskey'),
        ('CAN', 'Canadian Whisky/Rye'),
        ('RUM', 'Rum')
    )

    whiskey_type = models.CharField(max_length=3, choices=SPIRIT_TYPES, default='BOU')

    # Distillery
    distillery = models.CharField("Distillery Name", max_length=255)
    
    # Brand or Label
    brand = models.CharField("Brand Name", max_length=255, blank=True)
    
    # Release Name
    release = models.CharField("Release Name", max_length=255, blank=True)

    # Age
    age = models.FloatField("Age", validators=[MinValueValidator(0), MaxValueValidator(45)])

    # Proof
    proof = models.FloatField("Proof", validators=[MinValueValidator(79), MaxValueValidator(140)])

    # ABV
    abv = models.FloatField("ABV", validators=[MinValueValidator(38), MaxValueValidator(72)])

    # Single Barrel?
    single_barrel = models.BooleanField("Single Barrel?")

    # Barrel Proof?
    barrel_proof = models.BooleanField("Barrel Proof?")

    # Store Pick?
    store_pick = models.BooleanField("Store Pick?")

    # Is Open?
    open_status = models.BooleanField("Is Open?")

    # Quantity
    quantity = models.IntegerField("Quantity")

    # Valuation
    valuation = models.FloatField("Valuation ($)")

    # Last Valued
    value_date = models.DateField("Last Valued")

    # Notes
    notes = models.TextField("Notes", blank=True)
