#### Membres du groupe : Castel Aurélien, Léa Dacosta, Kevin Seri, Nicolas Guiblin
#### Tuteur : Florent Madelaine
<br>

# Cahier des charges PT
### Délais (Octobre 2019 à Mars 2020)  
<br>

## Sommaire

<br>
### I) Contexte
### II) Spécifications fonctionnelles
### III) Spécifications techniques
### IV) Diagrammes
<br>

## I) Contexte

<br>
Aujourd'hui, l'intelligence artificielle est en forte expansion dans tous les domaines. Elles s'appliquent notamment aux transports, aux jeux vidéos, aux systèmes embarqués ou encore aux diagnostics médicaux, etc. Afin d'en avoir une première approche, nous avons choisi d'implémenter une IA dans le cadre de notre projet tuteuré. Par ailleurs, la transformation digitale des entreprises est primordiale et nécessite la présence d'APIs (Interface de Programmation Applicative), qui facilitent l'intégration de logiciels. Nous avons donc décidé de lier ces deux concepts en réalisant une API d'intelligence artificielle.

Ce projet nous permet d'expérimenter le travail de groupe en totale autonomie. Ainsi, chacun peut apporter ses compétences et les élargir. Il nous permet aussi d'utiliser une méthode de gestion de projet qui correspond à celles mises en place dans les entreprises. Le groupe s'entretient donc régulièrement avec son tuteur, considéré comme client, afin de rendre compte de ses réalisations.

<br>
## II) Spécifications fonctionnelles

<br>
Le but de ce projet est de créer une API d’intelligence artificielle permettant
de jouer à n’importe quel jeu à deux joueurs en tour par tour et à information
complète tels que le jeu de Nim, le Korridor, etc.

Afin de déterminer les fonctionnalités que nous devrons au minimum
produire, nous utilisons la méthode MoSCoW :

* M : Must (fonctionnalités vitales)
* S : Should (fonctionnalités importantes)
* C : Could (fonctionnalités optionnelles)
* W : Would (fonctionnalités pour parfaire le projet)

<br>
#### Diagramme de MoSCoW

<br>
![alt text](https://dwarves.iut-fbleau.fr/git/castel/PT-API-IA-python/raw/master/images/MoSCoW.png)

<br>
## III) Spécifications techniques

<br>
Notre projet sera codé en Python. En effet, ce langage est le plus utilisé
dans le domaine de l’intelligence artificielle et possède de nombreuses
librairies. Parmi celles-ci, nous utiliserons anytree, matplotlib, networkx, numpy, pylab, etc. qui serviront principalement à représenter graphiquement les résultats obtenus des tests de nos intelligences artificielles.
De plus, c’est l’occasion de se former sur un langage qui nous est
inconnu.

Nous utiliserons dans un premier temps l’algorithme minimax, qui est
le plus adapté au type de jeux utilisés dans le cadre de ce projet. De ce fait,
l’IA prendra la meilleure décision parmi celles qui lui sont offertes, au vu de
l’état actuel du jeu.

L’API devra être la plus générique possible afin d’en faciliter son
intégration dans le développement du programmeur. Elle devra également
être mise à jour sans corruption des fonctionnalités des différents jeux.
Ainsi le projet utilisera le data-driven developpement : le projet est
piloté par les données qui lui sont fournies et l’application marchera peu
importe ces données.

<br>
#### Diagramme de Gantt

<br>
![alt text](https://dwarves.iut-fbleau.fr/git/castel/PT-API-IA-python/raw/master/images/Gantt.png)

<br>
#### Résultat des entretiens

*  24/10/2019 : Introduction du jeu "Le Korridor"
*  07/11/2019 : Explication de l'algorithme minimax
*  14/11/2019 : Confirmation du cahier des charges

<br>
## IV) Diagrammes

<br>
#### Diagramme de cas d’usage

<br>
![alt text](https://dwarves.iut-fbleau.fr/git/castel/PT-API-IA-python/raw/master/images/Cas%20d%27usage.png)