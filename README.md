#Lancement de l'api en local 
Avant de commencer, soyez sûr d'avoir instller MySql sur votre ordianteur.

  - Dans un premier, lancer une interface ou terminal MySql, et lancer ces commandes:
    - create database aperette;
    - create user 'aperette'@'localhost' identified by 'Epsi2021!';
    - grant all privileges on aperette.* to 'aperette'@'localhost';
  - Cloner ce dépot, puis placez-vous dans Aperette
  - Activer ou créer un environnement virtuel :
    - pip3 install virtualenv
    - python3 -m venv [Le nom que vous lui donnez]
    - source [Le nom que vous lui donnez]/bin/activate
   
   Pour utiliser Swagger:
    - python manage.py migrate
    - python manage.py runserver 
    - Allez à l'adresse indiquée dans le terminal
   
   Pour lancer les tests :
    - python manage.py test aperetteAPI.tests.test_categories.CategorieTest.str_categorie
    - python manage.py test aperetteAPI.tests.test_aperettes.AperetteTest.str_aperette
    - python manage.py test aperetteAPI.tests.test_ingredients.IngredientTest.str_ingredient


# Aperette Présentation

Aperette est une api contenant trois tables qui sont Aperette, Categorie et Ingredient.

Une aperette est un accompagnement que vous retrouvez lors de vos apéritifs, et qui est associé à un alcool avec lequel il se marie le
mieux.
Cette table contient un id, un nom, une photo, un booléen qui nous indique si l'aperette est une recette ou non (exemple dés de fromage et mini quiches), un alcool associé, avec lequel il s'accord le mieux, une liste de catégories, et d'ingrédients si l'aperette est une recette.

La table catégorie à une relation many to many avec la table aperette, et ne contient qu'un id et un nom.
Pour la table ingrédient, c'est relativement la même chose que la table catégorie, sauf que cette foreign key peut être nulle.

# Les choix techniques

Nous avons choisi de travailler pour le backend sur du Django/python, au vu des connaissances que nous avions pour ce langage et du fait qu'il soit compatible
avec le frontend, rédigé en VueJs.

Une fois terminée, cette API a été déposé sur un serveur ubuntu, nous permettant d'y accéder sans problème. Ce serveur est constamment disponible, grâce au gestionnaire de processus pm2, et évite de lancer le runserver pour obtenir les données à chaque fois.

# Les test présents
Quand on developpe une application, il est important de faire des tests, afin de savoir si ce que l'on code va gérer tous les cas d'utilisation et de voir les éventuels problèmes.
Nous avons écrit un test pour chaque table. Ces trois tests ont tous la même fonctionnalité, à savoir : vérifier que l'on rentre bien un string pour le nom.

# Swagger

Swagger a été mis en place afin de documenter notre api. Elle montre les différents urls disponibles ainsi que les actions possibles sur ces chemins
d'accès.
Il est également possible de tester et de mettre des paramètres pour chaque chemin.
