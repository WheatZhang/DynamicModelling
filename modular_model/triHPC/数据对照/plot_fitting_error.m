file = importdata('AccuracyOnHPCReport.txt');
data = file.data;
% place	x_O2	x_Ar	y_N2	y_O2	y_Ar	vap_etlp	liq_etlp
figure()
plot(1:42,data(:,2),'k');
hold on
plot(1:42,data(:,3),'r');
hold on
plot(1:42,data(:,4),'b');
hold on
plot(1:42,data(:,5),'k--');
hold on
plot(1:42,data(:,6),'r--');
legend('LiqO2','LiqAr','VapN2','VapO2','VapAr');
ylabel('Fraction');
xlabel('Tray No.(1=Bottom)');
title('Composition fitting error')
grid on
print('pic/CompFitting.jpg','-djpeg','-r600')
close

figure()
plot(1:42,data(:,7),'k');
hold on
plot(1:42,data(:,8),'r');
legend('Vapor Enthalpy','Liquid Enthalpy');
ylabel('Enthalpy/(kJ/kmol)');
xlabel('Tray No.(1=Bottom)');
title('Enthalpy fitting error')
grid on
print('pic/EnthalpyFitting.jpg','-djpeg','-r600')
close