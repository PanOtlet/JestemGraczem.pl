from django import forms


class MultiTwitch(forms.Form):
    username1 = forms.CharField(max_length=32, widget=forms.TextInput)
    username2 = forms.CharField(max_length=32, widget=forms.TextInput)
    username3 = forms.CharField(max_length=32, widget=forms.TextInput, required=False)
    username4 = forms.CharField(max_length=32, widget=forms.TextInput, required=False)
    chat = forms.BooleanField(widget=forms.CheckboxInput)
