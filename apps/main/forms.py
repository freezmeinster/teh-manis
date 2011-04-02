from django.contrib.auth.models import User
from django import forms

class UserRegistrationForm(forms.ModelForm):
    fullname = forms.CharField(label="Nama Lengkap", max_length=255)
    username = forms.RegexField(label="Username", max_length=30, regex=r'^[\w.@+-]+$',
    help_text = "Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.",
    error_messages = {'invalid': "Username hanya boleh beruba angka, huruf dan karakter @/./+/-/_ ."})
    password1 = forms.CharField(label="Kata Sandi", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Konfirmasi Kata Sandi", widget=forms.PasswordInput,
    help_text = "Masukan password yang sesuai untuk verifikasi.")
    
    class Meta:
	model = User
	fields = ("username","email","first_name","last_name")
	
    def if_exist(self):
	username = self.cleaned_data["username"]
	try:
	    User.objects.get(username=username)
	except User.DoesNotExist:
	    return username
	    raise forms.ValidationError("Pengguna sudah terdaftar.")
		
    def clean_password2(self):
	password1 = self.cleaned_data.get("password1", "")
	password2 = self.cleaned_data["password2"]
	if password1 != password2:
	    raise forms.ValidationError("Kedua kata sandi tidak cocok.")
	return password2
		    
    def save(self, commit=True):
	user = super(UserRegistrationForm, self).save(commit=False)
	user.first_name = self.cleaned_data["fullname"].split()[0] 
	user.last_name = ' '.join(self.cleaned_data["fullname"].split()[1:])
	user.set_password(self.cleaned_data["password1"])
	user.save()
	return user