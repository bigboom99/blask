(function () {
  const delButtons = document.querySelectorAll(".task_delete");
  const delButtonsValue = document.querySelectorAll(".task_pred_del_value");

  const tasks = document.querySelectorAll(".task");
  const task_delete_blue_forms = document.querySelectorAll(".task_delete_blue_form");
  const forms_important = document.querySelectorAll(".task_important");
  const tasks_days = document.querySelectorAll(".task_day");
  const task_day_numbers = document.querySelectorAll(".task_day_number");


// Обозначение дня таска
for (let i = 0; i < tasks_days.length; i++) {
    let number_of_day = task_day_numbers[i].textContent-1;
    tasks_days[i].children[number_of_day].classList.add('task_day_active');
  }

  //отправка формы удаления по клику на форму
  let onDelFormClick = function (task_number) {
    return function(evt) {
      task_delete_blue_forms[task_number].submit();
    }
  };
  for (let i = 0; i < task_delete_blue_forms.length; i++) {
      task_delete_blue_forms[i].addEventListener('click', onDelFormClick(i));
    }



  //изменение важности таска по клику на форму
  let onImportantFormClick = function (task_number) {
    return function(evt) {
      forms_important[task_number].submit();
    }
  };
  for (let i = 0; i < forms_important.length; i++) {
      forms_important[i].addEventListener('click', onImportantFormClick(i));
  }

//удаление элементов таска при удалении таска


  let onDelButtonClick = function (task_number) {
    return function(evt) {
      delButtons[task_number].submit();
    }
  };

  for (let i = 0; i < delButtons.length; i++) {
      delButtons[i].addEventListener('click', onDelButtonClick(i));
  }



  for (let i = 0; i < delButtons.length; i++) {
    let task_number = i;
    if (delButtonsValue[i].textContent == 'True') {
      tasks[task_number].children[0].classList.add('task_delete_ok');
      tasks[task_number].children[1].children[0].classList.add('text_line_through');
      tasks[task_number].children[2].classList.add('display_none');
      tasks[task_number].children[1].children[1].classList.add('display_none');
      tasks[task_number].children[3].classList.remove('display_none');
      if (tasks[task_number].children[1].children[2]) {
        tasks[task_number].children[1].children[2].classList.add('display_none');
        if (tasks[task_number].children[1].children[3]) {
            tasks[task_number].children[1].children[3].classList.add('display_none')
        }
      };
    }
    else {
      tasks[task_number].children[0].classList.remove('task_delete_ok');
      tasks[task_number].children[1].children[0].classList.remove('text_line_through');
      tasks[task_number].children[2].classList.remove('display_none');
      tasks[task_number].children[1].children[1].classList.remove('display_none');
      tasks[task_number].children[3].classList.add('display_none');
      if (tasks[task_number].children[1].children[2]) {
        tasks[task_number].children[1].children[2].classList.remove('display_none');
        if (tasks[task_number].children[1].children[3]) {
            tasks[task_number].children[1].children[3].classList.remove('display_none')
        }
      };
    }
  }

})()
