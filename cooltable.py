#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Max N Chubin <chubinmax@yandex.ru>
@Date: 2022-04-14
"""
class Mtable:
	'''
	Max Chubin <chubinmax@yandex.r>
	MaxTable - data output in tabular form.
	Many styles of borders, different colors for borders, title, header, data, intends for best look
	'''
	# символы для отрисовки узлов таблицы
	styles = [	['┌','─','┐','└','┘','│','┬','┴','┼','├','┤','│','─'],	# 0
 				['╔','═','╗','╚','╝','║','╦','╩','╬','╠','╣','║','═'],	# 1
				['╔','═','╗','╚','╝','║','╤','╧','┼','╟','╢','│','─'],	# 2
				['┌',' ','┐','└','┘',' ',' ',' ','┼',' ',' ','│','─'],	# 3
				['┌','─','┐','└','┘','│','┬','┴',' ','├','┤',' ',' '],	# 4
				['┌','─','┐','└','┘','│','─','─',' ','│','│',' ',' '],	# 5
				['╔','═','╗','╚','╝','║','╤','╧',' ','╟','╢',' ',' '],	# 6
				['╔','═','╗','╚','╝','║','═','═',' ','║','║',' ',' '],	# 7
				['+','-','+','+','+','|','-','-','+','|','|','|','-'],	# 8
				['+','=','+','+','+','|','=','=','+','|','|','|','='],	# 9
				['┌',' ','┐','└','┘',' ','┬','┴','┼','├','┤',' ',' '],	# 10
				['┌',' ','┐','└','┘',' ',' ',' ',' ',' ',' ',' ',' '],	# 11
				[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']	# 12
			]
	text_colors = {
		'black': 	30,
		'red': 		31,
		'green': 	32,
		'yellow':	33,
		'blue': 	34,
		'violet': 	35,
		'turquoise': 36,
		'white': 	37,
	}
	def color(self, text, color = 'white', bold = False, cont = False):
		if self.tofile:
			out = text
		else:
			col = self.text_colors.get(color)
			BOLD = ""
			if bold:
				BOLD = "\033[1m"
			if cont:
				fin = ""
			else:
				fin = "\033[0m"
			out = f"{BOLD}\033[{col}m{text}{fin}"
		return out

	# символы для отрисовки тени
	shadow_symbol = ['▐','▀']

	def __init__(self, title = '', title_color = 'white', header = False, header_alignment = 'center', header_color = 'white', data = [[' ']], alignment = 'left', style = 0, shadow = False, shadow_color = 'white', indent = 0, text_color = 'white', borders_color = 'white'):
		'''
		Вывод данных в табличном виде.

		Подпись таблицы:
		title = 'Table title'

		Цвет подписи таблицы:
		title_color = 'white'

		Заголовок:
		header = True - выделять первую строку ЗАГЛАВНЫМИ БУКВАМИ

		Выравнивание заголовков столбцов:
		header_alignment = 'left/center/right' - по умолчанию left. Выравнивание применяется только если параметра header = True
		
		Цвет заголовков таблицы:
		header_color = 'white'

		Данные:
		data = [[1,'Ivan','Petrov],[2,'Max','Chubin']]
		передаются в виде списка списков:
		[ [1,'Ivan','Petrov], [2,'Max','Chubin'] ]

		Выравнивание содержимого столбцов:
		alignment = 'left/center/right' - по умолчанию left

		Цвет текста в таблице:
		text_color = 'white'

		Table borders styles:
		* 	0 - single line borders and dividers
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

		Цвет тиний таблицы:
		borders_color = 'white'

		Тень:
		shadow = True - включить тень

		Цвет тени:
		shadow_color = 'white'

		Отступы текста от границ:
		indent = 0 

		Доступные цвета:
		'black' 	черный
		'red' 		красный
		'green' 	зеленый
		'yellow'	желтый,
		'blue'	 	синий
		'violet' 	фиолетовый
		'turquoise'	бирюзовый
		'white' 	белый

		ПРИМЕР:
		tbl1 = Table(title = 'Table title', header = True, header_alignment = 'center', data = [[1,'Ivan','Petrov],[2,'Max','Chubin']], alignment = 'left', style = 2, indent = 3)
		tbl.show()
		'''
		style = int(style)
		if style > len(self.styles):
			style = 0
		self.symbols = self.styles[style]
		self.title = title
		self.header = header
		self.shadow = shadow
		self.alignment = alignment.lower()
		self.header_alignment = header_alignment.lower()
		self.indent = int(indent)
		self.text_color = text_color.lower()
		self.borders_color = borders_color.lower()
		self.title_color = title_color.lower()
		self.header_color = header_color.lower()
		self.shadow_color = shadow_color.lower()
		self.tofile = False

		if type(data) == str:
			data = [[data]]
		elif type(data[0]) == str:
			data = [data]
		self.data = data
		self.rows = len(data)
		self.columns = len(data[0])
		self.columns_max = self.__max_len(self.data)
		self.table_width = self.__sum(self.columns_max) + 2 + self.columns

	def show(self):
		'''Выводит таблицу с цветовой разметкой в консоль'''
		table = self.__draw()
		for line in table:
			print(line)

	def draw(self):
		'''Возвращает таблицу как текст без консольной цветной разметки'''
		self.tofile = True
		table = self.__draw()
		result = ''
		for line in table:
			result += line + '\n'
		return result

	def __max_len(self, data):
		'''Поиск максимальной длины слов в столбце'''
		columns_max = []
		for column_number in range(self.columns):
			max_len = 0
			for line_number in range(self.rows):
				item_len = len(str(self.data[line_number][column_number])) + self.indent*2
				if max_len < item_len: 
					max_len = item_len
			columns_max.append(max_len)    
		return columns_max

	def __sum(self, data):
		'''Подсчет суммы длин всех слов в строке таблицы'''
		sum = 0
		for item in data:
			sum += item
		return sum
	
	def __draw(self):
		'''Отрисовка таблицы с содержимым'''
		table = []
		if self.title:
			table.append(self.color(self.title, self.title_color))
		# создание верхней линии
		top_line = self.color(self.symbols[0], self.borders_color, cont = 1)
		for t in range(len(self.columns_max) ):
			top_line = top_line + self.symbols[1]*self.columns_max[t]
			if t < len(self.columns_max)-1: 
				top_line += self.symbols[6]
		top_line += self.color(self.symbols[2],self.borders_color)

		# создание нижней линии
		bottom_line = self.color(self.symbols[3], self.borders_color, cont = 1)
		for t in range(len(self.columns_max)):
			bottom_line = bottom_line + self.symbols[1]*self.columns_max[t]
			if t < len(self.columns_max)-1:
				bottom_line += self.symbols[7]
		bottom_line += self.color(self.symbols[4], self.borders_color)
		if self.shadow:
				bottom_line += self.color(self.shadow_symbol[0], self.shadow_color)

		# создание средней линии
		middle_line = self.color(self.symbols[9], self.borders_color, cont = 1)
		for t in range(len(self.columns_max)):
			middle_line = middle_line + self.symbols[12]*self.columns_max[t]
			if t < len(self.columns_max)-1:
				middle_line += self.symbols[8]
		middle_line += self.color(self.symbols[10],self.borders_color)
		if self.shadow:
				middle_line += self.color(self.shadow_symbol[0], self.shadow_color)

		table.append(top_line)

		# тело таблицы
		for line_number in range(self.rows):
			line = ''
			line += self.color(self.symbols[5], self.borders_color)
			for column_number in range(self.columns):
				cell = ' ' * self.indent + str(self.data[line_number][column_number]) + ' ' * self.indent
				if line_number == 0 and self.header:
					# для первой строки таблицы  используем параметр выравнивания как для заголовка
					cell = cell.upper()
					aligment = self.header_alignment
					color = self.header_color
				else:
					# для остальных строк используем параметр выравнивания для содержимого
					aligment = self.alignment
					color = self.text_color
				if aligment == 'right':
					line += self.color(cell.rjust(self.columns_max[column_number]), color)
				elif aligment == 'center':
					line += self.color(cell.center(self.columns_max[column_number]), color)
				else:
					line += self.color(cell.ljust(self.columns_max[column_number]), color)
				if column_number < len(self.columns_max) - 1:
					line += self.color(self.symbols[11], self.borders_color)
			line += self.color(self.symbols[5], self.borders_color)
			if self.shadow:
				line += self.color(self.shadow_symbol[0], self.shadow_color)
			table.append(line)
			if line_number < self.rows - 1:
				table.append(middle_line)
		table.append(bottom_line)
		if self.shadow:
			table.append('  ' + self.color(self.shadow_symbol[1] * (self.table_width - 2), self.shadow_color))
		return table
