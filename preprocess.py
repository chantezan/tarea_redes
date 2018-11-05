

f=open("wine.csv", "r")
contents =f.readlines()
equipos = {"Houston Rockets":1,"Golden State Warriors":2,"Portland Trail Blazers":3,"Oklahoma City Thunder":4,"Utah Jazz":5,"New Orleans Pelicans":6,
           "San Antonio Spurs":7,"Minnesota Timberwolves":8,"Denver Nuggets":9,"Los Angeles Clippers":10,"Los Angeles Lakers":11,"Sacramento Kings":12,
           "Dallas Mavericks":13,"Memphis Grizzlies":14,"Phoenix Suns":15,"Toronto Raptors":16,"Boston Celtics":17,"Philadelphia 76ers":18,
           "Cleveland Cavaliers":19,"Indiana Pacers":20,"Miami Heat":21,"Milwaukee Bucks":22,"Washington Wizards":23,"Detroit Pistons":24,
           "Charlotte Hornets":25,"New York Knicks":26,"Brooklyn Nets":27,"Chicago Bulls":28,"Orlando Magic":29,"Atlanta Hawks":30}
entradas = [];
salidas = [];
for x in contents:
    entradas.append([x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],x[10]])
    salidas.append([x[11]])