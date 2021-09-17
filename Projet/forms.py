from django.db.models import fields
from .models import * 
from django import forms
from django.core.exceptions import ValidationError

class ProjectForm(forms.ModelForm):
    
    class Meta:
        model = Projet 
        fields=('name','description','slug','category','team',"Final_D","Start_D",'is_done')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control mb-3 rounded-pill'})
        self.fields['team'].widget.attrs.update(
            {'class': 'form-control mb-3 rounded-pill'})
        self.fields['description'].widget.attrs.update(
            {'class': 'form-control mb-3 ', 'placeholder': 'Description'})
        self.fields['slug'].widget.attrs.update(
            {'class': 'form-control mb-3 rounded-pill', 'placeholder': 'Default' , 'value':'Default'})
        self.fields['category'].widget.attrs.update(
            {'class': 'form-control mb-3 rounded-pill', 'placeholder': 'email'})
        self.fields['Final_D'].widget.attrs.update(
            {'class': 'form-control mb-3 rounded-pill' ,'placeholder':'YYYY-MM-DD'})
        self.fields['Start_D'].widget.attrs.update(
            {'class': 'form-control mb-3 rounded-pill' ,'placeholder':'YYYY-MM-DD'})
class CategoryForm(forms.ModelForm):
    """Form definition for Category."""

    class Meta:
        """Meta definition for Categoryform."""

        model = P_category
        fields = ('name','slug')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control mb-3 rounded-pill'})
        self.fields['slug'].widget.attrs.update(
            {'class': 'form-control mb-3 rounded-pill', 'placeholder': 'Default' , 'value':'Default'})
class TaskForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = ("Project_name","T_name","user","Final_D","Start_D","slug")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Project_name'].widget.attrs.update(
            {'class': 'form-control mb-3 rounded-pill'})
        self.fields['T_name'].widget.attrs.update(
            {'class': 'form-control mb-3 rounded-pill'})
        self.fields['user'].widget.attrs.update(
            {'class': 'form-control mb-3 rounded-pill'})
        self.fields['Final_D'].widget.attrs.update(
            {'class': 'form-control mb-3 rounded-pill' ,'placeholder':'YYYY-MM-DD'})
        self.fields['Start_D'].widget.attrs.update(
            {'class': 'form-control mb-3 rounded-pill' ,'placeholder':'YYYY-MM-DD'})
        self.fields['slug'].widget.attrs.update(
            {'class': 'form-control mb-3 rounded-pill', 'placeholder': 'Default' , 'value':'Default'})

class UpdateTaskForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = ("Project_name","T_name","user","Final_D","Start_D","progress","is_done","slug")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Project_name'].widget.attrs.update(
            {'class': 'form-control mb-3 rounded-pill'})
        self.fields['T_name'].widget.attrs.update(
            {'class': 'form-control mb-3 rounded-pill'})
        self.fields['user'].widget.attrs.update(
            {'class': 'form-control mb-3 rounded-pill'})
        self.fields['progress'].widget.attrs.update(
            {'class': 'form-control mb-3 rounded-pill'})
        self.fields['Final_D'].widget.attrs.update(
            {'class': 'form-control mb-3 rounded-pill' ,'placeholder':'YYYY-MM-DD'})
        self.fields['Start_D'].widget.attrs.update(
            {'class': 'form-control mb-3 rounded-pill' ,'placeholder':'YYYY-MM-DD'})
        self.fields['slug'].widget.attrs.update(
            {'class': 'form-control mb-3 rounded-pill', 'placeholder': 'Default' , 'value':'Default'})

    def verfprogress(self):
        prog = self.cleaned_data['progress']
        if prog < 100 :
            pass
        else:
            raise form.ValidationError("Progress should be less or equal to 100") 
        return prog
     




