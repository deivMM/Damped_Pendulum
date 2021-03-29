import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation, PillowWriter

# Swich it to True to show the animation in real time
plotRealTime = True

#Physics parameters
g = 9.81
k = 0.3
L = 1

#Integration interval in sec
delta_t = 0.001

#Time to simulate in sec
t_end = 20
#Initial Conditions
theta_0 = np.pi*0
theta_dot_0 = 8

# Animation
fps = 25

theta = [theta_0]
theta_dot = [theta_dot_0]
Kin_e = [0.5*theta_dot_0**2]
t_grid = np.arange(0, t_end, delta_t)

def theta_dot_dot(x,x_dot):
    return -k * x_dot - g / L * np.sin(x)

for _ in t_grid[1:]:
    theta_dot.append(theta_dot[-1] + delta_t * theta_dot_dot(theta[-1],theta_dot[-1]))
    theta.append(theta[-1] + delta_t * theta_dot[-1])
    Kin_e.append(0.5*theta_dot[-1]**2)

thisx, thisy = np.sin(theta),-np.cos(theta)

fig = plt.figure(figsize=(7,7),facecolor='.85')
fig.suptitle('Damped Pemdulum',fontsize=20,x=0.5,y=.95,weight='semibold')
gs1 = plt.GridSpec(3, 2,hspace=0.05,wspace=0.05)
ax1 = plt.subplot(gs1[0,0])
ax2 = plt.subplot(gs1[1,0])
ax3 = plt.subplot(gs1[2,0])
ax4 = plt.subplot(gs1[:,1],aspect='equal',facecolor='.85')

ax1.set_ylabel(r'${\theta}$ (rad)',fontsize=10)
ax2.set_ylabel(r'$\dot{\theta}$ $(rad/s$)',fontsize=10)
ax3.set_ylabel('Kin. En. ( J )',fontsize=10)
ax3.set_xlabel('t (s)',fontsize=10)
plt.setp([ax1.get_xticklabels(),ax2.get_xticklabels()], visible=False)
ax4.set_xticks([])
ax4.set_yticks([])
ax4.set_xlim(-1.5,1.5)
ax4.set_ylim(-1.5,1.5)
[ax.set_xlim(0,t_end) for ax in [ax1,ax2,ax3]]

n = 1000
colors= np.zeros((n,4))
colors[:,3] = np.linspace(0, 1, n, endpoint=True)
scatter = ax4.scatter(np.zeros(n), np.zeros(n), s = 1,
            facecolor = colors, edgecolor='none', zorder=-100)

line_ax1, = ax1.plot([], [],'k')
line_ax2, = ax2.plot([], [],'k')
line_ax3, = ax3.plot([], [],'k')
line1, = ax4.plot([0,1], [0,1], '-', color='k', lw=12, solid_capstyle='round')
line2, = ax4.plot([], [], '-', color='w', lw=10, solid_capstyle='round', zorder=2)
line3, = ax4.plot([], [], 'o', color='k', markersize=2, zorder=3)
line4, = ax4.plot([], [], 'o', color='k', markersize=25, zorder=1)
line = [line1, line2, line3, line4]

time_template = 'Time = {:3.1f}s'.format
p = ax4.text(-1,2, time_template,fontsize=20, style='italic',bbox={'facecolor': 'white', 'alpha': 1, 'pad': 10})
ax1.plot(t_grid,theta,'k',linewidth=.2,alpha=0.2)
ax2.plot(t_grid,theta_dot,'k',linewidth=.2,alpha=0.2)
ax3.plot(t_grid,Kin_e,'k',linewidth=.2,alpha=0.2)

def animate(i):
    x_cord = [0,thisx[i]]
    y_cord = [0,thisy[i]]
    line_ax1.set_data(t_grid[:i],theta[:i])
    line_ax2.set_data(t_grid[:i],theta_dot[:i])
    line_ax3.set_data(t_grid[:i],Kin_e[:i])
    line[0].set_data(x_cord, y_cord)
    line[1].set_data(x_cord, y_cord)
    line[2].set_data(x_cord, y_cord)
    line[3].set_data(thisx[i], thisy[i])
    scatter.set_offsets(np.c_[thisx[max(i-n,0):i],thisy[max(i-n,0):i]])
    p.set_text(time_template(t_grid[i]))

if plotRealTime:
    every_x_frame = 1 / (delta_t*fps)
    an = FuncAnimation(fig, animate, frames= np.arange(0,len(t_grid),int(every_x_frame)), interval=20, repeat=False)
else:
    animate(len(t_grid)-1)

plt.show()
# an.save("damp_pend_gif.gif", writer=PillowWriter(fps=10))

