from .models import WatchesUploads,Watch_Review
from django import forms

class UploadForm(forms.ModelForm):

    name = forms.CharField(
        widget = forms.TextInput(attrs={'class':'form-control'}),
        required=True
    )

    price = forms.DecimalField(
        widget = forms.NumberInput(attrs={'class':'form-control'}),
        required=True
    )

    description = forms.CharField(
        widget = forms.Textarea(attrs={'class':'form-control', 'rows': 3}),
        required=True
    )

    image = forms.ImageField(
        widget = forms.ClearableFileInput(attrs={'class':'form-control'}),
        required=True
    )



    class Meta:
        model = WatchesUploads
        fields = ['name', 'description', 'price', 'image']




class ReviewForm(forms.ModelForm):
    class Meta:
        model = Watch_Review
        fields = ['review', 'rating']
        widgets = {
            'review': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'rating': forms.Select(choices=[(i, str(i)) for i in range(1, 6)], attrs={'class': 'form-control'}),
        }
