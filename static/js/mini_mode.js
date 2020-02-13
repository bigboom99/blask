(function () {
  const mini_mode_form = document.querySelector(".mini_mode_form");
  const checkbox_icon_mini = document.querySelector(".checkbox_icon-mini");
  const mini_mode_active = document.querySelector(".person_mini_mode_value");
  const tasks = document.querySelectorAll(".task");
  const forms_important = document.querySelectorAll(".task_important");




  let onMiniFormClick = function () {
     mini_mode_form.submit();
  };
  checkbox_icon_mini.addEventListener('click', onMiniFormClick);
  if (mini_mode_active.classList.contains('True')) {
    checkbox_icon_mini.classList.add('checkbox_icon_active');
    for (let i = 0; i < tasks.length; i++) {
      let task_number = i;
      // tasks[task_number].children[2].classList.remove('display_none');
      if (tasks[task_number].children[1].children[1]) {
        tasks[task_number].children[1].children[1].remove();
      }
      if (tasks[task_number].querySelector(".task_date")) {
        tasks[task_number].querySelector(".task_date").remove();
      }
      if (tasks[task_number].querySelector(".task_day")) {
        tasks[task_number].querySelector(".task_day").remove();
      }
      forms_important[task_number].classList.add('task_important_mini');
    }
  }


})()
