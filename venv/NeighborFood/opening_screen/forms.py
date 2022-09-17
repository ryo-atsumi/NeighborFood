from tkinter import Widget
from django import forms

widget_textinput = forms.TextInput(
    attrs={
        "class": "form-control form-control-lg",
        "placeholder": "NeighborFoodで検索"
    }
)

class SearchForm(forms.Form):
    search_word = forms.CharField(widget=widget_textinput, label="", required=False)