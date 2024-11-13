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
    <tr align="left">
        <th>Свойство</th>
        <th>Описание</th>
    </tr>
    <tr align="left">
        <td>Первый стандартный цвет</td>
        <td><code>firstDefaultColor</code></td>
    </tr align="left">
        <tr>
        <td>Второй стандартный цвет</td>
        <td><code>secondDefaultColor</code></td>
    </tr align="left">
        <tr>
        <td>Первый акцентный цвет</td>
        <td><code>firstAccentColor</code></td>
    </tr align="left">
        <tr>
        <td>Второй акцентный цвет</td>
        <td><code>secondAccentColor</code></td>
    </tr>
</table>

Каждое свойство принимает в себя любое колличество значений.  
Цвета кодируются встроенными средствами языка Python:

<table>
    <tr>
        <th align="left">Цвет</th>
        <th>Текст</th>
        <th>Фон</th>
    </tr>
    <tr>
        <td>Черный</td>
        <td align="center"><code>30</code></td>
        <td align="center"><code>40</code></td>
    </tr>
    <tr>
        <td>Красный</td>
        <td align="center"><code>31</code></td>
        <td align="center"><code>41</code></td>
    </tr>
    <tr>
        <td>Зеленый</td>
        <td align="center"><code>32</code></td>
        <td align="center"><code>42</code></td>
    </tr>
    <tr>
        <td>Жёлтый</td>
        <td align="center"><code>33</code></td>
        <td align="center"><code>43</code></td>
    </tr>
    <tr>
        <td>Синий</td>
        <td  align="center"><code>34</code></td>
        <td  align="center"><code>44</code></td>
    </tr>
    <tr>
        <td>Фиолетовый</td>
        <td align="center"><code>35</code></td>
        <td align="center"><code>45</code></td>
    </tr>
    <tr>
        <td>Бирюзовый</td>
        <td align="center"><code>36</code></td>
        <td align="center"><code>46</code></td>
    </tr>
    <tr>
        <td>Белый</td>
        <td align="center"><code>37</code></td>
        <td align="center"><code>47</code></td>
    </tr>
    <tr>
        <td>Сброс</td>
        <td align="center" colspan=2><code>0</code></td>
    </tr>
</table>

В случае, если в свойство будет передан неправильный параметр или параметров не будет вовсе, это будет расценено как сброс стилизации (0)

### clearTerminal
Хранит в себе булевое значение. Отвечает за отчистку терминала перед выводом.
### showTime
Хранит в себе булевое значение. Отвечает за вывод времени в консоли.