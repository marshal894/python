#Задание № 1
fail = open('test.txt', 'w',encoding='utf-8')
line = input('Введите текст \n')
while line:
    fail.writelines(line)
    line = input('Введите текст \n')
    if not line:
        break
fail.close()
fail = open('test.txt', 'r')
content = fail.readlines()
print(content)
fail.close()


# Задание № 2
with open('file2.txt', 'r', encoding='utf-8') as f:
    usefulness = [f'{line}. {" ".join(count.split())} - {len(count.split())} слов ' for line, count in enumerate(f, 1)]
    print(*usefulness, f'всего строк - {len(usefulness)}.', sep='\n')


# Задание № 3
with open('salary.txt', 'r', encoding='utf-8') as f:
    employees_dict = {line.split()[0]: float(line.split()[1]) for line in f}
    print(f'Средняя величина дохода сотрудников = {round(sum(employees_dict.values()) / len(employees_dict), 3)}\n'
          f'Сотрудники, имеющие оклад менее 20000 {[e[0] for e in employees_dict.items() if e[1] < 20000]}')


# Задание № 4
rus_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре" }
with open('file41.txt', 'w', encoding='utf-8') as nf:
    with open('file4.txt', 'r', encoding='utf-8') as mf:
        nf.write(str([line.replace(line.split()[0], rus_dict.get(line.split()[0])) for line in mf]))


# Задание № 5
def summary():
    try:
        with open('file5.txt', 'w+') as file_obj:
            line = input('Введите цифры через пробел \n')
            file_obj.writelines(line)
            my_numb = line.split()
            print(sum(map(int, my_numb)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно набран номер. Ошибка ввода-вывода')
summary()


# Задание № 6
subj = {}
with open('file6.txt', encoding="utf-8") as f:
    for line in f:
        name, stats = line.split(':')
        n_sum = sum(map(int, "".join([i for i in stats if i == ' ' or (i >= '0' and i <= '9')]).split()))
        subj[name] = n_sum
print(f"{subj}")


# Задание № 7
import json
profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('file7.txt', 'r') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Прибыль средняя - {prof_aver:.2f}')
    else:
        print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
    pr = {'средняя прибыль': round(prof_aver)}
    profit.update(pr)
    print(f'Прибыль каждой компании - {profit}')
with open('file7.json', 'w') as write_js:
    json.dump(profit, write_js)
    js_str = json.dumps(profit)
    print(f'Создан файл с расширением json со следующим содержимым: \n '
          f' {js_str}')