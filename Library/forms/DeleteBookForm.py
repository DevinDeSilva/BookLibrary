from django import forms


class DeleteBook(forms.Form):
    title = forms.CharField(label='Title', max_length=30, required=True)
