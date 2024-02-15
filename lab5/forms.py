from django import forms

class FeedbackForm(forms.Form):
    my_message = forms.CharField(label='Feedback Message', widget=forms.Textarea)
    your_name = forms.CharField(max_length=50)
    review_area = forms.MultipleChoiceField(choices=[('food','Food'),('srvc','Service'),('amb','Ambiance'),('eugh','Angry Staff Members'),('gross','Cleanliness')],
        widget=forms.CheckboxSelectMultiple)

    def clean_my_message(self):

        my_message: str = self.cleaned_data.get('my_message')

        if "a" in my_message:
            raise forms.ValidationError(f"message must not contain 'a'the message was '{my_message}'")
        if "terrible" in my_message:
            raise forms.ValidationError(f"We don't accept bad reviews. You said: 'terrible' '{my_message}'")
        
        return my_message

