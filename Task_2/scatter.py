import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('Housing.csv')

# Scatter plot for 'area' vs 'price'
plt.figure(figsize=(10, 6))
plt.scatter(data['area'], data['price'], alpha=0.5)
plt.title('Scatter Plot of Area vs Price')
plt.xlabel('Area (sq ft)')
plt.ylabel('Price ($)')
plt.grid(True)
plt.show()

"""
Remarque:

On remarque que la plupart des points se situent dans la plage de 0 Ã 8 000 pieds carrés pour la
superficie et de 0 Ã 10 000 000 $ pour le prix.
aussi on remarque  une tendance générale indiquant que le prix augmente en fonction la
superficie, bien que cette relation ne soit pas parfaitement linéaire.
Il y a plusieurs points situés bien au-dessus de la tendance générale, ce qui pourrait
indiquer des propriétés exceptionnellement chères pour leur superficie ou (possibles
valeurs aberrantes)
"""