# Guide pour le lancement et l'utilisation de l'application

## Description rapide du principe de l'application

L'application est une application de gestion de produits d'une base de données
Elle permet à partir d'un client, d'interagir avec un serveur (qui sert de base de données)
et propose les fonctionnalitées classiques d'une base de données :

## Récupération du projet

Cloner le projet avec git avec la commande :
`git clone https://github.com/GregOurtiii/INFO910_introduction_devops.git`
Vous retrouverez les sources du client et du serveur python dans le dossier src.
Les fichiers .yaml pour Docker compose dans le fichier docker_compose.
Les fichiers .yaml pour Kubernetes dans le fichier kubernetes.

## Lancement de l'application

### docker compose :

- Rendez-vous dans le dossier "docker_compose".
- Téléchargez les images docker, et lancez l'image du client et du serveur dans le même network, via la commande :
  `docker-compose up`
- Récupérez l'id du conteneur client via la commande:
  `docker ps`
- Accédez ensuite au bash du client pour interagir avec le conteneur du client via la commande :
  `docker exec -it ID bash` ou ID correspond a l'id du conteneur client récupéré grace a la commande précédente
- Une fois dans le bash, lancez le client via la commande :
  ` python client.py`
- Vous pouvez maintenant interagir avec le conteneur du serveur à partir du conteneur du client en utilisant les
  différentes commandes proposées dans le menu affiché dans le bash du client lancé précédemment.

### kubernetes :

- Rendez vous dans le dossier "kubernetes".
- Démarrez minikube via la commande (cela peut prendre un certain temps) :
  `minikube start`
- Déployez les 2 fichiers .yaml afin de déployer le client et le serveur via les commandes :
  `kubectl apply -f serveur.yml` et `kubectl apply -f client.yml`
- Vérifiez que les pods sont bien en mode Running et récupérez le nom d'un des 2 clients via la commande :
  `kubectl get pods`
- Exécutez le client via la commande :
  `kubectl exec -it NOM -- sh` où NOM correspond au nom du pod du client récupéré grace a la commande précédente
- Accédez au bash du client via la commande :
  ` python client.py`
- Vous pouvez maintenant interagir avec le conteneur du serveur à partir du conteneur du client en utilisant les
  différentes commandes proposées dans le menu affiché dans le bash du client lancé précédemment.

## Description et Mode d'emploi de l'application :

L'application est une application de gestion d'un catalogue de produit contenu dans une base de données.
A partir du client, elle permet d'interagir avec un serveur (qui sert aussi de base de données)

Une fois le client lancé, vous aurez le choix entre 5 action:

- Lister tout les produits disponible dans le catalogue
- Lister un unique produit via son nom
- Ajouter un produit dans le catalogue
- Supprimer un produit du catalogue via son nom

Chaque produit dispose d'un id, d'un nom et d'un prix

## Auteurs :

BILLON Yohan
CLERC Gregory
M2 INFO - INFO 910 - Introduction DevOps
