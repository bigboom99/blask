(function () {
  const form = document.querySelector(".task_form");

  const settings_open_btn = document.querySelector(".menu_btn");
  const settings_close_btn = document.querySelector(".menu_back_btn");
  const settings_close_btn_toTasks = document.querySelector(".buttom_black");

  const checkbox_icon_mini = document.querySelector(".checkbox_icon-mini");
  const checkbox_icon_bot = document.querySelector(".checkbox_icon-bot");

  const main_container = document.querySelector(".main-container");
  const settings_container = document.querySelector(".settings_container");

  const wrap = document.querySelector(".wrap");


//открытие настроек
let onSettingsOpenBtnClick = function () {
  main_container.classList.add('visually-hidden');
  settings_container.classList.remove('visually-hidden');
  wrap.classList.add('fixed_wrap');
}
settings_open_btn.addEventListener('click', onSettingsOpenBtnClick);

//закрытие настроек
let onSettingsCloseBtnClick = function () {
  main_container.classList.remove('visually-hidden');
  settings_container.classList.add('visually-hidden');
  if (form.classList.contains('visually-hidden')) {
    wrap.classList.remove('fixed_wrap');
  }
}
settings_close_btn.addEventListener('click', onSettingsCloseBtnClick);
settings_close_btn_toTasks.addEventListener('click', onSettingsCloseBtnClick);

//Анимации чекбоксов
let onIconBotClick = function () {
  checkbox_icon_bot.classList.toggle('checkbox_icon');
  checkbox_icon_bot.classList.toggle('checkbox_icon_active');
  }
  checkbox_icon_bot.addEventListener('click', onIconBotClick);
})()
