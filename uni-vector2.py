import matplotlib.pyplot as plt
import numpy as np

from matplotlib import animation as ani

plt.figure(figsize=(10,10))
n=10
xmin = -5
xmax =  35
ymin = -20
ymax =  10

A = [[ 2, 1],
     [-0.5,-1.5]]
for i in range(n):
    for j in range(n):
        x=j
        y=i

        a = np.dot(A, [x, y])

        loc_adjust = .2  # 表示位置の調整
        plt.text(x-loc_adjust, y-loc_adjust, "%d"%(i*n + j), color="blue")
        plt.text(a[0]-loc_adjust, a[1]-loc_adjust, "%d"%(i*n + j), color="red")

        plt.plot([xmin,xmax],[0,0],"k", linewidth=1)
        plt.plot([0,0],[ymin,ymax],"k", linewidth=1)
        plt.xlim(xmin, xmax)
        plt.ylim(ymin, ymax)
plt.show()

#---------------------


def animate(nframe):
    global xx, A, la, v
    global num_frame

    plt.clf()
    i = nframe

    p1 = np.array([0, 0])
    p2 = np.array([np.cos(xx[i]), np.sin(xx[i])])
    p_inc = np.sin(xx[i])/np.cos(xx[i])
    p_inc_inv = np.cos(xx[i])/np.sin(xx[i])
    p_len = np.sqrt(np.sin(xx[i])**2 + np.cos(xx[i])**2)

    a2 = np.dot(A, p2)

    a_len = np.sqrt(a2[0]**2 + a2[1]**2)
    a_inc = a2[1]/a2[0]
    a_inc_inv = a2[0]/a2[1]

    dot = p2[0]*a2[0] + p2[1]*a2[1]
    inc_ratio = a_inc/p_inc
    diff_len1 = a_len - la[0]
    diff_len2 = a_len + la[1]

    diff_inc = a_inc - p_inc
    diff_inc_inv = a_inc_inv - p_inc_inv

    delta = 0.05
    # (-0.1 < dot and dot < 0.1):
    if (-delta < diff_inc and diff_inc < delta) or (-delta < diff_inc_inv and diff_inc_inv < delta):
        # 傾きが同じと判定
        lw = 4
    else:
        lw = 2

    plt.plot([0, p2[0]], [0, p2[1]], "b", zorder=110, linewidth=lw)
    plt.plot([0, a2[0]], [0, a2[1]], "r", zorder=100, linewidth=lw)

    plt.plot([-20, 20], [0, 0], "k", linewidth=1)
    plt.plot([0, 0], [-20, 20], "k", linewidth=1)
    plt.xlim(-3, 3)
    plt.ylim(-2, 2)

    plt.title("original(blue):(%.3f,%.3f) after(red):(%.3f,%.3f)" %
              (np.cos(xx[i]), np.sin(xx[i]), a2[0], a2[1]), size=14)
    plt.text(-1.5, 1.7, "[grad]  blue:%.3f red:%.3f ratio:%.3f" %
             (p_inc, a_inc, inc_ratio), size=14)
    plt.text(-1.5, 1.5, "[length]blue:%.3f red:%.3f ratio:%.3f" %
             (p_len, a_len, a_len/p_len), size=14)


A = np.array(
    [[2, 1],
     [-0.5, -1.5]])

la, v = np.linalg.eig(A)
print ("la", la)
print ("v", v)
num_frame = 127
xx = np.linspace(0, 2*np.pi, num_frame)
fig = plt.figure(figsize=(10, 9))
anim = ani.FuncAnimation(fig, animate, frames=num_frame, blit=True)
anim.save('eigen_value.gif', writer='imagemagick', fps=4, dpi=64)
