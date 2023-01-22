commands = ['Открыть файл',
			'Сохранить файл',
			'Показать все контакты',
			'Создать контакт',
			'Удалить контакт',
			'Изменить контакт',
			'Найти контакт',
			'Выход из программы']


def main_menu():
	print('Главное меню:')
	for i, item in enumerate(commands, 1):
		print(f'\t{i}. {item}')
	while True:
		try:
			choice = int(input('Выберите пункт меню: '))
			if 0 < choice < 9:
				return choice
			else:
				print('Введите значение от 1 до 8')
		except ValueError:
			print('Введите корректное значение: ')


def show_contacts(phone_list: list):
	if len(phone_list) < 1:
		print('Телефонная книга пуста или не открыта')
	else:
		print()
		for i, contact in enumerate(phone_list, 1):
			print(f'\t{i}. {contact[0]:20} {contact[1]:13} {contact[2]:20}')
		print()


def end_program():
	print('Программа завершена')


def create_new_contact():
	name = input('Введите имя и фамилию: ')
	phone = input('Введите телефон: ')
	comment = input('Введите комментарий: ')
	return name, phone, comment


def find_contact():
	find = input('Введите искомый элемент: ')
	return find


def select_contact(message: str):
	contact = input(message)
	return contact

def change_contact():
	print('Введите новые данные (если изменения не требуются нажмите Enter)')
	name = input('Введите имя и фамилию: ')
	phone = input('Введите телефон: ')
	comment = input('Введите комментарий: ')
	return name, phone, comment

def success_chan():
	print('Контакт успешно изменен!')


def success_open():
	print('Файл успешно открыт!')


def success_save():
	print('Файл успешно сохранен!')


def success_del():
	print('Контакт успешно удален!')


def success_find():
	print('Контакт успешно найден!')


def delete_confirm(contact: str):
	result = input(f'Вы действительно хотите удалить контакт {contact}? (y/n)').lower()
	if result == 'y':
		return True
	else:
		return False

def empty_request():
	print('Такого контакта не существует!')


def many_request():
	print('Введите более точную информацию. Найдено более одного контакта')