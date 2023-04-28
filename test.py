import random


class searchClass():
	# Класс для поиска повторяющихся элемнтов в массиве (списке)

	def __init__(self, col_item=30, arr=[], random_int=100000):
		"""
			параметры конструктора класса col_item - количество элементов массива (по умолчанию =30) 
			arr - сам массив, если не определен при создании, то заполняется случайными значениями 
			random_int - диапазон допустимых значений элемента  при задании случайным способом
		"""
		self.col_item = col_item
		self.random_int = random_int
		if not arr:
			self.array = [random.randint(0, self.random_int) for i in range(col_item)]
		else:
			self.array = arr
			self.col_item = len(arr)

	def search(self):
		""" 
			метод поиска повторяющихся элементов массива. Ищем с использованием множества
			пробегаемся в цикле по массиву. Если элемент уже во множетсве
		"""

		# первый способ 
		# visit = set()
		# dup = {element for element in self.array if element in visit or (visit.add(element) or False )}
		# if not dup:
		# 	return "дубликатов не найдено"
		# else:
		# 	return dup

		# алгоритмический способ
		dup = []
		for i in range(0, self.col_item):
			for j in range(i+1, self.col_item):
				if self.array[i] == self.array[j]:
					if not self.array[j] in dup:
						dup.append(self.array[j])
		return dup
					
		



if __name__ == "__main__":
	search = searchClass(arr=[7, 0, 1, 7, 4, 2, 4, 3, 8, 10, 5, 6, 0, 0, 3, 6, 4, 8, 0, 1, 7, 7, 9, 3, 9, 4, 0, 10, 3, 7])
	print(f"Исходный массив(список)= {search.array}")
	print(f"Найденные дубликаты= {search.search()}")