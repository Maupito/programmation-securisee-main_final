# Programmation sécurisée - IR4

## Introduction

Bienvenue dans le dépôt du cours de programmation sécurisée en IR4.

Ce dépôt a pour objectif de vous présenter les bases de Git et du framework web Python [Flask](https://flask.palletsprojects.com/).

Le fichier que vous êtes en train de lire s'appelle README (il faut donc le lire).
GitHub utilise la syntaxe [Markdown](https://www.markdownguide.org/) pour donner à ce texte **brut** un beau *formatage*.

Il faut toujours qu'un dépôt de code contienne ce fichier README ou README.md pour aider les utilisateurs à comprendre :

1. l'objectif du dépôt ;
2. comment installer l'application hébergée sur ce dépôt (installation des dépendances, compilation, etc.) ;
3. comment utiliser l'application ;
4. les limites du projet, la politique de contribution, la license, etc.

## Installation

### Cloner le dépôt

Cloner ce dépôt dans le répertoire de travail avec la commande :

```
git clone https://github.com/cseijido-esaip/programmation-securisee.git
```

### (Optionnel) Créer un nouvel environnement virtuel

Pour Linux ou MacOS

```bash
python3 -m venv .venv
source .venv/bin/activate
.venv/bin/python3 -m pip install --upgrade pip
```

Pour Windows

```shell
python -m venv .venv
.venv\Scripts\activate.bat
python -m pip install --upgrade pip
```

*Pour plus d'informations sur les environnements virtuels, consulter la [documentation officielle](https://docs.python.org/3/library/venv.html).*

### Installer les paquets nécessaires

Installer les paquets nécessaires avec la commande :

```bash
pip install -r requirements.txt
```

Liste des dépendances directes :

- flask

## Exécuter le programme

Exécuter la commande suivante pour démarrer l'application :

```bash
python first_server/app.py
```
