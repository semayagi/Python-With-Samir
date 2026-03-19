from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=1000)
    email = forms.EmailField()  # email validation
    message = forms.CharField(widget=forms.Textarea)

    # cleaned_data contains all the validated data of the form
    def send_email(self):
        print(f"Sending email from {self.cleaned_data['email']} with message: {self.cleaned_data['message']}")