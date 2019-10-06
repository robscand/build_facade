# -*- coding: utf-8 -*-

from math import floor

class NetGraph:
    def __init__(self, vertices):
        # Число всех вершин графа (событий)
        self.V = vertices
        # Словарь для хранения cписка связей графа
        self.graph = dict()
        # Список для хранения всех путей графа
        self.allPath = list()
        # Список для хранения расчета сетевого графика
        self.netgraph = list()
        # Продолжительность критического пути
        self.crit_val = 0
        # Сумма трудозатрат по всем путям
        self.sum_work_cost = 0.0
        # Сумма числа трудовых ресурсов по всем путям
        self.sum_mid_crew = 0.0
        # Минимальная продолжительность сетевого графика
        self.min_crit_val = 0.0

    # Функция для добавления ребра на граф и параметров работы сетевого графика (параметров графа)
    # Воспроизводит направленный граф в виде списка связей.
    # Заполняет список исходными данными для расчета сетевого графика
    # Используется для поиска всех путей сетевого графика.
    # Список связей - для каждой вершины графа указываются смежные вершины
    def addEdge(self, start=None, end=None, num_c=None, num_t=None):
        # Если указаны вершины
        if (start is not None and end is not None):
            # Если вершина уже есть в графе,
            # то добавляем к этой вершине 'start' смежную ей вершину 'end'
            if start in self.graph:
                self.graph[start].append(end)
            else:
                # Если вершины нет в графе,
                # то добавляем вершину 'start' и заводим список для смежных ей вершин 'end'
                self.graph[start] = [end]

        # Если указаны параметры сетевого графика, то формируем таблицу
        if (num_c is not None and num_t is not None):
            self.netgraph.append([start, end, num_c, num_t, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

    # Функция для расчета сетевого графика табличным методом
    # Заполняет таблицу сетевого графика временными параметрами каждой работы
    def calculateNetGraph(self):
        first_event = self.netgraph[0][0]
        last_event = self.netgraph[-1][1]
        # понадобится для поиска позднего окончания работы, которое совпадает с критическим путем
        end_list = []
        # расчет раннего начала и окончания
        for ind in range(len(self.netgraph)):
            # Если работа первая, то параметры будут следующими
            if self.netgraph[ind][0] == first_event:
                # раннее начало первой работы всегда 0
                self.netgraph[ind][4] = 0.0
                # ранее окончание = раннее начало работы + продолжительность работы
                self.netgraph[ind][5] = self.netgraph[ind][3]
                end_list.append(self.netgraph[ind][3])
            # Иначе для текущей работы ищем предыдущие (начальное событие совпадает
            # с конечным событием предыдущих работ)
            else:
                max_l = []
                for i in range(ind + 1):
                    if self.netgraph[ind][0] == self.netgraph[i][1]:
                        # сохраняем рание окончания предыдущих работ
                        max_l.append(self.netgraph[i][5])
                # ранее начало текущей работы совпадает с максимальным временем ранних окончаний предыдущих работ
                self.netgraph[ind][4] = max(max_l)
                # ранее окончание = раннее начало работы + продолжительность работы
                self.netgraph[ind][5] = round(self.netgraph[ind][3] + self.netgraph[ind][4], 4)
                end_list.append(self.netgraph[ind][5])

        # определяем продолжительность критического пути
        self.crit_val = max(end_list)

        # расчет позднего начала и позднего окончания начинаем с конца графика
        for ind in reversed(range(len(self.netgraph))):
            # если окончание работ соответствует последнему событию, то
            if self.netgraph[ind][1] == last_event:
                # позднее начало текушей работы совпадает c
                # максимальным временем раннего окончания предыдущих работ,
                # т.е. со временем критического пути
                self.netgraph[ind][7] = self.crit_val
                # позднее начало работы = позднее окончание работы - продолжительность работы
                self.netgraph[ind][6] = round(self.netgraph[ind][7] - self.netgraph[ind][3], 4)
            else:
                min_l = []
                for i in reversed(range(ind + 1, len(self.netgraph))):
                    if self.netgraph[ind][1] == self.netgraph[i][0]:
                        # сохраняем поздние начала последующих работ
                        min_l.append(self.netgraph[i][6])
                # позднее окончание текущей работы совпадает с минимальным временем поздних начал последующих работ
                self.netgraph[ind][7] = min(min_l)
                # позднее начало работы = позднее окончание работы - продолжительность работы
                self.netgraph[ind][6] = round(self.netgraph[ind][7] - self.netgraph[ind][3], 4)

        for ind in range(len(self.netgraph)):
            # Если текущая работа последняя, то
            if self.netgraph[ind][1] == last_event:
                # общий резерв = позднее окончание текущей работы - раннее окончание текущей работы
                self.netgraph[ind][8] = round(self.netgraph[ind][7] - self.netgraph[ind][5], 4)
                # частный резерв равен общему резерву времени
                self.netgraph[ind][9] = self.netgraph[ind][8]
            # Иначе
            else:
                # частный резерв = раннее начало последующей работы - раннее окончание текущей работы
                for i in range(ind + 1, len(self.netgraph)):
                    if self.netgraph[ind][1] == self.netgraph[i][0]:
                        self.netgraph[ind][9] = round(self.netgraph[i][4] - self.netgraph[ind][5], 4)
                # общий резерв = позднее окончание текущей работы - раннее окончание текущей работы
                self.netgraph[ind][8] = round(self.netgraph[ind][7] - self.netgraph[ind][5], 4)
        return self.netgraph

    def optimizeNetGraph(self):
        # словарь, хранящий расчет по пути
        param_dct = {}

        # проходим по всем путям
        for i in range(len(self.allPath)):
            ways_list = []
            # продолжительность каждого пути, трудозатраты пути
            time, work_cost = 0, 0
            for j in range(1, len(self.allPath[i])):
                # формируем список работ пути для дальнейшего облегчения поиска
                ways_list.append(str(self.allPath[i][j - 1]) + str(self.allPath[i][j]))
                # перебираем исходные данные
                for el in self.netgraph:
                    # если событие в одном из путей совпадает с событием в исходных данных
                    if self.allPath[i][j - 1] == el[0] and self.allPath[i][j] == el[1]:
                        # сохраняем время и трудозатраты каждой из работ
                        time += el[3]
                        work_cost += el[3] * el[2]
            # средние значения трудовых ресурсов пути
            mid_crew = work_cost / time
            self.sum_work_cost += work_cost
            self.sum_mid_crew += mid_crew
            # заполняем словарь
            param_dct[i] = [ways_list, work_cost, time, mid_crew]

        # Определяем минимальную продолжительность сетевого графика
        self.min_crit_val = self.sum_work_cost / self.sum_mid_crew

        # Определяем для каждого пути оптимальные значения трудовых ресурсов
        for key, val in param_dct.items():
            val.append((self.sum_mid_crew * val[1]) / self.sum_work_cost)

        # список хранит трудозатраты работ
        rwcost = []
        # вводим новые данные для промежуточного расчета сетевого графика
        for el in self.netgraph:
            opt_wc_list = []
            for val in param_dct.values():
                edge = str(el[0]) + str(el[1])
                # если значение из исходных данных совпадает со значением работы из списка путей
                if edge in val[0]:
                    # cохраняем значения оптимальных трудовых ресурсов
                    opt_wc_list.append(val[4])
            # новое количество рабочих - максимальное значение оптимальных трудовых ресурсов
            # из путей, где есть данная работа
            num_c = max(opt_wc_list)
            # если число бригад меньше 1, то поднимаем до 1 бригады
            if num_c < 1:
                num_c = 1
            num_t = (el[3] * el[2]) / num_c
            # новая продолжительность
            rwcost.append(el[3] * el[2])
            el[2] = round(num_c, 3)
            el[3] = round(num_t, 3)

        # Промежуточный расчет сетевого графика
        self.calculateNetGraph()

        # Корректируем число бригад и продолжительность до целых значений c точностью +- 1
        for i in range(len(self.netgraph)):
            # Если работа не фиктивная
            if self.netgraph[i][3] != 0:
                self.netgraph[i][3] = floor(self.netgraph[i][3] + self.netgraph[i][9])
                # Если после сложения резерва и времени, оно после округления получилось 0
                # то поднимаем его до 1
                if self.netgraph[i][3] == 0:
                    self.netgraph[i][3] = 1
            if self.netgraph[i][3] != 0:
                if rwcost[i] % self.netgraph[i][3] != 0:
                    mod_1 = rwcost[i] / (self.netgraph[i][3] + 1)
                    mod_2 = rwcost[i] / (self.netgraph[i][3] - 1)
                    # if mod_2 == 0: mod_2 += 1
                    if mod_1 < mod_2:
                        self.netgraph[i][3] += 1
                        self.netgraph[i][2] = floor(mod_1)
                    else:
                        self.netgraph[i][3] -= 1
                        # if self.netgraph[i][3] == 0: self.netgraph[i][3] += 1
                        self.netgraph[i][2] = floor(mod_2)
                else:
                    self.netgraph[i][2] = floor(rwcost[i] / self.netgraph[i][3])
            else:
                self.netgraph[i][2] = 0

        # Окончательный расчет сетевого графика
        self.calculateNetGraph()
        return self.netgraph

    # Распечатать критический путь
    def getCritWay(self, print_way=False, save_way=False, save_val=False):
        crit_list = []
        if print_way or save_way:
            for i in range(len(self.netgraph)):
                if self.netgraph[i][8] == self.netgraph[i][9] == 0:
                    crit_list.append(self.netgraph[i][0])
            crit_list.append(self.netgraph[i][1])
        if print_way: print(*crit_list, sep=' - ')
        if save_way: return crit_list
        if save_val: return self.crit_val

    # --- Поиск путей методом "Поиск в глубину"(DFS) ---
    # Данная рекурсивная функция выводит на экран все пути графа от вершины 'first' до вершины 'last'.
    # visited[] - отслеживает все вершины в текущем пути
    # path[] - хранит актуальные вершины
    def dfs(self, first, last, visited, path):
        # Отмечаем текущую вершину как посещенную и сохраняем ее список пути
        visited[first] = True
        path.append(first)

        # Если текущая вершина совпадает с конечной вершиной, то распечатать путь path[]
        if first == last:
            # не используем привычный append для добавления списка, т.к. python добавляет ссылку на список path
            # при очищении списка path удаляется и содержимое списка allPath
            # >> self.allPath.append(path) <<
            self.allPath.append([i for i in path])
        else:
            # Если текущая вершина не совпадает с конечной
            # Повторяем алгоритм для всех вершин, смежных с текущей вершиной
            for i in self.graph[first]:
                if not visited[i]:
                    self.dfs(i, last, visited, path)
                    # Удалить текущую вершину из пути path[] и пометить ее как непосещенную
        path.pop()
        visited[first] = False

    # Вывести все пути от вершины 'first' до вершины 'last'
    def buildAllPaths(self, first, last, print_ways=True, save_ways=False):
        # Пометить все верfirstины, как непосещенные
        visited = [False] * (self.V)
        # Создать список для записи путей
        path = []
        # Вызов рекурсивной функции для печати всех путей
        self.dfs(first, last, visited, path)
        if print_ways: print(*self.allPath)
        if save_ways: return self.allPath