from django import forms
from django.utils.text import slugify
from .models import Task
from .models import Project
from register.models import Company
from django.contrib.auth.models import User

STATUS = (
    ('1', 'Pending'),
    ('2', 'In Progress'),
    ('3', 'Done'),
)

DUE = (
    ('1', 'On Due'),
    ('2', 'Overdue'),
    ('3', 'Done'),
)


class DateForm(forms.Form):
    dead_line = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )


class TaskRegistrationForm(forms.ModelForm):
    project = forms.ModelChoiceField(queryset=Project.objects.all())
    assign = forms.ModelMultipleChoiceField(queryset=User.objects.all())
    task_name = forms.CharField(max_length=80)
    status = forms.ChoiceField(choices=STATUS)
    due = forms.ChoiceField(choices=DUE)

    class Meta:
        model = Task
        fields = '__all__'


    def save(self, commit=True):
        task = super(TaskRegistrationForm, self).save(commit=False)
        task.project = self.cleaned_data['project']
        task.task_name = self.cleaned_data['task_name']
        task.status = self.cleaned_data['status']
        task.due = self.cleaned_data['due']
        task.save()
        assigns = self.cleaned_data['assign']
        for assign in assigns:
            task.assign.add((assign))

        if commit:
            task.save()

        return task


    def __init__(self, *args, **kwargs):
        super(TaskRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['project'].widget.attrs['class'] = 'form-control'
        self.fields['project'].widget.attrs['placeholder'] = 'Social Name'
        self.fields['task_name'].widget.attrs['class'] = 'form-control'
        self.fields['task_name'].widget.attrs['placeholder'] = 'Name'
        self.fields['status'].widget.attrs['class'] = 'form-control'
        self.fields['status'].widget.attrs['placeholder'] = 'Email'
        self.fields['due'].widget.attrs['class'] = 'form-control'
        self.fields['due'].widget.attrs['placeholder'] = 'City'
        self.fields['assign'].widget.attrs['class'] = 'form-control'
        self.fields['assign'].widget.attrs['placeholder'] = 'Found date'


class ProjectRegistrationForm(forms.ModelForm):
    name = forms.CharField(max_length=80)
    assign = forms.ModelMultipleChoiceField(queryset=User.objects.all())
    status = forms.ChoiceField(choices=STATUS)
    dead_line = forms.DateField()
    company = forms.ModelChoiceField(queryset=Company.objects.all())
    complete_per = forms.FloatField(min_value=0, max_value=100)
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Project
        fields = '__all__'


    def save(self, commit=True):
        Project = super(ProjectRegistrationForm, self).save(commit=False)
        Project.name = self.cleaned_data['name']
        Project.status = self.cleaned_data['status']
        Project.dead_line = self.cleaned_data['dead_line']
        Project.company = self.cleaned_data['company']
        Project.complete_per = self.cleaned_data['complete_per']
        Project.description = self.cleaned_data['description']
        Project.save()
        assigns = self.cleaned_data['assign']
        for assign in assigns:
            Project.assign.add((assign))

        if commit:
            Project.save()

        return Project
        
        
    def __init__(self, *args, **kwargs):
        super(ProjectRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'Project Name'
        self.fields['status'].widget.attrs['class'] = 'form-control'
        self.fields['status'].widget.attrs['placeholder'] = 'Status'
        self.fields['dead_line'].widget.attrs['class'] = 'form-control'
        self.fields['dead_line'].widget.attrs['placeholder'] = 'Dead Line, type a date'
        self.fields['company'].widget.attrs['class'] = 'form-control'
        self.fields['company'].widget.attrs['placeholder'] = 'Company'
        self.fields['complete_per'].widget.attrs['class'] = 'form-control'
        self.fields['complete_per'].widget.attrs['placeholder'] = 'Complete %'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['placeholder'] = 'Type here the project description...'
        self.fields['assign'].widget.attrs['class'] = 'form-control'
        
        
        
# class ProjectUpdateForm(forms.ModelForm):
#     name = forms.CharField(max_length=80)
#     assign = forms.ModelMultipleChoiceField(queryset=User.objects.all())
#     status = forms.ChoiceField(choices=STATUS)
#     dead_line = forms.DateField()
#     company = forms.ModelChoiceField(queryset=Company.objects.all())
#     complete_per = forms.FloatField(min_value=0, max_value=100)
#     description = forms.CharField(widget=forms.Textarea)

#     class Meta:
#         model = Project
#         fields = '__all__'


#     def save(self, commit=True):
#         Project = super(ProjectUpdateForm, self).save(commit=False)
#         Project.name = self.cleaned_data['name']
#         Project.status = self.cleaned_data['status']
#         Project.dead_line = self.cleaned_data['dead_line']
#         Project.company = self.cleaned_data['company']
#         Project.complete_per = self.cleaned_data['complete_per']
#         Project.description = self.cleaned_data['description']
#         Project.save()
#         assigns = self.cleaned_data['assign']
#         for assign in assigns:
#             Project.assign.add((assign))

#         if commit:
#             Project.save()

#         return Project


#     def __init__(self, *args, **kwargs):
#         super(ProjectUpdateForm, self).__init__(*args, **kwargs)
#         self.fields['name'].widget.attrs['class'] = 'form-control'
#         self.fields['name'].widget.attrs['placeholder'] = 'Project Name'
#         self.fields['status'].widget.attrs['class'] = 'form-control'
#         self.fields['status'].widget.attrs['placeholder'] = 'Status'
#         self.fields['dead_line'].widget.attrs['class'] = 'form-control'
#         self.fields['dead_line'].widget.attrs['placeholder'] = 'Dead Line, type a date'
#         self.fields['company'].widget.attrs['class'] = 'form-control'
#         self.fields['company'].widget.attrs['placeholder'] = 'Company'
#         self.fields['complete_per'].widget.attrs['class'] = 'form-control'
#         self.fields['complete_per'].widget.attrs['placeholder'] = 'Complete %'
#         self.fields['description'].widget.attrs['class'] = 'form-control'
#         self.fields['description'].widget.attrs['placeholder'] = 'Type here the project description...'
#         self.fields['assign'].widget.attrs['class'] = 'form-control'