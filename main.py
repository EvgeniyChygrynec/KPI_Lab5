from tkinter import *

root = Tk()
root.title('Головне вікно')
root.geometry('580x550')
root.resizable(width=False, height=True)
basic_set = {
    ('Дмитро', 30), ('Оксана', 24), ('Олег', 36), ('Надія', 34),
    ('Юлія', 18), ('Артем', 31), ('Віталій', 20), ('Тарас', 65),
    ('Степан', 45), ('Олександр', 56), ('Михайло', 40), ('Євгеній', 19),
    ('Богдан', 5), ('Олексій', 47), ('Геннадій', 48), ('Єлизавета', 73)
}
basic_set_for_show = []
for item in basic_set:
    basic_set_for_show.append(f'{item[0]} - {item[1]}')


def Quick_sort(list_for_sort):
    if len(list_for_sort) <= 1:
        return list_for_sort
    elem = list_for_sort[0]
    left = list(filter(lambda x: x < elem, list_for_sort))
    center = [i for i in list_for_sort if i == elem]
    right = list(filter(lambda x: x > elem, list_for_sort))
    return Quick_sort(left) + center + Quick_sort(right)

list_for_sort = []
help_list = []
for i in range(len(list(basic_set))):
    list_for_sort.append(list(basic_set)[i][1])
for i in sorted(list_for_sort):
    for j in range(16):
        if i == list(basic_set)[j][1]:
            help_list.append(list(basic_set)[j])


def Info_about_student(NZK=1530):


    mini_window = Toplevel(root)
    mini_window.title('Студент ІО-15')
    mini_window.geometry('300x100')
    root.resizable(width=False, height=False)
    Label(mini_window, text='Чигринець Євгеній\n'
                            'група ІО-15\n'
                            'варіант {}'.format(NZK % 26 + 1), justify=LEFT,
          ).pack(fill='both')

List2 = Listbox(width=20, height=17)
List2.pack()
List2.grid(row=4, columnspan=2)
for i in basic_set_for_show:
    List2.insert(0, i)
Label(root, text='Лабораторна робота No5' + ' ' * 24).grid(row=0, column=0)
Label(root, text='Базова множина').grid(row=2, columnspan=2)
Label(root, text="Ім'я та вік людини").grid(row=3, columnspan=2)
Button(root, text='Відомості про студента', font="Times 16",
       command=Info_about_student) \
    .grid(row=0, column=1)
Label(root, text='Введіть вік людей, яких ви хотіли б знайти:').grid(column=0, row=9,
                                                                         sticky=E)

Getter = StringVar(root)
Year_for_search = Entry(root, textvariable=Getter, width=30, bd=3)
Year_for_search.grid(column=1, row=9, sticky=W)


def Get():
    Text_Years = Year_for_search.get()
    Text_Years = set(map(int, Text_Years.split(',', )))
    List_output = []
    Label(root, text='Інформація з бази даних:').grid(column=0, row=12, sticky=E)
    for i in range(len(basic_set)):
        for j in list(Text_Years):
            if j == list(basic_set)[i][1]:
                List_output.append(f'{list(basic_set)[i]} --- {j} років')
            elif j not in list_for_sort:
                List_output.append(f'У базі даних немає людей з таким віком --- {j}років')
    List_output = set(List_output)
    for i in range(len(List_output)):
        Text_Out = Label(root, text=f'{list(List_output)[i]}', justify=LEFT)
    Text_Out.grid(columnspan=2, row=i + 14, sticky=W)

Button(root, text='Пошук', command=Get).grid(row=10)
root.mainloop()
