from django import forms
from .models import myform

class detailsForm(forms.ModelForm):
    
    Name = forms.CharField(widget=forms.TextInput(attrs={"class":"input","type":"text","placeholder":"Name.."}))
    email = forms.CharField(widget=forms.TextInput(attrs={"class":"input","type":"email","placeholder":"Email.."}))
    mobile_number = forms.CharField(widget=forms.TextInput(attrs={"class":"input","type":"text","placeholder":"Phone Number.."}))
    college = forms.CharField(widget=forms.TextInput(attrs={"class":"input","type":"text","placeholder":"Collage..."}))
    branch = forms.CharField(widget=forms.TextInput(attrs={"class":"input","type":"text","placeholder":"Branch.."}))
    year = forms.CharField(widget=forms.TextInput(attrs={"class":"input","type":"text","placeholder":"Year.."}))
    
    class Meta:
        model = myform
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # removing label
        for key, field in self.fields.items():
            field.label = "" 
            