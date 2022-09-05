from django import forms 


class ConctactForm(forms.Form):
    matter = forms.CharField(max_length = 50, min_length = 1, widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length = 30, widget=forms.TextInput(attrs={'class': 'form-control'}))