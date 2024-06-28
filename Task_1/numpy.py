from typing import Union,Tuple,List
class Array :
    def __init__(self,data):
        """  On verifie que le parametre data est une liste si ce n'est pas le cas on message d'erreur est
            renvoyé pour notifier qu'il faudrait que data soit de type list"""
        if not isinstance(data,list):
            raise ValueError(" Erreur : data n'est pas une liste ")
            
        
        
        
        if all(isinstance(i, list) for i in data):
            """
            ici nn verifie aussi le type des variables avant d'initialiser le array parce
            que normalement une liste doit avoir les meme type d'éléments.
            Ensuite , on vérifie le nombre d'elements de la liste afin de savoir si elle est une liste vide
            ou non. si data est une liste vide on la considere comme un Array de dimension 1 . Si ce n'est
            pas le cas on passe ax verifications.
            
            """
            if(len(data)==0):
                self.dimension =1
                self.data = []
                self.shape = (0,)
            elif(len(data)!=0):
                
                val = len(data[0])
                val2 = type(data[0][0]) if data[0][0] else None
                
                if (all(val == len(i) for i in data)):
                    if(all(isinstance(j, val2) for j in i) for i in data):
                        self.dimension = 2
                        self.data = data
                        self.shape = (len(data),len(data[0]))
                    else:
                        raise ValueError("Erreur : tous les éléments ne sont du meme type ")
                        
                else:
                    raise ValueError("Erreur : Chaque élément de la liste de liste n'a pas la meme taille")
            
        elif (isinstance(data,list)) :
            j = type(data[0]) if data[0] else None
            
            if all(isinstance(i, j) for i in data):
                self.dimension = 1
                self.data = data
                self.shape = (len(data),)
            else :
                 raise ValueError("Erreur : type contenu dans data incorrecte ")    
            
        else:
            raise ValueError("Erreur : data doit etre une liste ou une liste de liste ")
            
        
    def __repr__(self):
        return f'Array({self.data}) , shape = {self.shape}'
    
    
    
    def __add__(self,array1):
        """Pour les operations , on verifie d'abord que l'élément pris en parametre est un Array ensuite qu'ils
        ont meme dimensions. On verifie si la dimension est 1 ou 2 et qu'ils sont du meme type soit (n,m)=(p,q)
        avec n=p et m=q.
        apres ces verifications on passe au operations
        1er Cas : Array 1D
         On parcourt les deux  Array  simultannement et j'effectue l'operation sur à chaque valeur de l'index i et je la stocke dans
         un nouveau Array.
         ex:
         a1 = Array([1,2])
         a2 = Array([3,4])
         a3 =a1+a2
         on a a3 = Array([a1[0] + a2[0] , [a1[1] + a2[1] ]) ce qui done a3 =Array ([1+3,2+4]) =Array(4,6)
         
        2eme Cas : Array 2D
            On parcourt les deux  Array  simultannement et on selectionne d'abord la premiere ligne de chaque
            Array ,ensuite je prends la colonnes à l'index donné pour les deux Array auquelle on applique l'operation
            et on stocke le resultat dans un nouveau Array à la ligne et index correspondant.
            ex :
            a3 = Array([[1,2,5],[4,7,9]])
            a4 = Array([[1, 2, 3],[9,8,7])
            a5 = a1 + a2
            on a  a5 = Array([ [a3[0][0] + a4[0][0] , a3[0][1] + a4[0][1], a3[0][2] + a4[0][2] ] , [a3[1][0] + a4[1][0] , a3[1][1] + a4[1][1]  ,a3[1][2] + a4[1][2] ]
            a5 = Array ([ [1+1 ,2+2 , 5+3 ],[4+9 ,7+8 ,9+7] ])
            a5 = Array( [ [2,4,8],[13,15,16]]
            """
        if( isinstance(array1,Array)):
            if(self.dimension == array1.dimension):
                if(self.dimension==1):
                    if(self.shape==array1.shape):
                        return Array([self.data[i]+array1.data[i] for i in range(self.shape[0])])
                    else :
                        raise ValueError("Erreur : Impossible de faire la somme d'un array de type n avec un autre de type p avec n != p")
                else:
                    if(self.shape==array1.shape):
                        return Array([[self.data[i][j] + array1.data[i][j] for j in range(self.shape[1])] for i in range(self.shape[0])])
                    else :
                        raise ValueError("Erreur : Impossible de faire la somme d'un array de type (n,m) avec un autre de type (p,q) avec n != p et m != q")
            else:
                raise ValueError("Erreur : Impossible de faire la somme de deux array de dimension différentes")
        elif(isinstance(array1,int)):
            if(self.dimension==1):
                return Array([array1 + self.data[i] for i in range(self.shape[0])])
            else:
                return Array([[array1 + self.data[i][j] for j in range(self.shape[0])] for i in range(self.shape[1])])
        else:
            raise TypeError("Erreur : paramètre de mauvais type")
    
    def __sub__(self,array1):
        if( isinstance(array1,Array)):
            if(self.dimension == array1.dimension):
                if(self.dimension==1):
                    if(self.shape==array1.shape):
                        return Array([self.data[i]-array1.data[i] for i in range(self.shape[0])])
                    else :
                        raise ValueError("Erreur : Impossible de faire la soustraction d'un array de type n avec un autre de type p avec n != p")
                else:
                    if(self.shape==array1.shape):
                        return Array([[self.data[i][j] - array1.data[i][j] for j in range(self.shape[1])] for i in range(self.shape[0])])
                    else :
                        raise ValueError("Erreur : Impossible de faire la soustraction d'un array de type (n,m) avec un autre de type (p,q) avec n != p et m != q")
            else:
                raise ValueError("Erreur : Impossible de faire la soustraction de deux array de dimension différentes")
        elif(isinstance(array1,int)):
            if(self.dimension==1):
                return Array([array1 - self.data[i] for i in range(self.shape[0])])
            else:
                return Array([[array1 - self.data[i][j] for j in range(self.shape[0])] for i in range(self.shape[1])])
        else:
            raise TypeError("Erreur : paramètre de mauvais type")

    def __mul__(self,array1):
        if( isinstance(array1,Array)):
            if(self.dimension == array1.dimension):
                if(self.dimension==1):
                    if(self.shape==array1.shape):
                        return Array([self.data[i]*array1.data[i] for i in range(self.shape[0])])
                    else :
                        raise ValueError("Erreur : Impossible de faire la multiplication d'un array de type n avec un autre de type p avec n != p")
                else:
                    if(self.shape==array1.shape):
                        return Array([[self.data[i][j] * array1.data[i][j] for j in range(self.shape[1])] for i in range(self.shape[0])])
                    else :
                        raise ValueError("Erreur : Impossible de faire la multiplication d'un array de type (n,m) avec un autre de type (p,q) avec n != p et m != q")
            else:
                raise ValueError("Erreur : Impossible de faire la multiplication de deux array de dimension différentes")
        elif(isinstance(array1,int)):
            if(self.dimension==1):
                return Array([array1 * self.data[i] for i in range(self.shape[0])])
            else:
                return Array([[array1 * self.data[i][j] for j in range(self.shape[0])] for i in range(self.shape[1])])
        else:
            raise TypeError("Erreur : paramètre de mauvais type")

    def __truediv__(self,array1):
        if( isinstance(array1,Array)):
            if(self.dimension == array1.dimension):
                if(self.dimension==1):
                    if(self.shape==array1.shape):
                        return Array([self.data[i]/array1.data[i] for i in range(self.shape[0])])
                    else :
                        raise ValueError("Erreur : Impossible de faire la division d'un array de type n avec un autre de type p avec n != p")
                else:
                    if(self.shape==array1.shape):
                        return Array([[self.data[i][j] / array1.data[i][j] for j in range(self.shape[1])] for i in range(self.shape[0])])
                    else :
                        raise ValueError("Erreur : Impossible de faire la division d'un array de type (n,m) avec un autre de type (p,q) avec n != p et m != q")
            else:
                raise ValueError("Erreur : Impossible de faire la division de deux array de dimension différentes")
        elif(isinstance(array1,int)):
            if(self.dimension==1):
                return Array([array1 / self.data[i] for i in range(self.shape[0])])
            else:
                return Array([[array1 / self.data[i][j] for j in range(self.shape[0])] for i in range(self.shape[1])])
        else:
            raise TypeError("Erreur : paramètre de mauvais type")

    
    def __matmul__(self,array1):
        if( isinstance(array1,Array)):
            if(self.dimension == array1.dimension):
                if(self.dimension==1):
                    if(self.shape==array1.shape):
                        return sum(self.data[i]*array1.data[i] for i in range(self.shape[0]))
                    else:
                        raise ValueError("Erreur : Impossible de faire le produit scalaire d'un array de type n avec un autre de type p avec n != p")
                else:
                    raise ValueError("Erreur : Opération possible qe sur les matrices de dimension 1")
            else:
               raise ValueError("Erreur : Impossible de faire le produit scalaire de deux array de dimension différentes")
        else:
            raise TypeError("Erreur : paramètre de mauvais type")
            
    
    
   
    def __getitem__(self, index):
        """
        d'abord je verifie la dimension ,ensuite le type du parametre index et aussi je le compare à la
        longueur du Array pour eviter de sortir des limites du tableau
        Ensuite on passe à l'indexage ou au slicing selon le cas ,s'il s'agit d'un tableau 1d ou 2d
        """
        if self.dimension == 1:
            if isinstance(index, int):
                if 0 <= index < self.shape[0]:
                    return self.data[index]
                else:
                    raise IndexError("Erreur : l'index est en dehors du parcours de la liste")
            elif isinstance(index, slice):
                return Array(self.data[index])
            else:
                raise TypeError("Erreur : paramètre de mauvais type. Il faut un entier ou un slice")

        elif self.dimension == 2:
            if isinstance(index, tuple):
                if len(index) == 2:
                    rows, cols = index

                    # Convertir les entiers en slices pour une manipulation cohérente
                    if isinstance(rows, int):
                        rows = slice(rows, rows + 1)
                    if isinstance(cols, int):
                        cols = slice(cols, cols + 1)

                    if isinstance(rows, slice) and isinstance(cols, slice):
                        sliced_data = [row[cols] for row in self.data[rows]]
                        # Vérifier si le slicing a renvoyé une liste de listes
                        if all(isinstance(sublist, list) for sublist in sliced_data):
                            return Array(sliced_data)
                        else:
                            return Array([sliced_data])
                    else:
                        raise TypeError("Erreur : Les lignes et les colonnes doivent être de type int ou slice")
                else:
                    raise TypeError("Erreur : Le tuple doit avoir exactement deux éléments")
            elif isinstance(index, int):
                if 0 <= index < self.shape[0]:
                    return Array(self.data[index])
                else:
                    raise IndexError("Erreur : l'index est en dehors du parcours de la liste")
            elif isinstance(index, slice):
                return Array(self.data[index])
            else:
                raise TypeError("Erreur : paramètre de mauvais type. Il faut un tuple ou un entier ou un slice")

        else:
            raise ValueError("Erreur : Dimension non supportée")

    
    
    
    def __contains__(self,valeur):
        """
        cette fonction permet de verifier la presence d'un element dans un array ou non.
        """
        if(self.dimension == 1):
            if(len(self.data)==0):
                print("Le Array est vide")
                return
            else:
                return any(self.data[i]==valeur for i in range(self.shape[0]))
        elif(self.dimension ==2):
            if(len(self.data)==0):
                print("Le Array est vide")
                return 
            else:
                return any((self.data[i][j]==valeur for j in range(self.shape[1])) for i in range(self.shape[0]) )
        else:
            raise ValueError("Erreur : Dimension non supporté ")
  
  
# Ici ce sont les exemples utilisés .vous pouvez aussi faire des verifications par rapport aux erreurs
a = Array([])
print(1 in a)
print(a)
a1 = Array([1, 2, 3, 4, 5])  
print(a1)
a2 = Array([[1, 2,4], [3, 4,7]])  
print(a2)
a3 = Array([[9,12,0]])
print(a3)
print(a2/a2)
print(a1@a1)
print(6 in a1)
print(a2[0:1,2])
print(a1+a1)

            