# Mtables - MaxChubin Tables
Easy to use but nice looking tables for console output
***
## Feauteres
* Many styles
* Aligments data and header
* Indents, shadow
* Table title
* Colors for header, data, borders, title, header background color
* Two ways output table: directly to console or output in pure text format to variable
* No need additional modules or requirements
***
## Available styles
Table borders styles:
* 0 - single line borders and dividers
*	1 - double line borders and dividers
*	2 - double line external borders and single line dividers
*	3 - no external borders, only single line dividers and corners
*	4 - single line external borders with rows and columns marker
*	5 - single line external borders
*	6 - double line external borders with rows and columns marker
*	7 - double line external borders
*	8 - ASCII style 1
*	9 - ASCII style 2
*	10 - formated data with divider crossroads 
*	11 - formated data with corners
*	12 - formated data without divider lines
*	13 - external sinle line border
*	14 - external double line border

![Some style examples](https://downloader.disk.yandex.ru/preview/48b4da814da6b896cc516e01e30f7032d9f305a2911db6049c65017ec798e754/63c5f881/gybyRRz8-BnctoFNloBNdP2FodPtTzNE4YgOEgsKe8l3TUAOyUjC9BilNhOwmZ2dGblCZjR_f5TPO5PHmX2-AQ%3D%3D?uid=0&filename=CNMtables.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=1872x974)


***
## Available colors
* black
* red
* green
* yellow
* blue
* violet
* turquoise
* white
***
## Example 1
```python 
from cooltable import Mtable

table = Mtable (title = "Style 2", data = example_text, style = 2, indent = 1, header = True, alignment = 'center', header_color = 'yellow', shadow_color = 'turquoise', text_color = 'green', borders_color = 'blue', title_color = 'red')

table.show()    # output color table to console

result = table.draw()  # output table to variable in text format
```

## Example 2
```python
from cmntables import CMNtable

if __name__ == "__main__":
	# Примеры использования библиотеки
	# Some examples

	# ВЫВОД ТЕКСТА В РАМКЕ
	# OUTPUT TEXT INTO BORDER
	example_text = 'Test Message'
	# задание цвета строкой
	# set color like a string
	CMNtable(data = example_text, borders_color='grEen', text_color='yeLLow').show()
	CMNtable(data = example_text, style = 1, indent = 3, borders_color = 'grEen', text_color = 'yeLLow').show()
	# задание цвета выбором свойств класса
	# color like class property
	CMNtable(data = example_text, style = 3, indent = 5, borders_color = CMNtable.COLOR_GREEN, text_color = CMNtable.COLOR_YELLOW, shadow_color = CMNtable.COLOR_BLUE).show()
	# выравнивания содержимого ячеек
	# diff aligment text in cells 
	CMNtable(data = [['Multi'],['line'],  ['Text Message']], style = 0, indent = 5, borders_color = CMNtable.COLOR_GREEN, text_color= CMNtable.COLOR_WHITE, alignment = CMNtable.ALIGMENT_LEFT, title = 'Aligment LEFT' ).show()
	CMNtable(data = [['Multi'],['line'],  ['Text Message']], style = 0, indent = 5, borders_color = CMNtable.COLOR_GREEN, text_color = CMNtable.COLOR_YELLOW, shadow_color = CMNtable.COLOR_YELLOW, alignment=CMNtable.ALIGMENT_CENTER, title = 'Aligment CENTER', title_color = CMNtable.COLOR_RED).show()
	CMNtable(data = [['Multi'],['line'],  ['Text Message']], style = 0, indent = 5, borders_color = CMNtable.COLOR_GREEN, text_color = CMNtable.COLOR_YELLOW, shadow_color = CMNtable.COLOR_GREEN, alignment = CMNtable.ALIGMENT_RIGHT, title = 'Aligment RIGHT').show()
	
	# ВЫВОД СТИХОТВОРЕНИЯ В ТАБЛИЧНОМ ВИДЕ ДЛЯ ВЫРАВНИВАНИЯ ПО ЦЕНТРУ
	# POEM OUTPUT WITH CENTER ALIGMENT
	text = '''Люблю грозу в начале мая,|Когда весенний, первый гром,|Как бы резвяся и играя,|Грохочет в небе голубом.|Гремят раскаты молодые,|Вот дождик брызнул, пыль летит,|Повисли перлы дождевые,|И солнце нити золотит.|С горы бежит  проворный,|В лесу не молкнет птичий гам,|И гам лесной и шум нагорный —|Все вторит весело громам.|Ты скажешь: ветреная Геба,|Кормя Зевесова орла,|Громокипящий кубок с неба,|Смеясь, на землю пролила.'''
	example_text = []
	list(map(example_text.append,([t.strip()] for t in text.split('|')))) # преобразуем текст в структуру: STRING --> [[...], [...], [...]]
	CMNtable(data = example_text, style = 14, indent = 2, borders_color = CMNtable.COLOR_GREEN, text_color=CMNtable.COLOR_YELLOW, alignment=CMNtable.ALIGMENT_CENTER, title = 'Автор Ф. И. Тютчев', title_color = CMNtable.COLOR_TURQUOISE, shadow_color = CMNtable.COLOR_BLACK).show()

	# ВЫВОД КОРТЕЖЕЙ
	# TUPLE OUTPUT
	example_text = (0, 1, 2, 3, 4, 5, 6, 7)
	CMNtable(data = example_text, borders_color='blue', text_color='yeLLow', title = 'Tuple output in style 0').show()
	example_text = [(0, 1, 2), (3, 4, 5, 6, 7), (8, 9)]
	CMNtable(data = example_text, style = 1, borders_color = 'violet', text_color = 'turquoise', title = 'Tuple output in style 1', title_color = 'turquoise').show()
	example_text = [(0, 1, 2), (3, 4, 5, 6, 7), (8, 9)]
	CMNtable(data = example_text, style =3,  indent = 2, borders_color = CMNtable.COLOR_GREEN, text_color = CMNtable.COLOR_RED, title = 'Tuple output in style 3. indent = 3', title_color = CMNtable.COLOR_TURQUOISE).show()

	# ВЫВОД СЛОВАРЕЙ
	# DICTIOMARY OUTPUT
	example_text = {'key one' : '1', 'key2': 'Value of key2', 3: 'Three', 4: 4}
	CMNtable(data = example_text, style = 8, indent = 3, borders_color = CMNtable.COLOR_RED, text_color = CMNtable.COLOR_YELLOW, title = 'Dict output in style 8, aligment = left (default)', title_color = CMNtable.COLOR_TURQUOISE).show()
	CMNtable(data = example_text, style = 8, indent = 3, borders_color = CMNtable.COLOR_RED, text_color = CMNtable.COLOR_YELLOW, title = 'Dict output in style 8, aligment = right', title_color = CMNtable.COLOR_TURQUOISE, alignment=CMNtable.ALIGMENT_RIGHT).show()
	CMNtable(data = example_text, style = 8, indent = 3, header = True, borders_color = CMNtable.COLOR_RED, text_color = CMNtable.COLOR_YELLOW, title = 'Dict output in style 9, aligment = center, header = True', title_color = CMNtable.COLOR_TURQUOISE, alignment=CMNtable.ALIGMENT_CENTER).show()

	# ВЫВОД СПИСКОВ
	# LISTS OUTPUT
	example_text = [['X', 'O'],['', 'X', 'O'],['','O', 'X']]
	CMNtable(title = "Style 3. Shadow = True, ", data = example_text, style = 3, indent = 2, borders_color = 'green', text_color = 'white', shadow_color = CMNtable.COLOR_BLACK).show()

	example_text = [
		['Name', 'SName', 'Age', 'E-mail', 'Phone'], # нулевой список содержит имена столбцов
		['Max', 'Chubin', 46, 'max@max.ru', '+7(123)222-33-44'], 
		['Sergey', 'Chubin', 54, 'Sergey@Sergey.ru', '+7(987)111-22-33'], 
		['Kristine', 'Plotnikova', 23, 'kris@kris.ru', '+7(456)321-06-07'], 
		['Elena', 'Ivanova', 43, 'lena@lena.ru', '+7(765)344-23-47']
	]
	# использование цвета фона для заголовков столбцов
	# use header backgroud color
	CMNtable(title = "Style 10. Shadow = True, header background color = RED", data = example_text, style = 10, header=1, indent = 5, borders_color = 'green', text_color = 'white', header_color = CMNtable.COLOR_VIOLET, header_bg_color = CMNtable.COLOR_RED, shadow_color = CMNtable.COLOR_BLACK).show()

	# ВЫВОД ТАБЛИЦЫ В ТЕКСТОВОМ ВИДЕ ДЛЯ ЗАПИСИ В ФАЙЛ БЕЗ ЦВЕТОВОЙ РАЗМЕТКИ МЕТОД DRAW()
	# OUTPUT TABLE IN PURE TEXT FORMAT WITHOUT CONSOLE COLOR MARKUP
	table = CMNtable(title = "Style 0", data = example_text, style = 0, header=1, indent = 5, borders_color='green', text_color = CMNtable.COLOR_GREEN)
	result = table.draw() # формируется текстовая строка, но на экран не выводится
	print(result)
	# f = open('out.txt', 'w') # открываем текстовый файл для записи
	# print(result, file = f) # записываем в него чистый текст без консольной цветовой разметки
	# f.close() # закрываем файл
