# -*- coding: utf-8 -*-
"""
Created on Sun May  2 11:36:06 2021

@author: Saadia Bayou
"""

from math import pi ,cos, sin, sqrt

class Point:
    """ classe Point définie les coordonnées 2D x et y d'un point 
    caractéristiques du point dans un plan son abscisse X et son ordonnée Y """
    
    lp=[]
    lx=[]
    ly=[]
    
    def __init__(self,X,Y):
        """ Constructeur point """
        self.x=X
        self.y=Y
        
     
        Point.lx.append(self.x)
        Point.ly.append(self.y)
        Point.lp.append(self)
        
    def __str__(self):
        s="\nLe point a pour coordonnées : x= {0} , y={1} "\
        .format(round(self.x,3),round(self.y,3))
        return s
    
    def __repr__(self):
        r="Point P=({0},{1})".format(self.x,self.y)
        return r 

    def move (self,rho,theta):
        """ Retourne un nouveau point"""
        # Projections
        self.x=self.x+rho*sin(theta)
        self.y=self.y+rho*cos(theta)
        p=Point(self.x,self.y)
        return p

    def milieu(self,p):
        """ Calcul le milieu du segment """
        self.x=(p.x+self.x)/2
        self.y=(p.y+self.y)/2 
        p=Point(self.x,self.y)
        return p
        
    def distance(self,p):
        """ calcul la distance entre deux points """
        lx=pow((p.x-self.x),2)
        ly=pow((p.y-self.y),2)
        l=lx+ly
        d=(sqrt(l))
        return d



def main():
    
    """ Instanciations et appels des méthodes de la class Point """
    
    # Instanciations
    
    
    P1=Point(0,0)    
    print("\nPoint P1: ",P1)
    
    #Attributs
    print("Absicce x1 = ",P1.x)
    print("Ordonnée y1 = ",P1.y)
        
    # Methode move
    
    P2=P1.move(10,pi/2)
    print("\nPoint P2 :", P2)
    
    print("\nlx=",Point.lx)
    print("\nly=",Point.ly)


    # Methode milieu    

    M=Point(10,10)
    N=Point(20,20)
    print("\nPoint M :",M)
    print("\nPoint N :",N)
    
    I=M.milieu(N)
    
    print("\nLe point I milieu du segment [NM]: ",I)

    #  Distance dMN , méthode distance    
    
    d=M.distance(N)
    print("\nLa distance MN est égale à :",round(d,3),"unités")


  
if __name__=="__main__":
    main()    
        
        
        
        
            
            
            
        
        