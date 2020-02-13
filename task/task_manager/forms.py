from django import forms
from .models import TaskModel

class FormHandler(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['header', 'description', 'personId',  'task_date', 'task_time', 'important', 'one_day', 'one_hour', 'minutes', 'remind_date', 'remind_time']

        widgets = {
            'header': forms.TextInput(attrs={'class': 'task_name', 'placeholder': "Название задачи..."}),
            'description': forms.TextInput(attrs={'class': 'task_comment', 'placeholder': "Комментарий к задаче..."}),
            'personId': forms.TextInput(attrs={'class': 'form_personId visually-hidden'}),
            'important': forms.TextInput(attrs={'class': 'visually-hidden make_important_activate_input', 'type': 'checkbox'}),
            'task_date': forms.TextInput(attrs={'class': 'task_date_input', 'type': 'text', 'placeholder': 'Дата', 'disabled': 'true', 'onfocus': "(this.type='date')", 'onblur': "if(this.value==''){this.type='text'}"}),
            'task_time': forms.TextInput(attrs={'class': 'task_time_input', 'type': 'text', 'placeholder': 'Время', 'disabled': 'true', 'onfocus': "(this.type='time')", 'onblur': "if(this.value==''){this.type='text'}"}),
            'remind_date': forms.TextInput(attrs={'class': 'remind_date_input', 'type': 'text', 'placeholder': 'Дата', 'disabled': 'true', 'onfocus': "(this.type='date')", 'onblur': "if(this.value==''){this.type='text'}"}),
            'remind_time': forms.TextInput(attrs={'class': 'remind_time_input', 'type': 'text', 'placeholder': 'Время', 'disabled': 'true', 'onfocus': "(this.type='time')", 'onblur': "if(this.value==''){this.type='text'}"}),
            'one_day': forms.TextInput(attrs={'class': 'visually-hidden certain_time_btn', 'type': 'checkbox', 'value': '1 день'}),
            'one_hour': forms.TextInput(attrs={'class': 'visually-hidden certain_time_btn', 'type': 'checkbox', 'value': '1 час'}),
            'minutes': forms.TextInput(attrs={'class': 'visually-hidden certain_time_btn', 'type': 'checkbox', 'value': '30 мин'})
            }
            
            
            # 'important': forms.TextInput(attrs={'class': 'visually-hidden'}),
            # 'task_date': forms.DateInput(attrs={'class': 'task_date', 'type': 'date'}),
            # 'task_time': forms.TimeInput(attrs={'class': 'task_time', 'type': 'time'}),
            # 'remind_date': forms.DateInput(attrs={'class': 'remind_date', 'type': 'date'}),
            # 'remind_time': forms.TimeInput(attrs={'class': 'remind_time', 'type': 'time'}),
           
    
    
    
    
    
    
    
    
    
    
    
    
    # header = forms.CharField(max_length=200, required=False)
    # description = forms.CharField(max_length=200, required=False)
    # personId = forms.CharField(max_length=50, required=False)
    # task_date = forms.DateField()
    # task_time = forms.TimeField()
    # remind_date = forms.DateField()
    # remind_time = forms.TimeField()
    
    # Person = forms.ModelChoiceField(queryset=PersonModel.objects.all())
    
    # header.widget.attrs.update({'class': 'task_name', 'placeholder': "Название задачи..."})
    # description.widget.attrs.update({'class': 'task_comment', 'placeholder': "Комментарий к задаче..."})
    # # task_date.widget.attrs.update({'class': 'task_date', 'type': 'date'})
    # # task_time.widget.attrs.update({'class': 'task_time', 'type': 'time'})
    # # remind_date.widget.attrs.update({'class': 'remind_date', 'type': 'date'})
    # # remind_time.widget.attrs.update({'class': 'remind_time', 'type': 'time'})
    
    # def save(self):
    #     new_task = TaskModel.objects.create(
    #         header=self.cleaned_data['header'],
    #         description=self.cleaned_data['description'],
    #         # task_date=self.cleaned_data['task_date'],
    #         # task_time=self.cleaned_data['task_time'],
    #         # remind_date=self.cleaned_data['remind_date'],
    #         # remind_time=self.cleaned_data['remind_time'],
    #         personId=self.cleaned_data['description']user_id
    #     )
    #     return new_task