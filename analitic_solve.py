import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def circulation_cylinder(a, alpha, vinf, gamma, size):
    # Центр цилиндра
    cx, cy = 0.5, 0.5  
    c = a  # Радиус цилиндра
    alpha_rad = np.radians(alpha)  # Угол атаки в радианах
    
    # Функции потенциала и скорости
    def velocity_field(x, y):
        z = (x - cx) + 1j * (y - cy)
        if np.abs(z) < c:  # Если точка внутри цилиндра, возвращаем NaN
            return np.nan, np.nan
        w_prime = vinf * (np.exp(-1j * alpha_rad) - c**2 / z**2 * np.exp(1j * alpha_rad)) + 1j * gamma / (2 * np.pi * z)
        return np.real(w_prime), -np.imag(w_prime)
    
    # Поиск стагнационных точек
    def stagnation_eq(x):
        """ Уравнение для нахождения стагнационной точки (по горизонтальной оси) """
        x = x[0]  # Берём первый элемент массива
        z = complex(x - cx, cy - cy)  # Только x-координата меняется, y=cy
        w_prime = vinf * (np.exp(-1j * alpha_rad) - c**2 / z**2 * np.exp(1j * alpha_rad)) + 1j * gamma / (2 * np.pi * z)
        return np.real(w_prime)  # Должно быть равно 0

    # Ищем два корня (левый и правый стагнационные точки)
    stagnation_x1 = fsolve(stagnation_eq, cx + c)[0]
    stagnation_x2 = fsolve(stagnation_eq, cx - c)[0]
    stagnation_points = np.array([[stagnation_x1, cy], [stagnation_x2, cy]])
    
    # Создание сетки
    x = np.linspace(0, 1, size)
    y = np.linspace(0, 1, size)
    X, Y = np.meshgrid(x, y)
    
    # Вычисление поля скоростей
    U, V = np.vectorize(velocity_field)(X, Y)
    
    # График
    fig, ax = plt.subplots(figsize=(10, 10))

    # Вычисление скорости
    speed = np.sqrt(np.abs(U)**2 + np.abs(V)**2)

    # Цветовая подложка
    plt.pcolormesh(X, Y, speed, shading='auto', cmap='viridis') 

    # Добавляем цветовую шкалу
    plt.colorbar(label='Скорость')
    
    # Линии тока
    stream = ax.streamplot(X, Y, U, V, color='black', linewidth=1.2, density=2, minlength=0.8, arrowsize=0)
    
    # Отрисовка цилиндра
    theta = np.linspace(0, 2 * np.pi, 300)
    cylinder_x = cx + c * np.cos(theta)
    cylinder_y = cy + c * np.sin(theta)
    ax.fill(cylinder_x, cylinder_y, 'w', zorder=3)
    cylinder_line, = ax.plot(cylinder_x, cylinder_y, 'r', linewidth=2.2, zorder=4)
    
    # Отметка стагнационных точек
    stagnation_plot = ax.scatter(stagnation_points[:, 0], stagnation_points[:, 1], color='lime', s=100, zorder=5)

    # Настройка осей
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    plt.xlabel("L")
    plt.ylabel("H")
    plt.title("Обтекание цилиндра с циркуляцией")
    
    # Добавляем легенду
    ax.legend(handles=[stagnation_plot, cylinder_line, stream.lines], labels=["Критические точки", "Контур цилиндра", "Линии тока"])

    plt.show()

# Вызов функции
circulation_cylinder(0.125, 0, 1.0, 0.1, 1000)

