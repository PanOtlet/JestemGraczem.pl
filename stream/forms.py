from django import forms
from captcha.fields import ReCaptchaField


class YouTubeForm(forms.Form):
    name = forms.CharField(label='Tytuł filmu', max_length=50)
    video_id = forms.CharField(label='ID filmu', max_length=23)
    captcha = ReCaptchaField()


class TwitchForm(forms.Form):
    username = forms.CharField(label='Nazwa użytkownika na Twitch.tv')
    captcha = ReCaptchaField()
