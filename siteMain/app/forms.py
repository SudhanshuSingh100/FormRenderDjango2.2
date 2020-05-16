from django import forms
from .models import UserModel


class UserForm(forms.Form):
    username = forms.CharField(max_length=30)
    title = forms.CharField(max_length=200)
    first_name = forms.CharField(max_length=25)
    last_name = forms.CharField(max_length=25)
    mother_name = forms.CharField(max_length=30)
    father_name = forms.CharField(max_length=30)
    email_id = forms.EmailField(max_length=200)
    secret_code = forms.CharField(max_length=5,widget=forms.PasswordInput())
    address = forms.CharField(max_length=250)
    date = forms.DateTimeField(widget=forms.SelectDateWidget())


    class Meta:
        model = UserModel
        fields = ('Username', 'Title', 'First Name', 'Last_name',
                      'Mother Name', 'Father Name', 'Email_id',
                      'Passcode', ' Address', 'Date')


"""
class User(forms.Form):
    username = forms.CharField(max_length=30,
                               min_length=4, required=True,
                               widget=forms.TextInput(
                                    attrs={
                                        "placeholder": "Username",
                                        "class": "form-control"
                                    }
                                 )
                               )
    title = forms.CharField(max_length=60, min_length=12, required=True,
                               widget=forms.TextInput(
                                    attrs={
                                        "placeholder": "Project Title",
                                        "class": "form-control"
                                    }
                                 )
                               )

    first_name = forms.CharField(max_length=20, min_length=4,required=True, widget=forms.TextInput(
                                    attrs={
                                        "placeholder": "First Name",
                                        "class": "form-control"
                                        }))
                                 
    last_name = forms.CharField(max_length=30,
                               min_length=4,required=True,
                               widget=forms.TextInput(
                                    attrs={
                                        "placeholder" : "Last Name",
                                        "class" : "form-control"
                                    }
                                 )
                               )

    mother_name = forms.CharField(max_length=30,
                               min_length = 4,required = True,
                               widget = forms.TextInput(
                                    attrs = {
                                        "placeholder" : "Mother's Name",
                                        "class" : "form-control"
                                    }
                                 )
                               )

    father_name = forms.CharField(max_length=30,
                               min_length = 4,required = True,
                               widget = forms.TextInput(
                                    attrs = {
                                        "placeholder" : "Father's Name",
                                        "class" : "form-control"
                                    }
                                 )
                               )
    email_id = forms.EmailField(max_length=255, required=True,
                                widget=forms.EmailInput(
                                      attrs={
                                          "placeholder": "Email",
                                          "class": "form-control"
                                      }
                                 )
                                )
    secret_code = forms.CharField(min_length=5,max_length=5, required=True,
                                  widget= forms.PasswordInput(attrs={"placeholder": "Passcode",
                                                                     "class": "form-control" }
                                    )
                                  )
    address = forms.Textarea(max_length=200,required=True,
                             widget=forms.TextInput(
                                 attrs={
                                     "placeholder":"Address",
                                     "class": "form-control"
                                 })
                             )
    date = forms.DateTimeField(widget=forms.SelectDateWidget(
                                      attrs={
                                     "placeholder":"Address",
                                     "class": "form-control" }
                                 )
                               )
"""
