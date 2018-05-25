import random
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


class Generator:
    """
    Класс генератора
    """
    def __init__(self,
                 number=1,
                 name=False,
                 second_name=False,
                 patronymic=False,
                 sex=False,
                 city_and_region=False,
                 profession=False,
                 favorite_drink=False,
                 favorite_dish=False,
                 favorite_film=False
                 ):
        self.male_names = ('Иван', 'Сергей', 'Анатолий', 'Денис', 'Роман',
                           'Александр', 'Олег', 'Андрей', 'Борис', 'Максим',
                           'Михаил', 'Никита', 'Владимир', 'Дмитрий', 'Евгений',
                           'Руслан', 'Петр', 'Станислав', 'Самуил', 'Аркадий')
        self.male_second_names = ('Петров', 'Иванов', 'Сидоров', 'Кузнецов', 'Попов',
                                  'Васильев', 'Соколов', 'Михайлов', 'Новиков', 'Морозов',
                                  'Волков', 'Алексеев', 'Лебедев', 'Семенов', 'Егоров',
                                  'Павлов', 'Козлов', 'Степанов', 'Николаев', 'Никитин')
        self.male_patronymics = ('Андреевич', 'Альбертович', 'Олегович', 'Иванович', 'Анатольевич',
                                 'Денисович', 'Романович', 'Александрович', 'Борисович', 'Дмитриевич',
                                 'Евгениевич', 'Максимович', 'Михайлович', 'Никитович', 'Владимирович',
                                 'Русланович', 'Петрович', 'Станиславович', 'Самуилович', 'Аркадиевич')
        self.male_professions = ('водитель', 'сантехник', 'дворник', 'электрик', 'программист',
                                 'инженер', 'учитель', 'преподаватель', 'продавец', 'консультант',
                                 'агент', 'кассир', 'бухгалтер', 'менеджер', 'логист',
                                 'оператор', 'грузчик', 'машинист', 'летчик', 'гонщик')
        self.female_names = ('Ольга', 'Светлана', 'Ирина', 'Зинаида', 'Оксана',
                             'Алиса', 'Полина', 'Римма', 'Регина', 'Камилла',
                             'Снежана', 'Татьяна', 'Наталия', 'Лидия', 'Инна',
                             'Вера', 'Василиса', 'Анна', 'Анастасия', 'Алла')
        self.female_second_names = ('Савинова', 'Хворова', 'Смирнова', 'Петрова', 'Иванова',
                                    'Сидорова', 'Кузнецова', 'Попова', 'Васильева', 'Соколова',
                                    'Михайлова', 'Новикова', 'Морозова', 'Волкова', 'Алексеева',
                                    'Лебедева', 'Семенова', 'Егорова', 'Козлова', 'Николаева')
        self.female_patronymics = ('Алексеевна', 'Олеговна', 'Ивановна', 'Андреевна', 'Альбертовна',
                                   'Олеговна', 'Денисовна', 'Анатольевна', 'Романовна', 'Александровна',
                                   'Борисовна', 'Дмитриевна', 'Евгениевна', 'Максимовна', 'Михайловна',
                                   'Никитовна', 'Владимировна', 'Руслановна', 'Петровна', 'Станиславовна')
        self.female_professions = ('учительница', 'воспитательница', 'оператор', 'гонщица', 'летчица',
                                   'бухгалтер', 'швея', 'грузчица', 'кассир', 'инженер',
                                   'программист', 'продавщица', 'менеджер', 'логист', 'агент',
                                   'консультант', 'машинистка', 'стенографистка', 'посудомойщица', 'уборщица')
        self.city_and_region = ('Санкт-Петербург, Ленинградская область', 'Москва, Московская область', 'Новокузнецк, Кемеровская область', 'Барнаул, Алтайский край', 'Благовещенск, Амурская область',
                                'Архангельск, Архангельская область', 'Астрахань, Астраханская область', 'Воронеж, Воронежская область', 'Иркутск, Иркутская область', 'Волгоград, Волгоградская область',
                                'Вологда, Вологодская область', 'Белгород, Белгородская область', 'Владимир, Владимирская область', 'Калуга, Калужская область', 'Новосибирск, Новосибирская область',
                                'Владивосток, Приморский край', 'Мурманск, Мурманская область', 'Магадан, Магаданская область', 'Орел, Орловская область', 'Пенза, Пензенская область')
        self.favorite_drinks = ('водка', 'вода', 'сок', 'компот', 'чай',
                                'капучино', 'американо', 'фраппе', 'гляссе', 'латте',
                                'эспрессо', 'коньяк', 'вино', 'джин', 'шампанское',
                                'вермут', 'лимонад', 'виски', 'ром', 'кофе')
        self.favorite_dishes = ('запеканка', 'борщ', 'харчо', 'шашлык', 'бургер',
                                'хот-дог', 'пирожок', 'самса', 'хычин', 'шаверма',
                                'мороженое', 'шоколад', 'кабачки', 'рыба', 'икра',
                                'овощи', 'щи', 'каша', 'хлеб', 'торт')
        self.favorite_films = ('Бегущий по лезвию', 'Судья Дредд', 'Звездные войны', 'Побег из Шоушенка', 'Зеленая миля',
                               'Форрест Гамп', 'Список Шиндлера', '1+1', 'Леон', 'Начало',
                               'Король Лев', 'Бойцовский клуб', 'Жизнь прекрасна', 'Крестный отец', 'Криминальное чтиво',
                               'Престиж', 'Игры разума', 'Достучаться до небес', 'Черная пантера', 'Властелин колец')

        self.number = number
        self.flag_name = name
        self.flag_second_name = second_name
        self.flag_patronymic = patronymic
        self.flag_sex = sex
        self.flag_city_and_region = city_and_region
        self.flag_profession = profession
        self.flag_favorite_drink = favorite_drink
        self.flag_favorite_dish = favorite_dish
        self.flag_favorite_film = favorite_film

        self.bd = []
        self.filename = 'result.txt'

    def generate(self):
        """
        Ф-ция осуществляет генерацию необходимого числа данных
        """
        self.bd = []
        for i in range(self.number):
            if random.randrange(2) == 1:
                self.bd.append(self.generate_male())
            else:
                self.bd.append(self.generate_female())
        return self.bd

    def generate_male(self):
        """
        Ф-ция осуществляет генерацию данных одно мужчины
        """
        person = {}
        print('Зашел в генератор м')
        if self.flag_name:
            person['имя'] = random.choice(self.male_names)
        if self.flag_second_name:
            person['фамилия'] = random.choice(self.male_second_names)
        if self.flag_patronymic:
            person['отчество'] = random.choice(self.male_patronymics)
        if self.flag_sex:
            person['пол'] = 'м'
        if self.flag_city_and_region:
            person['город и область'] = random.choice(self.city_and_region)
        if self.flag_profession:
            person['профессия'] = random.choice(self.male_professions)
        if self.flag_favorite_drink:
            print('Создал м')
            person['любимый напиток'] = random.choice(self.favorite_drinks)
        if self.flag_favorite_dish:
            person['любимое блюдо'] = random.choice(self.favorite_dishes)
        if self.flag_favorite_film:
            person['любимый фильм'] = random.choice(self.favorite_films)
        return person

    def generate_female(self):
        """
        Ф-ция осуществляет генерацию данных одной женщины
        """
        person = {}
        print('Зашел в генератор ж')
        if self.flag_name:
            person['имя'] = random.choice(self.female_names)
        if self.flag_second_name:
            person['фамилия'] = random.choice(self.female_second_names)
        if self.flag_patronymic:
            person['отчество'] = random.choice(self.female_patronymics)
        if self.flag_sex:
            person['пол'] = 'ж'
        if self.flag_city_and_region:
            person['город и область'] = random.choice(self.city_and_region)
        if self.flag_profession:
            person['профессия'] = random.choice(self.female_professions)
        if self.flag_favorite_drink:
            print('Создал ж')
            person['любимый напиток'] = random.choice(self.favorite_drinks)
        if self.flag_favorite_dish:
            person['любимое блюдо'] = random.choice(self.favorite_dishes)
        if self.flag_favorite_film:
            person['любимый фильм'] = random.choice(self.favorite_films)
        return person

    def write_bd_to_file(self):
        """
        Ф-ция осуществляет запись результата генерации в файл
        """
        if len(self.bd) != 0:
            with open(self.filename, 'w+') as f:
                for i in range(len(self.bd)):
                    f.write('№%s\n' % str(i+1))
                    if self.flag_name:
                        f.write('Имя: %s\n' % self.bd[i]['имя'])
                    if self.flag_second_name:
                        f.write('Фамилия: %s\n' % self.bd[i]['фамилия'])
                    if self.flag_patronymic:
                        f.write('Отчество: %s\n' % self.bd[i]['отчество'])
                    if self.flag_sex:
                        f.write('Пол: %s\n' % self.bd[i]['пол'])
                    if self.flag_city_and_region:
                        f.write('Город и область: %s\n' % self.bd[i]['город и область'])
                    if self.flag_profession:
                        f.write('Профессия: %s\n' % self.bd[i]['профессия'])
                    if self.flag_favorite_drink:
                        f.write('Любимый напиток: %s\n' % self.bd[i]['любимый напиток'])
                    if self.flag_favorite_dish:
                        f.write('Любимое блюдо: %s\n' % self.bd[i]['любимое блюдо'])
                    if self.flag_favorite_film:
                        f.write('Любимый фильм: %s\n' % self.bd[i]['любимый фильм'])
                    f.write('\n')


class StartWindow:
    """
    Класс начального окна
    """
    def __init__(self, frame):
        self.frame = frame
        self.title = Label(frame, text='Добро пожаловать!')
        self.button_write = Button(frame, text='Генерация')
        self.button_help = Button(frame, text='Справка')
        self.button_exit = Button(frame, text='Выход')

    def goto_generate(self, event):
        """
        Ф-ция выполняется при нажатии кнопки "Генератор", осуществляет
        переход к меню генератора.
        """
        self.pack_forget()
        new_window = GenerateWindow(self.frame)
        new_window.bind()
        new_window.pack()

    def goto_help(self, event):
        """
        Ф-ция выполняется при нажатии кнопки "Справка, осуществляет
        переход к меню справки.
        """
        self.pack_forget()
        new_window = HelpWindow(self.frame)
        new_window.bind()
        new_window.pack()

    def goto_exit(self, event):
        """
        Ф-ция выполняется при нажатии кнопки "Выход", осуществляет
        выход из программы.
        """
        self.frame.destroy()

    def bind(self):
        """
        Ф-ция, в которой задаются функции-сценарии, которые выполняются
        при нажатии кнопок.
        """
        self.button_write.bind('<1>', self.goto_generate)
        self.button_help.bind('<1>', self.goto_help)
        self.button_exit.bind('<1>', self.goto_exit)

    def pack(self):
        """
        Ф-ция, в которой выполняется размещение виджетов в окне и задание
        параметров размещения.
        """
        self.title.pack(fill='x', pady=5, ipady=3)
        self.button_write.pack(fill='x', pady=5, ipady=3)
        self.button_help.pack(fill='x', pady=5, ipady=3)
        self.button_exit.pack(side=BOTTOM, fill='x', pady=5, ipady=3)

    def pack_forget(self):
        """
        Ф-ция выполняет удаление всех элементов данного окна при переходе
        в другое меню.
        """
        self.title.pack_forget()
        self.button_write.pack_forget()
        self.button_help.pack_forget()
        self.button_exit.pack_forget()


class HelpWindow:
    """
    Класс окна "Справка" с кнопкой "Назад" и текстом справки
    """
    def __init__(self, frame):
        self.frame = frame
        self.title = Label(frame, text='Справка')
        self.full_text = """
Данная программа осуществляет генерацию тестовых данных

Возможные параметры тестовых данных:
1. Имя
2. Фамилия
3. Отчество
4. Пол
5. Город и область
6. Профессия
7. Любимый напиток
8. Любимое блюдо
9. Любимый фильм

По все параметрам, кроме пола, существует 20 возможных
вариантов значений, которые при генерации выбираются случайно.

Для выполнения генерации перейдите в меню "Генератор",
выберите необходимые поля, укажите количество экземпляров
данных и нажмите "Сгенерировать". 
Результат генерации сохраняется в файл по выбору (по-умолчанию
сохраняется в каталоге со скриптом в текстовом файле "result.txt")
"""
        self.text = Text(frame)
        self.text.insert(1.0, self.full_text)
        self.button_back = Button(self.frame, text='Назад')

    def goto_back(self, event):
        """
        Ф-ция выполняется при нажатии кнопки "Назад", осуществляет
        переход к начальному меню.
        """
        self.pack_forget()
        new_window = StartWindow(self.frame)
        new_window.bind()
        new_window.pack()

    def bind(self):
        """
        Ф-ция, в которой задаются функции-сценарии, которые выполняются
        при нажатии кнопок.
        """
        self.button_back.bind('<1>', self.goto_back)

    def pack(self):
        """
        Ф-ция, в которой выполняется размещение виджетов в окне и задание
        параметров размещения.
        """
        self.title.pack(fill='x', pady=5, ipady=3)
        self.text.pack(fill='x', pady=5, ipady=3)
        self.button_back.pack(side=BOTTOM, fill='x', pady=5, ipady=3)

    def pack_forget(self):
        """
        Ф-ция выполняет стирание всех элементов данного окна при переходе
        в другое меню.
        """
        self.title.pack_forget()
        self.text.pack_forget()
        self.button_back.pack_forget()


class GenerateWindow:
    """
    Класс окна генератора с галочками по всем пункта и кнопкой "Сгенерировать"
    """

    def __init__(self, frame):
        self.bd = []
        self.frame = frame
        self.frame_cb = Frame(self.frame)
        self.name_value = BooleanVar()
        self.second_name_value = BooleanVar()
        self.patronymic_value = BooleanVar()
        self.sex_value = BooleanVar()
        self.city_and_region_value = BooleanVar()
        self.profession_value = BooleanVar()
        self.favorite_drink_value = BooleanVar()
        self.favorite_dish_value = BooleanVar()
        self.favorite_film_value = BooleanVar()
        self.title = Label(self.frame, text='Генератор')
        self.label_numer = Label(self.frame_cb, text='Количество:')
        self.entry_number = Entry(self.frame_cb)
        self.name_check = Checkbutton(self.frame_cb, text='Имя', variable=self.name_value, onvalue=True, offvalue=False)
        self.second_name_check = Checkbutton(self.frame_cb, text='Фамилия', variable=self.second_name_value, onvalue=True, offvalue=False)
        self.patronymic_check = Checkbutton(self.frame_cb, text='Отчество', variable=self.patronymic_value, onvalue=True, offvalue=False)
        self.sex_check = Checkbutton(self.frame_cb, text='Пол', variable=self.sex_value, onvalue=True, offvalue=False)
        self.city_and_region_check = Checkbutton(self.frame_cb, text='Город и область', variable=self.city_and_region_value, onvalue=True, offvalue=False)
        self.profession_check = Checkbutton(self.frame_cb, text='Профессия', variable=self.profession_value, onvalue=True, offvalue=False)
        self.favorite_drink_check = Checkbutton(self.frame_cb, text='Любимый напиток', variable=self.favorite_drink_value, onvalue=True, offvalue=False)
        self.favorite_dish_check = Checkbutton(self.frame_cb, text='Любимое блюдо', variable=self.favorite_dish_value, onvalue=True, offvalue=False)
        self.favorite_film_check = Checkbutton(self.frame_cb, text='Любимый фильм', variable=self.favorite_film_value, onvalue=True, offvalue=False)
        self.button_generate = Button(frame, text='Сгенерировать')
        self.button_back = Button(self.frame, text='Назад')

    def generate(self, event):
        """
        Ф-ция выполняется при нажатии кнопки "Сгенерировать" и осуществляет проверку и запуск генерации
        """
        str_entry = self.entry_number.get()
        if not (self.name_value.get() or self.second_name_value.get() or self.patronymic_value.get() or
                self.sex_value.get() or self.city_and_region_value.get() or self.profession_value.get() or
                self.favorite_drink_value.get() or self.favorite_dish_value.get() or self.favorite_film_value.get()):
            messagebox.showinfo('Ошибка', 'Не выбран ниодин пункт')
        elif str_entry == '':
            messagebox.showinfo('Ошибка', 'Не задано количество тестовых данных')
        elif int(str_entry) <= 0 or not str_entry.isdigit():
            messagebox.showinfo('Ошибка', 'Некорректно задано количество тестовых данных')
        else:
            file_d = filedialog
            obj = Generator(number=int(self.entry_number.get()),
                            name=self.name_value.get(),
                            second_name=self.second_name_value.get(),
                            patronymic=self.patronymic_value.get(),
                            sex=self.sex_value.get(),
                            city_and_region=self.city_and_region_value.get(),
                            profession=self.profession_value.get(),
                            favorite_drink=self.favorite_drink_value.get(),
                            favorite_dish=self.favorite_dish_value.get(),
                            favorite_film=self.favorite_film_value.get())
            obj.filename = file_d.asksaveasfilename()
            self.bd = obj.generate()
            obj.write_bd_to_file()
            print(self.bd)
            self.list_window()

    def list_window(self):
        """
        Ф-ция выводит на экран окно с текстом результата генерации
        """
        list_w = Toplevel()
        format_text = ''
        for i in range(len(self.bd)):
            format_text += '№' + str(i + 1) + '\n'
            if self.name_value.get():
                format_text += 'Имя: ' + self.bd[i]['имя'] + '\n'
            if self.second_name_value.get():
                format_text += 'Фамилия: ' + self.bd[i]['фамилия'] + '\n'
            if self.patronymic_value.get():
                format_text += 'Отчество: ' + self.bd[i]['отчество'] + '\n'
            if self.sex_value.get():
                format_text += 'Пол: ' + self.bd[i]['пол'] + '\n'
            if self.city_and_region_value.get():
                format_text += 'Город и область: ' + self.bd[i]['город и область'] + '\n'
            if self.profession_value.get():
                format_text += 'Профессия: ' + self.bd[i]['профессия'] + '\n'
            if self.favorite_drink_value.get():
                format_text += 'Любимый напиток: ' + self.bd[i]['любимый напиток'] + '\n'
            if self.favorite_dish_value.get():
                format_text += 'Любимое блюдо: ' + self.bd[i]['любимое блюдо'] + '\n'
            if self.favorite_film_value.get():
                format_text += 'Любимый фильм: ' + self.bd[i]['любимый фильм'] + '\n'
            format_text += '\n'
        list_w.title('Результат генерации')
        text = Text(list_w)
        text.insert(1.0, format_text)
        text.pack(side=LEFT)

    def goto_back(self, event):
        """
        Ф-ция выполняется при нажатии кнопки "Назад", осуществляет
        переход к начальному меню.
        """
        self.pack_forget()
        new_window = StartWindow(self.frame)
        new_window.bind()
        new_window.pack()

    def bind(self):
        """
        Ф-ция, в которой задаются функции-сценарии, которые выполняются
        при нажатии кнопок.
        """
        self.button_back.bind('<1>', self.goto_back)
        self.button_generate.bind('<1>', self.generate)

    def pack(self):
        """
        Ф-ция, в которой выполняется размещение виджетов в окне и задание
        параметров размещения.
        """
        self.title.pack(fill='x', pady=5, ipady=3)
        self.frame_cb.pack()

        self.label_numer.grid(row=0, column=0, sticky='w')
        self.entry_number.grid(row=0, column=1, sticky='w')
        self.name_check.grid(row=1, column=0, sticky='w', columnspan=2)
        self.second_name_check.grid(row=2, column=0, sticky='w', columnspan=2)
        self.patronymic_check.grid(row=3, column=0, sticky='w', columnspan=2)
        self.sex_check.grid(row=4, column=0, sticky='w', columnspan=2)
        self.city_and_region_check.grid(row=5, column=0, sticky='w', columnspan=2)
        self.profession_check.grid(row=6, column=0, sticky='w', columnspan=2)
        self.favorite_drink_check.grid(row=7, column=0, sticky='w', columnspan=2)
        self.favorite_dish_check.grid(row=8, column=0, sticky='w', columnspan=2)
        self.favorite_film_check.grid(row=9, column=0, sticky='w', columnspan=2)

        self.button_generate.pack(fill='x', pady=5, ipady=3)
        self.button_back.pack(side=BOTTOM, fill='x', pady=5, ipady=3)

    def pack_forget(self):
        """
        Ф-ция выполняет стирание всех элементов данного окна при переходе
        в другое меню.
        """
        self.title.pack_forget()
        self.frame_cb.pack_forget()

        self.label_numer.grid_forget()
        self.entry_number.grid_forget()
        self.name_check.grid_forget()
        self.second_name_check.grid_forget()
        self.patronymic_check.grid_forget()
        self.sex_check.grid_forget()
        self.city_and_region_check.grid_forget()
        self.profession_check.grid_forget()
        self.favorite_drink_check.grid_forget()
        self.favorite_dish_check.grid_forget()
        self.favorite_film_check.grid_forget()

        self.button_generate.pack_forget()
        self.button_back.pack_forget()


def main():
    """
    Главная ф-ция программы, в ней осуществляется создание стартового окна
    и задание его параметров.
    """
    root = Tk()
    root.title('Генерация тестовых данных')
    height = (root.winfo_screenheight() - root.winfo_reqheight()) / 2 - 300
    width = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2 - 300
    size = '400x600'
    root.geometry('%s+%d+%d' % (size, width, height))
    window = StartWindow(root)
    window.bind()
    window.pack()
    root.mainloop()


if __name__ == '__main__':
    main()

