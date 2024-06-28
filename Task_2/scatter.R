library(ggplot2)

# chargement du dataset dataset
data <- read.csv("Housing.csv")

# nuage de point des colonnes  ('area' vs 'price')
scartter <- ggplot(data, aes(x = area, y = price)) +
  geom_point(col = "black", , alpha = 0.5) +
  labs(title = "Scatter Plot des colonnes  Area et Price", x = "Area ", y = "Price ") + 
  theme_minimal()

print(scartter)

#Remarque

#On remarque que la plupart des points se situent dans la plage de 0 Ã 8 000 pieds carrés pour la
#superficie et de 0 Ã 10 000 000 $ pour le prix.
#aussi on remarque  une tendance générale indiquant que le prix augmente en fonction la
#superficie, bien que cette relation ne soit pas parfaitement linéaire.
#Il y a plusieurs points situés bien au-dessus de la tendance générale, ce qui pourrait
#indiquer des propriétés exceptionnellement chères pour leur superficie ou (possibles
#valeurs aberrantes)