from django.shortcuts import get_object_or_404, render, redirect
from .forms import FormHandler
from .models import *

class ObjectDetailMixin:
    task = None
    
    def date(self, d, m, y):
        if (m - 2) > 0:
            y = y
        else:
            y - 1
        if (m - 2) > 0:
            m = m - 2
        else:
            12 - abs(m - 2)
        c = y // 100
        y = y % 100
        n = (d + ((13 * m - 1) // 5) + y + (y // 4 + c // 4 - 2 * c + 777)) % 7
        return n 
    
    def post(self, request, task_id, user_id):
        try:
            self.task = TaskModel.objects.get(id=task_id)
            self.post_update()
            form = FormHandler()
            person = PersonModel.objects.get(person_id=user_id)
            try:
                tasks = TaskModel.objects.all().filter(personId=user_id)
                months = [0, 'янв', 'фев', 'мар', 'апр', 'мая', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']
                for task in tasks:
                    if task.task_date:
                        date = task.task_date.split('-')
                        d = int(date[2])
                        m = int(date[1])
                        y = int(date[0])
                        task_day = self.date(d, m, y)
                        if task_day:
                            task.task_day = task_day
                        else:
                            task.task_day = 7
                        if task.task_date and task.task_time:
                            res_date = str(d) +' '+ months[m] + ','
                        else:
                            res_date = str(d) +' '+ months[m]
                        task.task_date_new = res_date
                tasks = sorted(tasks, key=lambda task: task.important, reverse = True)
            except TaskModel.DoesNotExist:
                return render(request, 'task_manager/index.html', context={'form': form, 'user_id': user_id, 'person': person})
            else:
                return render(request, 'task_manager/index.html', context={'tasks': tasks, 'form': form, 'user_id': user_id, 'person': person})
        except TaskModel.DoesNotExist:
            form = FormHandler()
            person = PersonModel.objects.get(person_id=user_id)
            try:
                tasks = TaskModel.objects.all().filter(personId=user_id)
                months = [0, 'янв', 'фев', 'мар', 'апр', 'мая', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']
                for task in tasks:
                    if task.task_date:
                        date = task.task_date.split('-')
                        d = int(date[2])
                        m = int(date[1])
                        y = int(date[0])
                        task_day = self.date(d, m, y)
                        if (task_day):
                            task.task_day = task_day
                        else:
                            task.task_day = 7
                        if task.task_date and task.task_time:
                            res_date = str(d) +' '+ months[m] + ','
                        else:
                            res_date = str(d) +' '+ months[m]
                        task.task_date_new = res_date
                tasks = sorted(tasks, key=lambda task: task.important, reverse = True)
            except TaskModel.DoesNotExist:
                return render(request, 'task_manager/index.html', context={'form': form, 'user_id': user_id, 'person': person})
            else:
                return render(request, 'task_manager/index.html', context={'tasks': tasks, 'form': form, 'user_id': user_id, 'person': person})
            