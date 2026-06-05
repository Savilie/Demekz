=== СТРУКТУРА ПРОЕКТА ===

main.py              — точка входа (запускай её)
config.py            — настройки (пароль MySQL, цвета, шрифт)
database.py          — работа с MySQL (запросы к БД)
run.bat              — запуск двойным кликом
resources/           — фото товаров (20 шт.), иконка, заглушка
windows/
    auth_window.py          — окно авторизации
    main_window.py          — список товаров + детали
    product_edit_window.py  — форма добавления/редактирования товара
    order_list_window.py    — список заказов
    order_edit_window.py    — форма добавления/редактирования заказа

database_install/    — скрипты для создания БД
    create_db.sql           — создание таблиц
    insert_data.sql         — наполнение данными
    chitaigorod_dump.sql    — дамп БД

block_scheme_and_erd/ — ER-диаграмма и блок-схема


=== БЫСТРЫЙ СТАРТ ===

1. Открыть config.py, вписать пароль MySQL:
   "password": "твой_пароль"

2. Создать БД (в MySQL Workbench или cmd):
   source database_install/create_db.sql
   source database_install/insert_data.sql

3. Запустить:
   - Двойным кликом по run.bat
   - Или: python main.py


=== КАК ПОМЕНЯТЬ ВНЕШНИЙ ВИД ===

Цвета, шрифт — в config.py:
  FONT_FAMILY = "Comic Sans MS"     — шрифт
  COLOR_MAIN_BG = "#FFFFFF"          — основной фон
  COLOR_SECONDARY_BG = "#ABCFCE"    — доп. фон
  COLOR_ACCENT = "#546F94"           — акцент

Расположение элементов — в windows/main_window.py:
  Метод _build_ui() — вся вёрстка
  Строки с side="left"/"right"/"top"/"bottom" — положение блоков
  pack(), grid() — способ расположения

Окна авторизации — windows/auth_window.py
Формы товара — windows/product_edit_window.py
Заказы — windows/order_list_window.py и order_edit_window.py


=== ДАННЫЕ ДЛЯ ВХОДА ===

Логины и пароли в user_import.xlsx, основные:
  Админ: 94d5ous@gmail.com / uzWC67
  Менеджер: ptec8ym@yahoo.com / LdNyos
  Клиент: yzls62@outlook.com / JlFRCZ
  Гость: кнопка "Войти как гость"
