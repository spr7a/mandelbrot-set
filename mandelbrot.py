
import numpy as np
import matplotlib.pyplot as plt
rows = 1000
cols = 1000
iterations =85
def mandelbrot(c, z):
    global iterations
    cnt = 0
    for a in range(iterations):
        z = z**2 + c
        cnt += 1
        if(abs(z) >2):
            break
    return cnt

def mandelbrot_set(x, y):
    m = np.zeros((len(x), len(y)))
    for i in range(len(x)):
        for j in range(len(y)):
            c = complex(x[i], y[j])
            z = complex(0, 0)
            cnt = mandelbrot(c, z)
            m[i, j] = cnt
    return m

x = np.linspace(-2, 1, rows)
y = np.linspace(-1, 1, cols)
m = mandelbrot_set(x, y)
# plt.xlabel("Re(c)")
# plt.ylabel("Im(c)")
# plt.imshow(m.T, cmap = "magma")
plt.xlabel("Re(c)")
plt.ylabel("Im(c)")
plt.imshow(m.T, cmap="magma", extent=[-2, 1, -1, 1])
# plt.grid(True)
plt.style.use('dark_background')
plt.grid(color='lightgray', linestyle='--', linewidth=0.05)
plt.savefig('result.png', dpi=2000, bbox_inches='tight')
plt.show()
