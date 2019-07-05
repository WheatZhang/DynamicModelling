data_aspen = xlsread("单塔数据","aspen");
data_pyomo = xlsread("单塔数据","pyomo");
%T	P	L	V	y_N2	y_O2	y_Ar	x_N2	x_O2	x_Ar
figure()
subplot(211)
plot(1:42,data_aspen(:,2),'k',1:42,data_pyomo(:,2),'r');
ylabel('T/℃');
% xlabel('Tray No.(1=Bottom)');
legend('Aspen','Pyomo');
title('Temperature profile of HPC')
grid on
subplot(212)
plot(1:42,data_aspen(:,2)-data_pyomo(:,2),'k');
ylabel('T/℃');
xlabel('Tray No.(1=Bottom)');
title('Temperature error')
grid on
print('pic/Temperature.jpg','-djpeg','-r600')
close

figure()
subplot(211)
plot(1:42,data_aspen(:,4),'k',1:42,data_pyomo(:,4),'r');
hold on
plot(1:42,data_aspen(:,5),'b',1:42,data_pyomo(:,5),'m');
ylabel('Flowrate/kmol');
% xlabel('Tray No.(1=Bottom)');
legend('Aspen-L','Pyomo-L','Aspen-V','Pyomo-V');
title('Flowrate profile of HPC')
grid on
subplot(212)
plot(1:42,data_aspen(:,4)-data_pyomo(:,4),'k');
hold on
plot(1:42,data_aspen(:,5)-data_pyomo(:,5),'r');
legend('Liquid','Vapor');
ylabel('Flowrate/kmol');
xlabel('Tray No.(1=Bottom)');
title('Flowrate error')
grid on
print('pic/Flowrate.jpg','-djpeg','-r600')
close

figure()
subplot(211)
plot(1:42,data_aspen(:,6),'k',1:42,data_pyomo(:,6),'r');
hold on
plot(1:42,data_aspen(:,7),'b',1:42,data_pyomo(:,7),'m');
hold on
plot(1:42,data_aspen(:,8),'k--',1:42,data_pyomo(:,8),'r--');
ylabel('Fraction');
% xlabel('Tray No.(1=Bottom)');
legend('Aspen-N2','Pyomo-N2','Aspen-O2','Pyomo-O2','Aspen-Ar','Pyomo-Ar');
title('Vapor composition profile of HPC')
grid on
subplot(212)
plot(1:42,data_aspen(:,6)-data_pyomo(:,6),'k');
hold on
plot(1:42,data_aspen(:,7)-data_pyomo(:,7),'r');
hold on
plot(1:42,data_aspen(:,8)-data_pyomo(:,8),'b');
legend('N2','O2','Ar');
ylabel('Fraction');
xlabel('Tray No.(1=Bottom)');
title('Vapor Composition error')
grid on
print('pic/VapComposition.jpg','-djpeg','-r600')
close

figure()
subplot(211)
plot(1:42,data_aspen(:,9),'k',1:42,data_pyomo(:,9),'r');
hold on
plot(1:42,data_aspen(:,10),'b',1:42,data_pyomo(:,10),'m');
hold on
plot(1:42,data_aspen(:,11),'k--',1:42,data_pyomo(:,11),'r--');
ylabel('Fraction');
% xlabel('Tray No.(1=Bottom)');
legend('Aspen-N2','Pyomo-N2','Aspen-O2','Pyomo-O2','Aspen-Ar','Pyomo-Ar');
title('Liquid composition profile of HPC')
grid on
subplot(212)
plot(1:42,data_aspen(:,9)-data_pyomo(:,9),'k');
hold on
plot(1:42,data_aspen(:,10)-data_pyomo(:,10),'r');
hold on
plot(1:42,data_aspen(:,11)-data_pyomo(:,11),'b');
legend('N2','O2','Ar');
ylabel('Fraction');
xlabel('Tray No.(1=Bottom)');
title('Liquid Composition error')
grid on
print('pic/LiqComposition.jpg','-djpeg','-r600')
close