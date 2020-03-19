# Mode d'emploi
- [Mode d'emploi](#mode-demploi)
  - [Installation](#installation)
  - [Utilisation normale](#utilisation-normale)
  - [Résumé du projet](#r%c3%a9sum%c3%a9-du-projet)
  - [Arguments supplémentaires](#arguments-suppl%c3%a9mentaires)
  - [Manuel du main](#manuel-du-main)
  - [Diagramme de classes et de packages](#diagramme-de-classes-et-de-packages)

## Installation
Mode d'emploi installation, testé sur les machines de l'IUT (Arch Linux):
```bash
python3.7 -m ensurepip --default-pip --user
```
```bash
setuptools wheel --user
```
```bash
cd ~/.local/bin
```
```bash
./pip3 install --upgrade pip --user
```
```bash
./pip3 install matplotlib && install numpy
```
## Utilisation normale
Lancez soit à la racine du git
```bash
python ./projet
```
ou dans le dossier courant
```bash
python ./__main__.py
```
## Résumé du projet
Le projet avait pour but de créer une application modulaire pouvant jouer à des jeux en tour par tour. Pour avoir un adversaire face à un utilisateur humain nous avons donc créé plusieurs algorithmes pouvant jouer au jeu, dont certains pouvant apprendre : grâce à des algorithmes d’apprentissage par renforcement ou « reinforcement learning ».  
L’application actuelle permet de jouer à différents jeux tels que le jeu de Nim, TicTacToe, Quoridor. Et face à un humain nous avons mis en place plusieurs types d’algorithmes tels que MinMax, QLearning  ou SARSA.
La modularité de l’application permet de créer de nouveaux jeux et algorithmes tout en préservant le bon fonctionnement des fonctionnalités. Le projet peut donc être utilisé sous forme d’API, un utilisateur peut incorporer les classes et fonctions dans son code.

## Arguments supplémentaires
Lancez soit à la racine du git
```bash
python ./projet -h
```
ou dans le dossier courant
```bash
python ./__main__.py -h
```
__Exemples:__
Faire un entrainement de 20000 parties:
```bash
python ./projet -t 20000
```
Faire un entrainement de 20000 parties et sauvegarder dans un fichier:
```bash
python ./projet -t 20000 -s
```
Charger un fichier qui a été sauvegardé:
```bash
python ./projet -l myfilename.pkl
```

## Manuel du main
![alt text](https://dwarves.iut-fbleau.fr/git/castel/PT-API-IA-python/raw/master/images/main.jpg)

## Diagramme de classes et de packages
![alt text](https://dwarves.iut-fbleau.fr/git/castel/PT-API-IA-python/raw/master/images/Class_Diagram.jpg)
![alt text](https://dwarves.iut-fbleau.fr/git/castel/PT-API-IA-python/raw/master/images/Package_Diagram.jpg)