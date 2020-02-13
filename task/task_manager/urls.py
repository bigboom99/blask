from django.urls import path
from .views import TaskCreate, TaskDelete, TaskImportant, TaskPredDel, TaskMiniMode, TaskUpdate, taskBot


urlpatterns = [
    path('', TaskCreate.as_view(), name='index'),
    path('task_del/<task_id>/<user_id>/', TaskDelete.as_view(), name='task_delete'),
    path('important/<task_id>/<user_id>/', TaskImportant.as_view(), name='task_important'),
    path('pred_del/<task_id>/<user_id>/', TaskPredDel.as_view(), name='task_pred_del'),
    path('mini_mode/<user_id>/', TaskMiniMode.as_view(), name='task_mini_mode'),
    path('task_update/<task_id>/', TaskUpdate.as_view(), name='update'),
    path('task_bot/', taskBot, name='task_bot'),
]
