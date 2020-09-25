from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from .models import Snippet, Book
from django.core.validators import RegexValidator
#This class will create a form with the required fields for the project
class AddForm(forms.ModelForm):
    id = forms.IntegerField()
    title = forms.CharField()
    date = forms.DateField()
    author = forms.CharField()
    publication = forms.CharField()
    price = forms.FloatField()

    class Meta:
        model = Book
        fields = ('id', 'title','date','author','publication','price')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            'id',
            'title',
            'date',
            'author',
            'publication',
            'price',
            Submit("submit", "ADD", css_class="btn-success")
#The submit button is used in the form which will lead to sumbmission of the data

        )


#This class is just used for demo purpose.
class SnippetForm(forms.ModelForm):

    class Meta:
        model = Snippet
        fields = ('title', 'body')





