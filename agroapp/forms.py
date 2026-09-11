from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import FarmerProfile, CropInput


class FarmerRegistrationForm(UserCreationForm):
    full_name = forms.CharField(max_length=150, required=True, label="Full Name")
    phone = forms.CharField(max_length=15, required=True, label="Phone Number")
    district = forms.CharField(max_length=100, required=False, label="District")
    village = forms.CharField(max_length=100, required=False, label="Village")
    preferred_language = forms.ChoiceField(
        choices=FarmerProfile.LANGUAGE_CHOICES,
        required=True,
        label="Preferred Language"
    )
    land_size_acres = forms.DecimalField(
        max_digits=5,
        decimal_places=2,
        required=False,
        label="Land Size (acres)"
    )
    soil_type = forms.ChoiceField(
        choices=FarmerProfile.SOIL_TYPE_CHOICES,
        required=False,
        label="Soil Type"
    )
    preferred_crops = forms.CharField(
        max_length=255,
        required=False,
        help_text="Comma-separated crop names (e.g., Ragi, Maize)"
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "full_name", "phone", "district", "village",
                  "preferred_language", "land_size_acres", "soil_type",
                  "preferred_crops", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        full_name = self.cleaned_data.get("full_name", "")
        user.first_name = full_name

        if commit:
            user.save()
            FarmerProfile.objects.create(
                user=user,
                phone=self.cleaned_data["phone"],
                district=self.cleaned_data.get("district", ""),
                village=self.cleaned_data.get("village", ""),
                preferred_language=self.cleaned_data["preferred_language"],
                land_size_acres=self.cleaned_data.get("land_size_acres"),
                soil_type=self.cleaned_data.get("soil_type", ""),
                preferred_crops=self.cleaned_data.get("preferred_crops", "")
            )

        return user


class CropInputForm(forms.ModelForm):
    class Meta:
        model = CropInput
        fields = ['location', 'soil_type', 'ph_value', 'nitrogen',
                  'phosphorus', 'potassium', 'land_area', 'season']
