(function () {
  const all_tasks_descriptions = document.querySelectorAll(".task_description");
  const form = document.querySelector(".task_form");
  const tasks = document.querySelector(".tasks");
  const tasks_important = document.querySelectorAll(".task_important");
  const tasks_id = document.querySelectorAll(".task_id_js");

  const task_name = document.querySelector(".task_name");
  const task_comment = document.querySelector(".task_comment");
  const checkbox_icon_important = document.querySelector(".checkbox_icon_important");
  const checkbox_icon_date = document.querySelector(".checkbox_icon_date");
  const checkbox_icon_reminder = document.querySelector(".checkbox_icon_reminder");
  const certain_times = document.querySelectorAll(".certain_time");
  const certain_times_btns = document.querySelectorAll(".certain_time_btn");
  const task_add_btn = document.querySelector(".task_add");
  const main_footer = document.querySelector(".main_footer");

  const reset_btn = document.querySelector(".reset_btn");
  const submit_btn = document.querySelector(".submit_btn");

  const task_date_input = document.querySelector(".task_date_input");
  const task_time_input = document.querySelector(".task_time_input");
  const remind_date_input = document.querySelector(".remind_date_input");
  const remind_time_input = document.querySelector(".remind_time_input");

  const make_important_activate_input = document.querySelector(".make_important_activate_input");
  const wrap = document.querySelector(".wrap");


  const user_id = document.querySelector(".user_id");
  const form_personId = document.querySelector(".form_personId");



// Передача user_id в python
  form_personId.value = user_id.textContent;



// Закрытие формы
  let onResetBtnClick = function () {
    form.classList.add('visually-hidden');
    tasks.classList.remove('visually-hidden');
    main_footer.classList.remove('visually-hidden');
    wrap.classList.remove('fixed_wrap');
    form.reset();

    if (checkbox_icon_important.classList.contains('checkbox_icon_active')) {
      onIconImportantClick();
    }

    if (checkbox_icon_date.classList.contains('checkbox_icon_active')) {
      onIconDateClick();
    }

    if (checkbox_icon_reminder.classList.contains('checkbox_icon_active')) {
      onIconReminderClick();
    }

    form.setAttribute('action', "/");

  }

    reset_btn.addEventListener('click', onResetBtnClick);
// Открытие формы
  let onTaskAddBtnClick = function () {
    form.classList.remove('visually-hidden');
    tasks.classList.add('visually-hidden');
    main_footer.classList.add('visually-hidden');
    wrap.classList.add('fixed_wrap');


    onIconDateClick();
    onIconReminderClick();

  }

    task_add_btn.addEventListener('click', onTaskAddBtnClick);


// Отправка формы
   let onSubmitBtnClick = function () {
     form.submit();
   }

  submit_btn.addEventListener('click', onSubmitBtnClick);


// Важность таска
  let onIconImportantClick = function () {

    checkbox_icon_important.classList.toggle('checkbox_icon_active');

    if (make_important_activate_input.checked) {
      make_important_activate_input.removeAttribute('checked', true);
      make_important_activate_input.value = 'False';
    }
    else {
      make_important_activate_input.setAttribute('checked', true);
      make_important_activate_input.value = 'True';
    }

  }
  let onIconDateClick = function () {
    task_date_input.classList.toggle('time_input_active');
    task_time_input.classList.toggle('time_input_active');

    if (task_date_input.disabled) {
      task_date_input.removeAttribute('disabled');
      task_time_input.removeAttribute('disabled');
    }
    else {
      task_date_input.setAttribute('disabled', true);
      task_time_input.setAttribute('disabled', true);
      task_date_input.value = '';
      task_time_input.value = '';
    }


    checkbox_icon_date.classList.toggle('checkbox_icon_active');
  }

// Выбор времени напоминания

  let onIconReminderClick = function () {
    let onCertainTimeClick = function (time_mumber) {
      return function(evt) {
        if (certain_times_btns[time_mumber].checked) {
          certain_times_btns[time_mumber].removeAttribute('checked', true);
        }
        else {
          certain_times_btns[time_mumber].setAttribute('checked', true);
        }

        if (certain_times_btns[time_mumber].checked) {
          certain_times[time_mumber].classList.add('certain_time_active')
        } else {
          certain_times[time_mumber].classList.remove('certain_time_active')
        }
      }
    };

    remind_date_input.classList.toggle('time_input_active');
    remind_time_input.classList.toggle('time_input_active');


    checkbox_icon_reminder.classList.toggle('checkbox_icon_active');

    if (remind_date_input.disabled) {
      remind_date_input.removeAttribute('disabled');
      remind_time_input.removeAttribute('disabled');
      for (let i = 0; i < certain_times_btns.length; i++) {
          certain_times[i].addEventListener('click', onCertainTimeClick(i));
      }
    }
    else {
      remind_date_input.setAttribute('disabled', true);
      remind_time_input.setAttribute('disabled', true);
      remind_date_input.value = '';
      remind_time_input.value = '';
      for (let i = 0; i < certain_times_btns.length; i++) {
          certain_times[i].removeEventListener('click', onCertainTimeClick(i));
          certain_times[i].classList.remove('certain_time_active');
          certain_times_btns[i].removeAttribute('checked');
      }
    }
    if (remind_date_input.disabled) {
      for (let i = 0; i < certain_times_btns.length; i++) {
          certain_times[i].addEventListener('click', onCertainTimeClick(i));
      }
    }
    else {
      for (let i = 0; i < certain_times_btns.length; i++) {
          certain_times[i].removeEventListener('click', onCertainTimeClick(i));
          certain_times[i].classList.remove('certain_time_active');
          certain_times_btns[i].removeAttribute('checked');

      }
    }
  }
  checkbox_icon_important.addEventListener('click', onIconImportantClick);
  checkbox_icon_date.addEventListener('click', onIconDateClick);
  checkbox_icon_reminder.addEventListener('click', onIconReminderClick);







  //UPDATE TASK

  let onUpdateTaskClick = function (task_number) {
    return function(evt) {

      //Открываем форму
      form.classList.remove('visually-hidden');
      let update_url = "/task_update/"+tasks_id[task_number].textContent+"/"
      form.setAttribute('action', update_url);
      tasks.classList.add('visually-hidden');
      main_footer.classList.add('visually-hidden');
      wrap.classList.add('fixed_wrap');

     //Заполняем ее данными таска
     task_name.value = all_tasks_descriptions[task_number].children[0].textContent;
     if (all_tasks_descriptions[task_number].querySelector(".task_descript").textContent) {
       task_comment.value = all_tasks_descriptions[task_number].querySelector(".task_descript").textContent;
     }

     //Важность таска
     if (tasks_important[task_number].classList.contains('task_important_True')) {
       onIconImportantClick();
     }

     // Дата таска
     if (all_tasks_descriptions[task_number].querySelector(".task_date_js").textContent) {

       task_date_input.value = all_tasks_descriptions[task_number].querySelector(".task_date_js").textContent;
       if (!checkbox_icon_date.classList.contains('checkbox_icon_active')) {
         onIconDateClick();
       }
     }

     // Время таска
     if (all_tasks_descriptions[task_number].querySelector(".task_time_js").textContent) {
       task_time_input.value = all_tasks_descriptions[task_number].querySelector(".task_time_js").textContent;
       if (!checkbox_icon_date.classList.contains('checkbox_icon_active')) {
         onIconDateClick();
       }
     }

     // Напоминаия времени час или два

     if (all_tasks_descriptions[task_number].querySelector(".task_remind_one_day_js").classList.contains('True')) {
       if (!checkbox_icon_reminder.classList.contains('checkbox_icon_active')) {
         onIconReminderClick();
       }
       onCertainTimeClick(0);
     }
     if (all_tasks_descriptions[task_number].querySelector(".task_remind_one_hour_js").classList.contains('True')) {
       if (!checkbox_icon_reminder.classList.contains('checkbox_icon_active')) {
         onIconReminderClick();
       }
       onCertainTimeClick(1);
     }
     if (all_tasks_descriptions[task_number].querySelector(".task_remind_minutes_js").classList.contains('True')) {
       if (!checkbox_icon_reminder.classList.contains('checkbox_icon_active')) {
         onIconReminderClick();
       }
       onCertainTimeClick(2);
     }

     // Напоминаие точного времени
     // Дата напоминаня таска
     if (all_tasks_descriptions[task_number].querySelector(".task_remind_date_js").textContent) {
       if (!checkbox_icon_reminder.classList.contains('checkbox_icon_active')) {
         onIconReminderClick();
       }
       remind_date_input.value = all_tasks_descriptions[task_number].querySelector(".task_remind_date_js").textContent;
     }

     // Время напоминания таска
     if (all_tasks_descriptions[task_number].querySelector(".task_remind_time_js").textContent) {
       if (!checkbox_icon_reminder.classList.contains('checkbox_icon_active')) {
         onIconReminderClick()
       }
       
       remind_time_input.value = all_tasks_descriptions[task_number].querySelector(".task_remind_time_js").textContent;
     }

     // Функция выбора времени
     let onCertainTimeClick = function (time_mumber) {
       return function(evt) {
         if (certain_times_btns[time_mumber].checked) {
           certain_times_btns[time_mumber].removeAttribute('checked', true);
         }
         else {
           certain_times_btns[time_mumber].setAttribute('checked', true);
         }

         if (certain_times_btns[time_mumber].checked) {
           certain_times[time_mumber].classList.add('certain_time_active')
         } else {
           certain_times[time_mumber].classList.remove('certain_time_active')
         }
       }
     };


    }
  };

  for (let i = 0; i < all_tasks_descriptions.length; i++) {
      all_tasks_descriptions[i].addEventListener('click', onUpdateTaskClick(i));
  }

})()
