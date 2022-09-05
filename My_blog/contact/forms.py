from django import forms 


class ConctactForm(forms.Form):
    matter = forms.CharField(max_length = 50, min_length = 1)
    message = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField(max_length = 30)