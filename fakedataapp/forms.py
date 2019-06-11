from django import forms

class FakeDataForm(forms.Form):
    fieldnames = forms.CharField(max_length=200, required=True, help_text='Enter space seperated field names.')
    ranges = forms.CharField(max_length=200, required=True, help_text='Enter space seperated range values.')
    datatypes = forms.CharField(max_length=200, required=True, help_text='Enter space seperated datatypes values. i -> integer, c -> varchar')
    class Meta:
        fields = ('fieldnames', 'ranges')
    def clean(self):
        cleaned_data = super(FakeDataForm, self).clean()
        fieldnames = cleaned_data.get('fieldnames')
        ranges = cleaned_data.get('ranges')
        datatypes = cleaned_data.get('datatypes')
        if not fieldnames and not ranges and not datatypes:
            raise forms.ValidationError('You have to write something!')
