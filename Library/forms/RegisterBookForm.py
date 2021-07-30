from django import forms


class RegisterBook(forms.Form):
    title = forms.CharField(label='Title', max_length=30, required=True)
    author = forms.CharField(label='Author', max_length=30, required=True)
    genre = forms.CharField(label='Genre', max_length=30, required=True)
    height = forms.IntegerField(label='Height', max_value=10000, required=True)
    publisher = forms.CharField(label='Publisher', max_length=50, required=True)
