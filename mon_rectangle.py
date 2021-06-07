# -*- coding: utf-8 -*-
"""
Created on Fri May  7 19:02:33 2021

@author: Saadia Bayou
"""

from point import Point
from math import pi ,sqrt
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle # Nom  methode Rectangle de la biblio matplolib


class MonRectangle(): # nom de ma classe
    """ Classe MonRectangle : Définit la longueur, la largeur , un point initiale P0, 
       construit les 3 autres points à partir de P0, 
       calcul le périmètre, la surface, la diagonale, et trace le rectangle 
       de deux manières différentes """
    
    
    lx=[]
    ly=[]
    lp=[]
    
    def __init__(self,point,longueur,largeur):
        

        self.p=point
        self.la=largeur
        self.lo=longueur

        
        #Rectangle.Point.lp.append(self.p)

        
    def __str__(self) :
        
        s1="\nLe recrangle a pour largeur {0} et pour longueur {1}".\
        format(round(self.la,2),round(self.lo,2))
        s2=" \nson point initial est P0 = {} ".format(self.p)
        
        return s1+s2
    
    def __repr__(self):
        
        r1= "\nRectangle:(largeur={0},longueur={1},"
        r2= "P0 ={2})"
        r=(r1+r2).format(self.la,self.lo,self.p)
        return r
    
    def PerimRec(self):
        """ Calcul le perimetre du rectangle """
        perim=(2*self.lo+2*self.la)
        return perim
    
    def SurfRec(self):
        """ Calcul la surface du rectangle  """
        surf=self.lo*self.la
        return surf
    
    def DiagoRec(self):
        """ Calcul la longueur de la diagonale du rectangle """
        diago=sqrt(pow(self.la,2)+pow(self.lo,2))
        return diago

    def TraceRec(l1,l2):
        """ Trace le rectangle """
        plt.plot(l1, l2,color="green")
        plt.show()
        plt.close()
        figRec=plt.show()
        return figRec


    def TrRec(self):
        """ Trace le rectangle """
        
        fig = plt.figure()
        ax = fig.add_subplot(111)
        
        # paramétrage 
        rec = matplotlib.patches.Rectangle(self.p,self.lo,self.la, color="green",alpha=0.5)
        
        ax.add_patch(rec)
        ax.grid()
        plt.xlim([-20, 20])
        plt.ylim([-20, 20])
        
        fgrec=plt.show()      
        return fgrec


def main():
    
    # On définit un point de départ:
   
    # Point initiale
    PA=Point(0,0)
    print(PA)
    
    print("xA=",PA.x)
    print("yA=",PA.y)
    # Enregistrement des données du point initial
    Px0=PA.x
    Py0=PA.y
    P0=(Px0,Py0)
    
    
    # Instanciation classe MonRectangle
    Rec=MonRectangle(P0,10,5)
    print(Rec)
    print(repr(Rec))


    # On en déduit les 3 autres points à partir du point initial:
    
    PB=PA.move(Rec.lo,pi/2)
    print(PB)
    
#    print("new_xA=xB",PA.x)
#    print("new_yA=yB",PA.y)
    
    PC=PB.move(Rec.la,0)
    print(PC) 
    
    PD=PC.move(Rec.lo,-pi/2)
    print(PD) 
    
    # Liste des abscisses et ordonnées
    
    print("\nlx=",Point.lx)
    print("\nly=",Point.ly)
    lx=Point.lx
    ly=Point.ly
    # Ajout point initiale pour boucler le graphe
    lx.append(Px0)
    ly.append(Py0)
    

    # Calcul des grandeures - perimètre , surface, diagonale:
    
    print("\nPerimètre = " ,round(Rec.PerimRec(),2))
    print("Surface = " ,round(Rec.SurfRec(),2))
    print("Diagonale  = " ,round(Rec.DiagoRec(),2))


    # Tracés du rectangle Rec de la classe MonRectangle 
    
    # Tracé rectangle 1 
    MonRectangle.TraceRec(lx,ly)
    
    # Tracé du rectangle 2    
    Rec.TrRec()
    
    
if __name__=="__main__":
    main()      
        
