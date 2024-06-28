import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('Housing.csv')

# Histogram for 'bedrooms'
plt.figure(figsize=(10, 6))
plt.hist(data['bedrooms'], bins=10, edgecolor='black')
plt.title('Histogram of Bedrooms')
plt.xlabel('Number of Bedrooms')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

"""
Remarque:

La tendance générale  indique que les propriétés avec 3 chambres sont les plus courantes, suivies par celles 
avec 2 et 4 chambres, tandis que les autres catégories sont beaucoup moins fréquentes.
La majorité des données se concentre autour des catégories de 2, 3, et 4 chambres.
Il y a très peu de propriétés avec 0, 1, 5 ou 6 chambres, ce qui indique que ce sont des
valeurs moins courantes ou “”valeurs aberrantes””.
"""
