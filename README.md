# Задание 1

Для модели курса добавьте в сериализатор поле вывода количества уроков. Поле реализуйте с помощью 
SerializerMethodField() + 

# Задание 2

Добавьте новую модель в приложение users:

1. Платежи:+

- пользователь,
- дата оплаты,
- оплаченный курс или урок,
- сумма оплаты,
- способ оплаты: наличные или перевод на счет.

####   * Поля пользователь,оплаченный курс иотдельно оплаченный урок должны быть ссылками на соответствующие модели.

Запишите в таблицу, соответствующую этой модели данные через инструмент фикстур или кастомную команду.

#### Если вы забыли как работать с фикстурами или кастомной командой - можете вернуться к уроку 20.1 Работа с ORM в Django чтобы вспомнить материал.


# Задание 3+

Для сериализатора для модели курса реализуйте поле вывода уроков. Вывод реализуйте с помощью сериализатора для связанной модели.

#### Один сериализатор должен выдавать и количество уроков курса и информацию по всем урокам курса одновременно.

# Задание 4 +

Настроить фильтрацию для эндпоинта вывода списка платежей с возможностями:

- менять порядок сортировки по дате оплаты,
- фильтровать по курсу или уроку,
- фильтровать по способу оплаты.

#### Дополнительное задание +
Для профиля пользователя сделайте вывод истории платежей, расширив сериализатор для вывода списка платежей