% load data from raster text file 
data = load('/home/justus/Dropbox/b_research/b-muongraphy-UNI/b_cosmicraysuni/atenuation_calculation/rastert_dem_uni1-clean.txt');
raster = reshape(data, 317, 626); % viene a ser la matriz de elevación
%raster = raster(100:150, 280:500);
conv=1;                                                            % km por degree, %Average radius of the earth: 6371km.
conv=conv*1;                                                           % in meters
%dx=3/3600*conv;
dx=0.95;




%x_t=linspace(0,625,626); 
x_t=linspace(0,50,51); 
%y_t=linspace(0,316,317); 
y_t=linspace(0,220,221); 
raster=double(raster); 
%dato= [10, 120,207,237,1, 2000,6];                            %localization observation point latitude, longitude

dato= [300, 120,207,237,1, 2000,6];                            %localization observation point latitude, longitude


for n=1:1
close all 
punto = num2str(dato(n,5));

  

figure(1)
imagesc(x_t, y_t, raster)
colorbar 
colormap jet
title(['Location Geographical Coordinates Observation Point',num2str(dato(n,5))])
xlabel('Longitude')
ylabel('Latitude')
%set(gca,'YDir','normal')

G0=[dato(n,1),dato(n,2)]; 
     
zg = interp2(x_t, y_t, raster, G0(1), G0(2)); 
%zg = interp2(y_t, x_t, raster, G0(1), G0(2)); 

G0_0=[G0(1) G0(2) zg];                                                     %point observation 3D

hold on
%plot3(G0(1),G0(2),zg,'ro','MarkerEdgeColor','r','MarkerFaceColor','b','MarkerSize',3);
plot3(G0(1),G0(2),'ro','MarkerEdgeColor','r','MarkerFaceColor','b','MarkerSize',3);

hold on


%str = 'Relieve2DGeoCERROUNI';
%nombre = strcat(str,punto,'.pdf');
%saveas(gcf,nombre)
end



lon_t_0=x_t - min(x_t);
lat_t_0=y_t - min(y_t);                                                %The reference system is redefined.


 

P0_lon=G0(1);
P0_lat=G0(2);
P0_0=[P0_lon, P0_lat, zg];                                                 %point observation 3D is redefined

%to meters
lon_t_m=lon_t_0*conv;                                                      %The reference system is redefined
lat_t_m=lat_t_0*conv;                                                      
P0_m=[P0_lon, P0_lat, zg/conv]*conv; 


lon_t_m_int=min(lon_t_m):dx/2:max(lon_t_m);
lat_t_m_int=min(lat_t_m):dx/2:max(lat_t_m);




[XX,YY] = meshgrid(lon_t_m_int,lat_t_m_int);

%zint = interp2(lon_t_m,lat_t_m,raster,XX,YY);
zint = interp2(lat_t_m,lon_t_m,raster,XX,YY);

zint = double(zint);
figure(3)
surface(lon_t_m_int,lat_t_m_int,zint)

keyboard
colorbar
colormap jet
zlim([1500 4000])
shading interp
xlabel('X (m)')
ylabel('Y (m)')
zlabel('altitud (m)')


az=45;
el=45;
view(az,el)



