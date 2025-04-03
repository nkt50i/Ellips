from fenics import *
import numpy as np

# Определение сетки
L = 1.0  # Длина области по оси x_1
H = 1.0  # Длина области по оси x_2
mesh = RectangleMesh(Point(0, 0), Point(L, H), 10, 10)  # Прямоугольная сетка

# Определение функции для переменной ψ
V = FunctionSpace(mesh, 'P', 1)

# Условие на границе цилиндра (ψ = 0 на границе)
bc = DirichletBC(V, Constant(0), 'on_boundary')

# Определение переменной для скорости
u_infinity = 1.0  # Пример скорости на входе
psi_0 = u_infinity * H  # Интеграл от скорости по высоте области

# Условие периодичности по продольной координате (по оси x_1)
class PeriodicBoundaryX1(SubDomain):
    def inside(self, x, on_boundary):
        # Сравнение значений x[0] (координата по оси x1) с границами
        return near(x[0], 0) or near(x[0], L)

    def map(self, x, y):
        if near(x[0], 0):
            y[0] = x[0] + L
        elif near(x[0], L):
            y[0] = x[0] - L
        else:
            y[0] = x[0]
        y[1] = x[1]

# Условие периодичности по поперечной координате (по оси x_2)
class PeriodicBoundaryX2(SubDomain):
    def inside(self, x, on_boundary):
        # Сравнение значений x[1] (координата по оси x2) с границами
        return near(x[1], 0) or near(x[1], H)

    def map(self, x, y):
        y[0] = x[0]
        if near(x[1], 0):
            y[1] = x[1] + H
        elif near(x[1], H):
            y[1] = x[1] - H
        else:
            y[1] = x[1]

# Определение граничных условий для периодичности
periodic_x1 = PeriodicBoundaryX1()
periodic_x2 = PeriodicBoundaryX2()

# Создаем группу граничных условий для функции ψ
bc_periodic_x1 = DirichletBC(V, Constant(0), periodic_x1)
bc_periodic_x2 = DirichletBC(V, Constant(psi_0), periodic_x2)

# Пример вариационной задачи (для уравнений Навье-Стокса, гипотетической задачи)
psi = TrialFunction(V)
v = TestFunction(V)

# Пример вариационной задачи (для простого уравнения теплопроводности или потенциальной задачи)
a = dot(grad(psi), grad(v))*dx
L = Constant(0)*v*dx  # Источник силы (можно заменить на необходимую задачу)

# Решение задачи с учетом граничных условий
psi_solution = Function(V)
solve(a == L, psi_solution, [bc, bc_periodic_x1, bc_periodic_x2])

# Визуализация результата
import matplotlib.pyplot as plt
plot(psi_solution)
plt.show()
