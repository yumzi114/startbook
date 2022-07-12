from django import forms
class PostSearchForm(forms.Form):
    search_word=forms.CharField(label='Search Word')
    #<input type="text">와 같음 charfield는 textinput위젯