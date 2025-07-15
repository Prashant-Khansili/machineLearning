from django import forms
from .models import LemonImage

class LemonImageForm(forms.ModelForm):
    class Meta:
        model = LemonImage
        fields = ['image']
    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if image.size > 10 * 1024 * 1024:
                raise forms.ValidationError("Image size should not exceed 10MB")
            return image
        else:
            raise forms.ValidationError("Couldn't read uploaded image")
