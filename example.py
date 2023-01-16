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
