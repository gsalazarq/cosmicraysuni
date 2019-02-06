README

### TXT to ROOT 

Tener cuidado con el nombre del archivo txt y la correcta definicin de las variables. 

## Scripts para automatizar la simulacin de rayos cósmicos. 
cd ~/Programs/arti/sims/
do_sims.sh -w ~/Programs/lago-corsika/run/ -p lima04 -t 3600 -y -u gerald -s lima -k 5000

#Fill site options
0              (Zenit)
90
[Default]
[Default]
0.1            (Rigidity)
[Defaul]       (Modelo Atmosferico)
0.024951	(Campo geomagnetico)   
-0.2975

cd ~/Programs/lago-corsika/run/
ls *lima04*
gedit go.sh &
# replace lima0n  -> lima0(n+1)
go.sh
./go.sh
ls run-lima04* > run.sh
gedit run.sh &
# replace run  -> ./run
./run


for i in DAT??????.bz2; do j=$(echo $i | sed -e 's/.bz2//'); u=$(echo $j | sed -e 's/DAT//'); bzip2 -d -k $i; echo $j | lagocrkread | analysis -p -v $u; rm $j; done
