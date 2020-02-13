from __future__ import unicode_literals
from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import get_object_or_404, render, redirect
from .forms import FormHandler
from .models import TaskModel, PersonModel
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .utils import ObjectDetailMixin
import requests

import xml.etree.ElementTree as ET
import vk_api
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

from django.views.decorators.csrf import csrf_exempt
import json
import vk


class TaskCreate(View):
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

    def get(self, request):
        user_id = request.GET.get("vk_user_id", "")
        if not(user_id):
            user_id = 0
        form = FormHandler()

        try:
            person = PersonModel.objects.get(person_id=user_id)
        except PersonModel.DoesNotExist:
            newPerson = PersonModel(person_id=user_id)
            newPerson.save()

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

    def post(self, request):
             bound_form = FormHandler(request.POST)
             new_task = bound_form.save()
             user_id = request.POST.get('personId','')
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


class TaskDelete(ObjectDetailMixin, View):
    def post_update(self):
        task_delete = self.task
        task_delete.delete()


class TaskImportant(ObjectDetailMixin, View):
    def post_update(self):
        task_important = self.task
        if task_important.important:
            task_important.important = False
        else:
            task_important.important = True

        task_important.save()


class TaskPredDel(ObjectDetailMixin, View):
    def post_update(self):
        task = self.task
        if task.pred_del:
            task.pred_del = False
        else:
            task.pred_del = True

        task.save()


class TaskMiniMode(View):
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

    def post(self, request, user_id):
        person = PersonModel.objects.get(person_id=user_id)
        if person.mini_mode:
            person.mini_mode = False
        else:
            person.mini_mode = True

        person.save()

        form = FormHandler()
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


class TaskUpdate(View):
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

    def post(self, request, task_id):
             old_task = TaskModel.objects.get(id=task_id)
             old_task.delete()

             bound_form = FormHandler(request.POST)
             new_task = bound_form.save()
             user_id = request.POST.get('personId','')
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


@csrf_exempt
def taskBot(request):
    token = 'e19c12c1bdb9061452e642730058a307ea5cebe79d9db7c12bfd1ca82b9d0e84af724325b595336da2ee8'
    confirmation_token = '7fd0d0c9'
    secret_key = 'skjvdvlsdmvd'
    first_answer = 'Привет, это агрегатор игр GameDiscount.ru. Выбери функцию и мы найдем для тебя лучшее предложение'
    game_name = 'Введи название игры'

    if (request.method == "POST"):
        data = json.loads(request.body)
        if (data['secret'] == secret_key):
            if (data['type'] == 'confirmation'):
                return HttpResponse(confirmation_token, content_type="text/plain", status=200)
            if (data['type'] == 'message_new'):  # if VK server send a message
                vk_session = vk_api.VkApi(token=token)
                vk = vk_session.get_api()
                user_id = data['object']['user_id']
                message = data['object']['body']
                if (message == 'Начать'):
                    keyboard = VkKeyboard(one_time=True)

                    keyboard.add_button('Найти игру', color=VkKeyboardColor.PRIMARY)
                    keyboard.add_line()
                    keyboard.add_button('Подписаться на игру', color=VkKeyboardColor.POSITIVE)
                    keyboard.add_line()
                    keyboard.add_vkapps_button(app_id=7289973, owner_id=-191161476, label='Перейти в приложение', hash="sendKeyboard", payload=None)
                    #keyboard.add_vkapps_button(app_id=7289973, owner_id=-181108510, label="Отправить клавиатуру", hash="sendKeyboard")
                    vk.messages.send(message=first_answer, keyboard=keyboard.get_keyboard(), random_id=get_random_id(),
                                     peer_id=user_id)
                elif (message == 'Найти игру'):
                    vk.messages.send(message=game_name, random_id=get_random_id(), peer_id=user_id)
                elif (message):
                    xml = requests.get('https://steam-account.ru/partner/products.xml').text
                    tree = ET.parse(xml)
                    root = tree.getroot()

                    product = tree.find("response/product[name='Aliens vs. Predator Collection']")

                    vk.messages.send(message=str(product), random_id=get_random_id(), peer_id=user_id)
                return HttpResponse('ok', content_type="text/plain", status=200)
    else:
        return HttpResponse('see you :)')
