function [P,R,E] = fun_1(V,I,t)

%Calculations
P = (V*I)/1000;
R = V/I;
E = P*t;
fprintf('Power = %0.2fkW\nResistance = %0.2fohms\nEnergy = %0.2fKwh\n', P,R,E)

