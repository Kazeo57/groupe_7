#Chargement du dataset
data <- read.csv("Housing.csv")

h <- hist(data$bedrooms,
  breaks = 10,
  col = "skyblue",
  main = "Repartion de la colonne Bedroom",
  xlab = "bedrooms",
  ylab = "Éffectif"
)

print(h)

#Remarque

#La tendance générale  indique que les propriétés avec 3 chambres sont les plus courantes, suivies par celles 
#avec 2 et 4 chambres, tandis que les autres catégories sont beaucoup moins fréquentes.
#La majorité des données se concentre autour des catégories de 2, 3, et 4 chambres.
#Il y a très peu de propriétés avec 0, 1, 5 ou 6 chambres, ce qui indique que ce sont des
#valeurs moins courantes ou “”valeurs aberrantes””.
