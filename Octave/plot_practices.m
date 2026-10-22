%ploting
t = 0:pi/100:2*pi;
y = sin(t);

plot(t,y,'--','linewidth', 3)
grid minor on
ylabel('sin(t)')
xlabel('time')
title('sin(x) against time')

