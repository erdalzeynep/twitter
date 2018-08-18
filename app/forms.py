from django import forms

from app.models import Tweet


class AddTweetForm(forms.ModelForm):
    author = forms.CharField(required=False, widget=forms.HiddenInput())

    class Meta:
        model = Tweet
        fields = {'content', 'author'}

    def __init__(self, username, *args, **kwargs):
        self.current_username = username
        super(AddTweetForm, self).__init__(*args, **kwargs)

    def clean_author(self):
        return self.current_username


class UpdateTweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = {'content'}
