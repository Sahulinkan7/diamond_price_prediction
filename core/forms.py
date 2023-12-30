from typing import Any
from django import forms 

cutchoice=(
    ('Fair','Fair'),
    ('Good','Good'),
    ('Very Good','Very Good'),
    ('Premium','Premium'),
    ('Ideal','Ideal'),
)

colorchoice=(
    ('D','D'),
    ('E','E'),
    ('F','F'),
    ('G','G'),
    ('H','H'),
    ('I','I'),
    ('J','J'),
)

claritychoice=(
    ('I1','I1'),
    ('SI2','SI2'),
    ('SI1','SI1'),
    ('VS2','VS2'),
    ('VS1','VS1'),
    ('VVS2','VVS2'),
    ('VVS1','VVS1'),
    ('IF','IF')
)

class PredictionForm(forms.Form):
    carat=forms.FloatField(widget=forms.TextInput(attrs={'class':'form-control'}))
    depth=forms.FloatField(widget=forms.TextInput(attrs={'class':'form-control'}))
    table=forms.FloatField(widget=forms.TextInput(attrs={'class':'form-control'}))
    x=forms.FloatField(widget=forms.TextInput(attrs={'class':'form-control'}))
    y=forms.FloatField(widget=forms.TextInput(attrs={'class':'form-control'}))
    z=forms.FloatField(widget=forms.TextInput(attrs={'class':'form-control'}))
    cut=forms.ChoiceField(choices=cutchoice,widget=forms.Select(attrs={'class':'form-control'}))
    color=forms.ChoiceField(choices=colorchoice,widget=forms.Select(attrs={'class':'form-control'}))
    clarity=forms.ChoiceField(choices=claritychoice,widget=forms.Select(attrs={'class':'form-control'}))
    
    