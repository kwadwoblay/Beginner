%%Variables and basic arithmetic
clc; clear;
V = input('Enter the Voltage: ');
I = input('Enter the current: ');
t = input('Enter the time in hours: ');

%Calculations
P = (V*I)/1000;
R = V/I;
E = P*t;
fprintf('Power = %0.2fkW\nResistance = %0.2fohms\nEnergy = %0.2fKwh\n', P,R,E)

