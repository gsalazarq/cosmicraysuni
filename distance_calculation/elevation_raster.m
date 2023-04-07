% load data from raster text file 
data = load('/home/justus/Dropbox/b_research/b-muongraphy-UNI/b_cosmicraysuni/atenuation_calculation/rastert_dem_uni1-clean.txt');
raster = reshape(data, 317, 626);
imagesc(raster);
[n,m] = meshgrid(1:size(data,2), 1:size(data,1)); % create x and y vectors using meshgrid

surf(n,m,raster, 'EdgeColor', 'none');
colormap(jet); 
colorbar; 
xlabel('X'); 
ylabel('Y'); 
zlabel('Data'); 
rotate3d on;
