from django import forms
# Signup Form for registering users
# -------------------------


class SignupForm(forms.Form):
    username = forms.CharField(max_length=30, required=True, label='',
                               widget=forms.TextInput(attrs={'id': 'signup-username',
                                                             'placeholder': 'Nome de Usuário',
                                                             'class': 'form-control', }))
    email = forms.EmailField(max_length=254, required=True, label='',
                             widget=forms.TextInput(attrs={'id': 'signup-email',
                                                           'placeholder': 'Email',
                                                           'class': 'form-control',
                                                           }))
    password = forms.CharField(max_length=100, required=True, label='',
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Senha',
                                                             'type': 'password',
                                                             'id': 'signup-password',
                                                             }))


# Login Form for authenticating users
# -------------------------
class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, required=True, label='',
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Nome de Usuário',
                                                             'id': 'login-username',
                                                             }))
    password = forms.CharField(max_length=100, required=True, label='',
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Senha',
                                                             'type': 'password',
                                                             'id': 'login-password',
                                                             }))


# Settings Form for changing profile settings
# -------------------------
class ProfileSettingsForm(forms.Form):
    profile_photo = forms.ImageField(required=False,)
    first_name = forms.CharField(max_length=20, required=False,
                                 widget=forms.TextInput(attrs={'class': 'form-control',
                                                               'placeholder': 'Nome',
                                                               'id': 'form-username',
                                                               }))
    bio = forms.CharField(max_length=140, required=False,
                          widget=forms.TextInput(attrs={'class': 'form-control',
                                                        'placeholder': 'Máximo 140 caracteres',
                                                        'id': 'form-bio-input',
                                                        }))
    location = forms.CharField(max_length=30, required=False,
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Sua lcoalização (Arstotzka)',
                                                             'id': 'form-location-input',
                                                             }))
    personal_link = forms.CharField(max_length=30, required=False,
                                    widget=forms.TextInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'www.youtube.com/channel/twittaft',
                                                                  'id': 'form-personal-link-input',
                                                                  }))

# TWeet form for adding tweets(entries)
# -------------------------
class TweetForm(forms.Form):
    tweet_content = forms.CharField(max_length=280, required=True, label='',
                                    widget=forms.Textarea(attrs={'id': 'tweet-mechanism-textarea',
                                                                  'placeholder': "Glória a Arstotzka! (máximo 280 caracteres)",
                                                                  }))

# Search Form for searching users
# -------------------------
class SearchForm(forms.Form):
    key_word = forms.CharField(max_length=30, label='', required=False,
                               widget=forms.TextInput(attrs={'placeholder': 'procurar usuário',
                               }))
