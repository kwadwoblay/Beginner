import numpy as np
import matplotlib.pyplot as plt

# Variables
pi = 3.14159

x = np.arange(0,2*pi,pi/100)
y1 = 2*np.cos(x)
y2 = np.cos(x)
y3 = 0.5*np.cos(x)

#plot
#plt.plot(x,y1,'--',x,y2,'-',x,y3,':')
plt.plot(x,y1,label = '2cos(x)', linestyle = '--',linewidth = 2, color = (0.2,0.3,0.4))
plt.plot(x,y2,label = 'cos(x)', ls = '-',linewidth = 2, color = (0.4,0.3,0.4))
plt.plot(x,y3,label = '2cos(x)', linestyle = ':',lw = 2, color = (0.2,0.5,0.4))
plt.legend()
plt.xlabel(r'$0 \leq  x \leq 2/pi$')
plt.ylabel('Cosine functions')
#plt.legend(["2cos(x)","cos(x)","0.5cos(x)"])
plt.title('Typical example of multiple plots')
plt.grid(visible = True, axis = 'both', which = 'both',ls = '--', color = (0.3,0.2,0.2), lw = 1)
plt.savefig("Python/handout/cosine_plot.png")
plt.ylim(-3,3)
plt.xlim(0, 2*pi)
plt.show()
