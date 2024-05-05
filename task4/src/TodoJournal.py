import sys
import json

class TodoJournal:
    """
    Класс для представления журнала тудушек.
    ...
    Атрибуты
    --------
    name : str
        название тудушки
    path_todo : str
        путь к журналу

    Методы
    ------
    create(self):
        Создание тудушки
    add_entry(self, new_entry):
        Добавление тудушки
   remove_entry(self, index):
        Удаление тудушки
   _update(self, new_data):
        Обновление данных о тудушках
   _parse(self):
        Получение данных о тудушках
    """
    def __init__(self, path_todo):
        """
        Устанавливает все необходимые атрибуты для объекта TodoJournal.
        Параметры
        ---------
        name : str
            название тудушки
        path_todo : str
            путь к журналу
        entries : list
            массив задач
        counter : int
            счетчик для итерирования
        """
        self.path_todo = path_todo
        self.name = self._parse()["name"]
        self.entries = self._parse()["todos"]
        self.counter = 0

    @staticmethod
    def create(filename, name):
        """
        Создаёт json файл для задач
        """
        try:
            with open(filename, "w", encoding='utf-8') as todo_file:
                json.dump(
                    {"name": name, "todos": []},
                    todo_file,
                    sort_keys=True,
                    indent=4,
                    ensure_ascii=False,
                )
        except FileNotFoundError as error:
            print(f"{error}")
            print(f"Не существует такой тудушки: {filename}")
            sys.exit(1)

        except PermissionError as error:
            # Обработка ошибок, связанных с разрешением на доступ к файлу
            print(f"{error}")
            print(f"У Вас нет прав на открытие данного файла! {filename}")
            sys.exit(2)

    def add_entry(self, new_entry):
        """
        добавляет новую тудушку в json файл

        Параметры
        ---------
        new_entry : str
            новая задача
        """

        if (new_entry not in self.entries):
            self.entries.append(new_entry)

        new_data = {
            "name": self.name,
            "todos": self.entries,
        }

        self._update(new_data)

    def remove_entry(self, index):
        """
        удаляет тудушку из json файла

        Параметры
        ---------
        index : int
            индекс удаляемой тудушки
        """

        self.entries.pop(index)

        new_data = {
            "name": self.name,
            "todos": self.entries,
        }

        self._update(new_data)

    def _update(self, new_data):
        """
        заполняет json файл новыми данными

        Параметры
        ---------
        new_data : str
            новые тудушки
        """
        try:
            with open(self.path_todo, "w", encoding='utf-8') as todo_file:
                json.dump(
                    new_data,
                    todo_file,
                    sort_keys=True,
                    indent=4,
                    ensure_ascii=False,
                )
        except FileNotFoundError as error:
            print(f"{error}")
            print(f"Не существует такой тудушки: {self.path_todo}")
            sys.exit(1)
        except PermissionError as error:
            # Обработка ошибок, связанных с разрешением на доступ к файлу
            print(f"{error}")
            print(f"У Вас нет прав на открытие данного файла! {self.path_todo}")
            sys.exit(2)

    # ниже статическое поле класса
    shortcut_names = {"first": 0, "last": -1}

    def __getattr__(self, item):
        index = self.shortcut_names.get(item, None)
        if index is not None:
            return self.entries[index]

        cls = type(self)
        raise AttributeError(f"{cls.__name__} object has no attribute {item}")

    def __len__(self):
        """Возвращает количество задач"""
        return len(self.entries)

    def __iter__(self):
        return iter(self.entries)

    def __next__(self):
        length = self.__len__()
        if self.counter > length:
            raise StopIteration

        else:
            self.counter += 1
        return self.entries[self.counter - 1]

    def __getitem__(self, item):
        if 0 <= item < len(self.entries):
            return self.entries[item]
        else:
            raise IndexError("Неверный индекс")

    def _parse(self):
        """
        чтение json файла
        Возвращаемое значение
        ---------------------
        str
        """
        try:
            with open(self.path_todo, 'r') as todo_file:
                data = json.load(todo_file)
            return data
        except FileNotFoundError as error:
            print(f"{error}")
            print(f"Не существует такой тудушки: {self.path_todo}")
            sys.exit(1)
        except PermissionError as error:
            # Обработка ошибок, связанных с разрешением на доступ к файлу
            print(f"{error}")
            print(f"У Вас нет прав на открытие данного файла! {self.path_todo}")
            sys.exit(2)


todo = TodoJournal('../task4.json')
print(todo.first)
todo.first = "test"
print(todo.first)
print(todo[0])
'''def main():
    TodaysTodos = TodoJournal('../task4.json')
    for i in TodaysTodos:
        print(i)
    print(TodaysTodos[1])


if __name__ == '__main__':
    main()'''
