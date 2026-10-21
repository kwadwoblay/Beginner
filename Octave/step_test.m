pkg load control
s = tf('s');
G = 1 / (s^2 + 2*s + 1);
step(G)
figure
bode(G)
