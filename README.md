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

[Samples of Tables Styles 0-3](https://downloader.disk.yandex.ru/preview/ef4c00e54f32bfcd1bb7d6cbfbfd0e77ae763751aabdd772593eb78f01ba536b/63c5eae3/jHmGiDJaKHUAKgMCu6exN-ruuZUdpXf4HrxlC4RJ8rh4bWzYi2A7Mw0cNlCJUBC7GUPDTEgkvvGFHtV6IDYhNA%3D%3D?uid=0&filename=styles0-3.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048)

[Samples of Tables Styles 4-7](https://downloader.disk.yandex.ru/preview/45fac07e72320673aa23a091cf4d9f3010b2311eeb552a3ab3ed0960a0200f03/63c5e959/sudv65zWP8Gz5ucB0BCeEOoLIZijh98BcRIQPTRc0yhCS1L7_-MvL-5-4iKAcF7rToZbwyQ1PIvXEpTY5zrbng%3D%3D?uid=0&filename=styles4-7.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048)

[Samples of Tables Styles 8-11](https://downloader.disk.yandex.ru/preview/85d54ddbdd73f84473024e523bf55faf66168748aca60d80ec7f94abd32fcee0/63c5e98f/Ky2kdmQ9lR4XM8a7ebT9InKlpwby9m-K9YpCtK09Ibbdg4xaVeOmFjZ6TFvzXgJ6n7CWoOmuHTmfvZQzZ0B8QA%3D%3D?uid=0&filename=styles8-12.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048)

[Samples of Tables Style 12](https://downloader.disk.yandex.ru/preview/582086bdf70bced0c01983f6b6a448ef57142c770e1d3c81db5f557a0274f1d8/63c5e9b7/0cKCT-C42tqdrSqHQa5_KBAfhGvjDe7XDjmFdtdy7txEi90_9YIPU_C828C-Nw4wUV4osfieXttjLzUh0kRhew%3D%3D?uid=0&filename=style12.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048)


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

table = Mtable (title = "Style 2", data = example_text, style = 2, indent = 1, header = True, alignment = 'center', header_color = 'yellow', shadow = True, shadow_color = 'turquoise', text_color = 'green', borders_color = 'blue', title_color = 'red')

table.show()    # output color table to console

result = table.draw()  # output table to variable in text format
```

## Example 2
```python
from email import header
from textwrap import indent
from cooltable import Mtable

if __name__ == "__main__":
	# Примеры использования библиотеки
	# Some examples

	# ВЫВОД ТЕКСТА В РАМКЕ
	# OUTPUT TEXT INTO BORDER
	example_text = 'Test Message'
	# задание цвета строкой
	# set color like a string
	Mtable(data = example_text, borders_color='grEen', text_color='yeLLow').show()
	Mtable(data = example_text, style = 1, indent = 3, borders_color = 'grEen', text_color = 'yeLLow').show()
	# задание цвета выбором свойств класса
	# color like class property
	Mtable(data = example_text, style = 3, indent = 5, borders_color = Mtable.COLOR_GREEN, text_color = Mtable.COLOR_YELLOW, shadow_color = Mtable.COLOR_BLUE).show()
	# выравнивания содержимого ячеек
	# diff aligment text in cells 
	Mtable(data = [['Multi'],['line'],  ['Text Message']], style = 0, indent = 5, borders_color = Mtable.COLOR_GREEN, text_color= Mtable.COLOR_WHITE, alignment = Mtable.ALIGMENT_LEFT, title = 'Aligment LEFT' ).show()
	Mtable(data = [['Multi'],['line'],  ['Text Message']], style = 0, indent = 5, borders_color = Mtable.COLOR_GREEN, text_color = Mtable.COLOR_YELLOW, shadow_color = Mtable.COLOR_YELLOW, alignment=Mtable.ALIGMENT_CENTER, title = 'Aligment CENTER', title_color = Mtable.COLOR_RED).show()
	Mtable(data = [['Multi'],['line'],  ['Text Message']], style = 0, indent = 5, borders_color = Mtable.COLOR_GREEN, text_color = Mtable.COLOR_YELLOW, shadow_color = Mtable.COLOR_GREEN, alignment = Mtable.ALIGMENT_RIGHT, title = 'Aligment RIGHT').show()
	
	# ВЫВОД СТИХОТВОРЕНИЯ В ТАБЛИЧНОМ ВИДЕ ДЛЯ ВЫРАВНИВАНИЯ ПО ЦЕНТРУ
	# POEM OUTPUT WITH CENTER ALIGMENT
	text = '''Люблю грозу в начале мая,|Когда весенний, первый гром,|Как бы резвяся и играя,|Грохочет в небе голубом.|Гремят раскаты молодые,|Вот дождик брызнул, пыль летит,|Повисли перлы дождевые,|И солнце нити золотит.|С горы бежит  проворный,|В лесу не молкнет птичий гам,|И гам лесной и шум нагорный —|Все вторит весело громам.|Ты скажешь: ветреная Геба,|Кормя Зевесова орла,|Громокипящий кубок с неба,|Смеясь, на землю пролила.'''
	example_text = []
	list(map(example_text.append,([t.strip()] for t in text.split('|')))) # преобразуем текст в структуру: STRING --> [[...], [...], [...]]
	Mtable(data = example_text, style = 14, indent = 2, borders_color = Mtable.COLOR_GREEN, text_color=Mtable.COLOR_YELLOW, alignment=Mtable.ALIGMENT_CENTER, title = 'Автор Ф. И. Тютчев', title_color = Mtable.COLOR_TURQUOISE, shadow_color = Mtable.COLOR_BLACK).show()

	# ВЫВОД КОРТЕЖЕЙ
	# TUPLE OUTPUT
	example_text = (0, 1, 2, 3, 4, 5, 6, 7)
	Mtable(data = example_text, borders_color='blue', text_color='yeLLow', title = 'Tuple output in style 0').show()
	example_text = [(0, 1, 2), (3, 4, 5, 6, 7), (8, 9)]
	Mtable(data = example_text, style = 1, borders_color = 'violet', text_color = 'turquoise', title = 'Tuple output in style 1', title_color = 'turquoise').show()
	example_text = [(0, 1, 2), (3, 4, 5, 6, 7), (8, 9)]
	Mtable(data = example_text, style =3,  indent = 2, borders_color = Mtable.COLOR_GREEN, text_color = Mtable.COLOR_RED, title = 'Tuple output in style 3. indent = 3', title_color = Mtable.COLOR_TURQUOISE).show()

	# ВЫВОД СЛОВАРЕЙ
	# DICTIOMARY OUTPUT
	example_text = {'key one' : '1', 'key2': 'Value of key2', 3: 'Three', 4: 4}
	Mtable(data = example_text, style = 8, indent = 3, borders_color = Mtable.COLOR_RED, text_color = Mtable.COLOR_YELLOW, title = 'Dict output in style 8, aligment = left (default)', title_color = Mtable.COLOR_TURQUOISE).show()
	Mtable(data = example_text, style = 8, indent = 3, borders_color = Mtable.COLOR_RED, text_color = Mtable.COLOR_YELLOW, title = 'Dict output in style 8, aligment = right', title_color = Mtable.COLOR_TURQUOISE, alignment=Mtable.ALIGMENT_RIGHT).show()
	Mtable(data = example_text, style = 8, indent = 3, header = True, borders_color = Mtable.COLOR_RED, text_color = Mtable.COLOR_YELLOW, title = 'Dict output in style 9, aligment = center, header = True', title_color = Mtable.COLOR_TURQUOISE, alignment=Mtable.ALIGMENT_CENTER).show()

	# ВЫВОД СПИСКОВ
	# LISTS OUTPUT
	example_text = [['X', 'O'],['', 'X', 'O'],['','O', 'X']]
	Mtable(title = "Style 3. Shadow = True, ", data = example_text, style = 3, indent = 2, borders_color = 'green', text_color = 'white', shadow_color = Mtable.COLOR_BLACK).show()

	example_text = [
		['Name', 'SName', 'Age', 'E-mail', 'Phone'], # нулевой список содержит имена столбцов
		['Max', 'Chubin', 46, 'max@max.ru', '+7(123)222-33-44'], 
		['Sergey', 'Chubin', 54, 'Sergey@Sergey.ru', '+7(987)111-22-33'], 
		['Kristine', 'Plotnikova', 23, 'kris@kris.ru', '+7(456)321-06-07'], 
		['Elena', 'Ivanova', 43, 'lena@lena.ru', '+7(765)344-23-47']
	]
	# использование цвета фона для заголовков столбцов
	# use header backgroud color
	Mtable(title = "Style 10. Shadow = True, header background color = RED", data = example_text, style = 10, header=1, indent = 5, borders_color = 'green', text_color = 'white', header_color = Mtable.COLOR_VIOLET, header_bg_color = Mtable.COLOR_RED, shadow_color = Mtable.COLOR_BLACK).show()

	# ВЫВОД ТАБЛИЦЫ В ТЕКСТОВОМ ВИДЕ ДЛЯ ЗАПИСИ В ФАЙЛ БЕЗ ЦВЕТОВОЙ РАЗМЕТКИ МЕТОД DRAW()
	# OUTPUT TABLE IN PURE TEXT FORMAT WITHOUT CONSOLE COLOR MARKUP
	table = Mtable(title = "Style 0", data = example_text, style = 0, header=1, indent = 5, borders_color='green', text_color = Mtable.COLOR_GREEN)
	result = table.draw() # формируется текстовая строка, но на экран не выводится
	print(result)
	# f = open('out.txt', 'w') # открываем текстовый файл для записи
	# print(result, file = f) # записываем в него чистый текст без консольной цветовой разметки
	# f.close() # закрываем файл
