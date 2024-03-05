# -*- coding: utf-8 -*-

import re

# Получаем текст, выделенный пользователем
selected_text = editor.getSelText()

# Если есть выделенный текст
if selected_text:
    # Разбиваем текст на строки
    lines = selected_text.split('\r\n')

    # Начинаем формировать результат
    result = []
    for i, line in enumerate(lines, start=1):
        # Формируем новую строку согласно заданному формату
        formatted_line = "!list[{0} ] = '/{1}'".format(i, line)
        result.append(formatted_line)

    # Преобразуем список обратно в строку для вставки
    result_text = '\n'.join(result)

    # Заменяем выделенный текст на новый, отформатированный текст
    editor.replaceSel(result_text)
    # Добавляем строку в конце текста
    editor.addText('\n do !line values !list\n\nenddo')
else:
    # Если текст не был выделен, выводим сообщение
    notepad.messageBox('Please select some text first.', 'No Text Selected')
    
