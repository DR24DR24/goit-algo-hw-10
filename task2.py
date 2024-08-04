import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi
import random

# Визначте функцію, яку потрібно інтегрувати, наприклад, f(x) = x^2
# def f(x):
#     return x**2

# Визначте межі інтегрування, наприклад, від 0 до 1
# a = 0  # нижня межа
# b = 2  # верхня межа

# Визначення функції та межі інтегрування
def f(x):
    return np.sin(1/x)

a = 0.00001  # Нижня межа
b = 2  # Верхня межа

# Обчислення інтеграла
result, error = spi.quad(f, a, b)

print(f"Інтеграл: {result}, Error: {error} ")  

def monte_carlo(f,num,a,b):
    points=np.array([random.uniform(a,b) for _ in range(num)])
    yval=f(points)
    integral=sum(yval)/num*(b-a)
    return integral

num=10000000
res2=monte_carlo(f,num,a,b)

print(f"Інтеграл Monte-Carlo:  {res2}, error {res2/np.sqrt(num)}")


# Створення діапазону значень для x
x = np.linspace(a, b, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([min(y) - 0.1, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()



