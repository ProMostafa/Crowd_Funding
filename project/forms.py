from django import forms
from project.models import Project, ProjectPicture
from django.forms.widgets import DateInput
from django.core.files.images import get_image_dimensions
# from project.models import UserProfile


class ProjectForm(forms.ModelForm):
    images = forms.ImageField(widget=forms.FileInput(attrs={'multiple': True}), required=True, help_text="you can upload more than one image")

    def clean(self):
        start_date = self.cleaned_data.get("start_date")
        end_date = self.cleaned_data.get("end_date")
        if end_date and start_date and end_date < start_date:
            msg = u"End date should be greater than start date."
            self._errors["end_date"] = self.error_class([msg])

    class Meta:
        model = Project
        fields = ['title', 'details', 'total_target', 'start_date', 'end_date', 'tags', 'category']
        widgets = {
            'start_date': DateInput(attrs={'type': 'date'}),
            'end_date': DateInput(attrs={'type': 'date'})
        }

