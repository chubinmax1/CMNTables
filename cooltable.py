#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Max N Chubin <chubinmax@yandex.ru>
@Date: 2023-01-16
"""
class Mtable:
	'''
	Max Chubin <chubinmax@yandex.r>
	MaxTable - data output in tabular form.
	Many styles of borders, different colors for borders, title, header, data, intends and shadow for best look
	'''
	COLOR_BLACK = 30
	COLOR_RED = 31
	COLOR_GREEN = 32
	COLOR_YELLOW = 33
	COLOR_BLUE = 34
	COLOR_VIOLET = 35
	COLOR_TURQUOISE = 36
	COLOR_WHITE = 37

	ALIGMENT_LEFT = 'left'
	ALIGMENT_CENTER = 'center'
	ALIGMENT_RIGHT = 'right'

	def __init__(self, title = '', title_color = 'white', header = False, header_alignment = 'center', header_color = 'white', data = [[' ']], alignment = 'left', style = 0, shadow_color = None, indent = 0, text_color = 'white', borders_color = 'white', header_bg_color = None):
		'''
		Вывод данных в табличном виде.

		Подпись таблицы:
		title = 'Table title'

		Цвет подписи таблицы:
		title_color = 'white'

		Заголовок:
		header = True - выделять первую строку ЗАГЛАВНЫМИ БУКВАМИ

		Выравнивание текста заголовков столбцов столбцов:
		header_alignment = 'left/center/right' - по умолчанию left. Выравнивание применяется только если параметра header = True
		
		Цвет текста заголовков столбцов таблицы:
		header_color = 'white'

		Цвет фона заголовков столбцов таблицы:
		header_bg_color = 'red'

		Данные:
		data = [[1,'Ivan','Petrov],[2,'Max','Chubin']]
		передаются в виде списка списков:
		[ [1,'Ivan','Petrov], [2,'Max','Chubin'] ]

		Выравнивание содержимого столбцов:
		alignment = 'left/center/right' - по умолчанию left

		Цвет текста в таблице:
		text_color = 'white'

		Стили границ таблицы:
		* 	0 - одинарная граница и разделители/singleline borders and dividers
		*	1 - двойная граница и разделители/double line borders and dividers
		*	2 - двойная гнраница и одинарные разделители/double line external borders and single line dividers
		*	3 - без внешней границы, только одинарный разделитель и углы/no external borders, only single line dividers and corners
		*	4 - одинарны граница с маркерами столбцов и строк/single line external borders with rows and columns marker
		*	5 - только одинарная граница/single line external borders
		*	6 - двойная граница с маркерами столбцов и строк/double line external borders with rows and columns marker
		*	7 - только двойная внешняя граница/double line external borders
		*	8 - ASCII style 1
		*	9 - ASCII style 2
		*	10 - отформатированные данные с перекрестиями/formated data with divider crossroads 
		*	11 - отформатированные данные с уголками/formated data with corners
		*	12 - отформатированные данные без разделительных линий/formated data without divider lines
		*	13 - одинарная внешняя рамка/external sinle line border
		*	14 - двойная внешняя рамка/external double line border

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

		# символы для отрисовки узлов таблицы
		self.styles = [	
					['┌','─','┐','└','┘','│','┬','┴','┼','├','┤','│','─'],	# 0
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
					[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],	# 12
					['┌','─','┐','└','┘','│',' ',' ',' ','│','│','│',' '],	# 13
					['╔','═','╗','╚','╝','║',' ',' ',' ','║','║','║',' ']	# 14
				]
		

		self.text_colors = {
			'black': 		30,
			'red': 			31,
			'green': 		32,
			'yellow':		33,
			'blue': 		34,
			'violet': 		35,
			'turquoise': 	36,
			'white': 		37,
		}

		# символы для отрисовки тени
		self.shadow_symbol = ['█','▀']

		try:
			self.style = int(style)
		except Exception as ex:
			self.style = 0
		if style > len(self.styles) or style < 0:
			self.style = 0
		self.symbols = self.styles[style]
		self.title = title.strip()
		self.header = bool(header)
		# self.shadow = bool(shadow)
		self.alignment = alignment.lower()
		self.header_alignment = header_alignment.lower()
		try:
			self.indent = int(indent)
		except Exception as ex:
			self.indent = 0
		if indent > 50:
			indent = 50
		self.text_color 	= self.__checkType(text_color)
		self.borders_color 	= self.__checkType(borders_color)
		self.title_color 	= self.__checkType(title_color)
		self.header_color 	= self.__checkType(header_color)
		self.shadow_color 	= self.__checkType(shadow_color)


		if header_bg_color:
			self.bg_color 	= self.__checkType(header_bg_color) + 10 # цвет фона отличается на 10 от цвета шрифта
		else:
			self.bg_color 	= None

		self.tofile = False
		if isinstance(data, dict): # если передали словарь, то отформатировать в правильный вид
			data = [list(data.keys()), list(data.values())]
		elif isinstance(data, str): # если передали строку, то схавать
			data = [[data]]
		elif isinstance(data[0], str): # если передали список, то отформатировать в правильный вид
			data = [data]
		elif isinstance(data, tuple): # если передали кортеж, то отформатировать в правильный вид
			data = [list(data)]
		self.data = data
		self.rows = len(data)
		# найдем MAX кол-во столбцов перебирая строки 
		self.columns = 0
		for item in data:
			if self.columns < len(item):
				self.columns = len(item)
		self.columns_max = self.__max_len(self.data)
		self.table_width = self.__sum(self.columns_max) + 2 + self.columns
	
	def __checkType(self, param):
		'''Если цвет был передан строкой то приводим к нижнему регистру, а если числом, то возвращаем это число. В случае неправильного типа задаем цвет  WHITE = 37'''
		if isinstance(param, str):
			return param.lower()
		elif isinstance(param, int):
			return param
		else:
			return 37
		

	@property
	def style_counter(self):
		'''максимально доступное количество стилей'''
		return len(self.styles)

	def color(self, text, color = 'white', bg = None, bold = False, cont = False):
		if self.tofile:
			out = text
		else:
			if isinstance(color, str):
				col = self.text_colors.get(color, 37)
			elif isinstance(color, int):
				col = color
			else:
				col = 37

			if isinstance(bg, str):
				bg_col = self.text_colors.get(bg, -1)
				if bg_col != -1 :
					bg_col = f'\033[{bg_col}m'
			elif isinstance(bg, int):
				bg_col = f'\033[{bg}m'
			else:
				bg_col = ''

			BOLD = ""
			if bold:
				BOLD = "\033[1m"
			if cont:
				fin = ""
			else:
				fin = "\033[0m"
			out = f"{BOLD}\033[{col}m{bg_col}{text}{fin}"
		return out


	def show(self):
		'''Выводит таблицу с цветовой разметкой в консоль'''
		table = self.__draw()
		for line in table:
			print(line)
		return table

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
				try:
					item_len = len(str(self.data[line_number][column_number])) + self.indent*2
				except:
					item_len = 0
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
			if t < len(self.columns_max) - 1: 
				top_line += self.symbols[6]
		top_line += self.color(self.symbols[2],self.borders_color)

		# создание нижней линии
		bottom_line = self.color(self.symbols[3], self.borders_color, cont = 1)
		for t in range(len(self.columns_max)):
			bottom_line = bottom_line + self.symbols[1]*self.columns_max[t]
			if t < len(self.columns_max)-1:
				bottom_line += self.symbols[7]
		bottom_line += self.color(self.symbols[4], self.borders_color)
		if self.shadow_color:
				bottom_line += self.color(self.shadow_symbol[0], self.shadow_color)

		# создание средней линии
		middle_line = self.color(self.symbols[9], self.borders_color, cont = 1)
		for t in range(len(self.columns_max)):
			middle_line = middle_line + self.symbols[12]*self.columns_max[t]
			if t < len(self.columns_max)-1:
				middle_line += self.symbols[8]
		middle_line += self.color(self.symbols[10],self.borders_color)
		if self.shadow_color:
				middle_line += self.color(self.shadow_symbol[0], self.shadow_color)

		table.append(top_line)

		# тело таблицы
		for line_number in range(self.rows):
			line = ''
			line += self.color(self.symbols[5], self.borders_color)
			for column_number in range(self.columns):
				bg_color = None
				bold = False
				try:
					elem = str(self.data[line_number][column_number]).replace('\n', '').strip()
				except:
					elem = ''
				cell = ' ' * self.indent + elem + ' ' * self.indent
				if line_number == 0 and self.header:
					# для первой строки таблицы  используем параметр выравнивания как для заголовка
					cell = cell.upper()
					aligment = self.header_alignment
					color = self.header_color
					bg_color = self.bg_color
					bold = True
				else:
					# для остальных строк используем параметр выравнивания для содержимого
					aligment = self.alignment
					color = self.text_color
				if aligment == 'right':
					line += self.color(cell.rjust(self.columns_max[column_number]), color, bg = bg_color, bold=bold)
				elif aligment == 'center':
					line += self.color(cell.center(self.columns_max[column_number]), color, bg = bg_color, bold=bold)
				else:
					line += self.color(cell.ljust(self.columns_max[column_number]), color, bg = bg_color, bold=bold)
				if column_number < len(self.columns_max) - 1:
					line += self.color(self.symbols[11], self.borders_color)
			line += self.color(self.symbols[5], self.borders_color)
			if self.shadow_color:
				line += self.color(self.shadow_symbol[0], self.shadow_color)
			table.append(line)
			if line_number < self.rows - 1:
				table.append(middle_line)
		table.append(bottom_line)
		if self.shadow_color:
			table.append('  ' + self.color(self.shadow_symbol[1] * (self.table_width - 2), self.shadow_color))
		return table
