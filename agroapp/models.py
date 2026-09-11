from django.db import models
from django.contrib.auth.models import User


class FarmerProfile(models.Model):
    LANGUAGE_CHOICES = [
        ('kn', 'Kannada'),
        ('en', 'English'),
        ('hi', 'Hindi'),
    ]

    SOIL_TYPE_CHOICES = [
        ('black', 'Black Soil'),
        ('red', 'Red Soil'),
        ('sandy', 'Sandy Soil'),
        ('loamy', 'Loamy Soil'),
        ('other', 'Other'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='farmer_profile')
    phone = models.CharField(max_length=15)
    district = models.CharField(max_length=100, blank=True)
    village = models.CharField(max_length=100, blank=True)
    preferred_language = models.CharField(max_length=5, choices=LANGUAGE_CHOICES, default='kn')

    land_size_acres = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    soil_type = models.CharField(max_length=20, choices=SOIL_TYPE_CHOICES, blank=True)
    preferred_crops = models.CharField(max_length=255, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class CropInput(models.Model):
    SEASON_CHOICES = [
        ('kharif', 'Kharif'),
        ('rabi', 'Rabi'),
        ('summer', 'Summer'),
    ]

    farmer = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    soil_type = models.CharField(max_length=20, choices=FarmerProfile.SOIL_TYPE_CHOICES)
    ph_value = models.DecimalField(max_digits=4, decimal_places=2)
    nitrogen = models.CharField(max_length=10)
    phosphorus = models.CharField(max_length=10)
    potassium = models.CharField(max_length=10)
    land_area = models.DecimalField(max_digits=5, decimal_places=2)
    season = models.CharField(max_length=10, choices=SEASON_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"CropInput #{self.id} by {self.farmer.username}"


class CropRecommendation(models.Model):
    crop_input = models.OneToOneField(CropInput, on_delete=models.CASCADE, related_name='recommendation')
    main_crop = models.CharField(max_length=100)
    score = models.IntegerField()
    alt_crop_1 = models.CharField(max_length=100, blank=True)
    alt_crop_2 = models.CharField(max_length=100, blank=True)
    reason = models.TextField()

    def __str__(self):
        return f"Recommendation for {self.crop_input.farmer.username}"


class FertilizerPlan(models.Model):
    crop_name = models.CharField(max_length=100)
    stage = models.CharField(max_length=50)  # e.g. Sowing, 30 Days
    fertilizer_name = models.CharField(max_length=100)
    quantity_per_acre = models.CharField(max_length=50)
    when_to_apply = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.crop_name} - {self.stage}"
