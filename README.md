Плагин Text List Formatter.py, который позволяет форматировать выделенный текст в редакторе Notepad++ в формат списка. 
Код разбивает выделенный текст на отдельные строки, добавляет префикс "!list[i ] = '/строка'" для каждой строки и заменяет выделенный текст новым отформатированным текстом. Кроме того, код добавляет строку "do !line values !list enddo" в конец текста. Если текст не был выделен, выводится сообщение с просьбой сначала выделить текст.

Запустить его можно, разместив файл в папке Notepad++\plugins\PythonScript\scripts \.
Затем открыть текстовый файл, который требует изменений в Notepad ++ -> выделить текст и кликнуть на ->plugins\PythonScript\scripts \Text List Formatter

Чтобы добавить его кнопку на панель инструментов и сделать возможным запуск по клавиатурному сочетанию, в настройках плагина (Plugins\Python Script\Configuration) выбираем созданный нами скрипт и добавляем его в меню и на панель инструментов. Теперь после перезапуска Notepad++ соответствующая кнопка появится на панели инструментов.
