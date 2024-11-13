# pyCall

<b>pyCall</b> - это простое консольное приложение, позволяющее узнать расписание, какое занятие идет на данный момент и сколько осталось времени до конца занятия/перемены.

## Взаимодействие с приложением

Для работы приложения на пк должен быть установлен python3. Для единоразового запуска достаточно выполнить файл main.py.  
Для удобства можно сделать bash или sh скрипт с похожим наполнением:

```python3 /lib/calls/main.py;```

## Настройка конфигурации

Вы можете отредактировать конфигурационный файл data-call.json, настроив поведение программы под себя. Файл хранит в себе следующие объекты:

### calls
Хранит в себе вариации расписаний. Имена свойств могут быть любыми. На данный момент этот объект может хранить в себе только 3 свойства, ни больше ни меньше.
### associations
Хранит в ассоциации дней и расписаний.  
Например ```"table_1": [0, 2, 3]``` - расписание под названием "table_1" ассоциировано с 0, 2 и 3 днем недели (понедельник, среда, четверг). Данный объект нужно настраивать для привязки дней недели к расписаниям.
### colors
Данный параметр хранит в себе настройки темы. Всего имеется 4 свойства:

<table>
    <tr>
        <th>Свойство</th>
        <th>Описание</th>
    </tr>
    <tr>
        <td>firstDefaultColor</td>
        <td>первый стандартный цвет</td>
    </tr>
        <tr>
        <td>secondDefaultColor</td>
        <td>второй стандартный цвет</td>
    </tr>
        <tr>
        <td>firstAccentColor</td>
        <td>первый акцентный цвет</td>
    </tr>
        <tr>
        <td>secondAccentColor</td>
        <td>второй акцентный цвет</td>
    </tr>
</table>

Каждое свойство принимает в себя любое колличество значений.  
Цвета кодируются встроенными средствами языка Python:

<table>
    <tr>
        <th>Layer 1</th>
        <th>Layer 2</th>
        <th>Layer 3</th>
    </tr>
</table>

|   Цвет        |   Текст         |   Фон           |
|---------------|-----------------|-----------------|
|   Черный      |   ```30```      |   ```40```      |
|   Красный     |   ```31```      |   ```41```      |
|   Зелениый    |   ```32```      |   ```42```      |
|   Жёлтый      |   ```33```      |   ```43```      |
|   Синий       |   ```34```      |   ```44```      |
|   Фиолетовый  |   ```35```      |   ```45```      |
|   Бирюзовый   |   ```36```      |   ```46```      |
|   Белый       |   ```37```      |   ```47```      |
|   Сброс       |               ```0```             |

В случае, если в свойство будет передан неправильный параметр или параметров не будет вовсе, это будет расценено как сброс стилизации (0)

### clearTerminal
Хранит в себе булевое значение. Отвечает за отчистку терминала перед выводом.
### showTime
Хранит в себе булевое значение. Отвечает за вывод времени в консоли.