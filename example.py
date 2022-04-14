from cooltable import Mtable

if __name__ == "__main__":
	example_text = [
		['Name', 'SName', 'Age', 'E-mail', 'Phone'],
		['Max', 'Chubin', 46, 'max@max.ru', '+7(123)222-33-44'], 
		['Sergey', 'Chubin', 54, 'Sergey@Sergey.ru', '+7(987)111-22-33'], 
		['Kristine', 'Plotnikova', 23, 'kris@kris.ru', '+7(456)321-06-07'], 
		['Elena', 'Ivanova', 43, 'lena@lena.ru', '+7(765)344-23-47']
	]

	for t in range(len(Mtable.styles)):
		table = Mtable(title = f"Style {t}", data = example_text, style = t, indent=1, header=True, alignment='center', header_color='yellow', shadow=True, shadow_color='turquoise', text_color='green', borders_color='blue', title_color='red')
		table.show() # вывод таблиц в консоль
		result = table.draw() # тут все таблицы в виде строки. Можно сохранить в файл.
