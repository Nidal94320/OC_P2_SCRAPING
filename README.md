
# Process running ETL pipeline (fr/en)

scraping script for https://books.toscrape.com/


## Comment executer en local le script python (en fr)

#### 1. Ouvrir un Terminal : "PowerShell" sous Windows et "Terminal" sous Mac

#### 2. Se placer dans un répertoire de travail (ex "mes documents") :

```bash
# navigation dans un terminal :
  pwd               # affiche le repertoire de travail
  ls                # liste les éléments contenus dans répertoire
  cd ..             # permet de remonter au dossier parent
  cd 'name_dossier' # permet d'accéder à un dossier fils
```

#### 3. Créer un nouveau dossier "etl_script" où l'on va importer le script python ETL à l'aide de la commande "mkdir" :

```bash
  mkdir etl_script
```

#### 4. Se placer dans le répertoire "ETL" à l'aide de la commande "cd" :

```bash
  cd etl_script
```

#### 5. Cloner le repo en entrant la commande suivante :

```bash
  git clone https://github.com/Nidal94320/OC_P2.git
```

#### 6. Créer un environnement virtuel à l’aide de la commande :

```bash
  python -m venv env
```

#### 7. Switcher sur l’environnement virtuel que l'on vient de créer :
```bash
env/Scripts/activate # sous Windows
source env/bin/activate # sous Mac

```
#### 8. Installer les packages Python :

```bash
pip install –r requirements.txt

```
#### 9. Exécuter le script en entrant la commande "python main.py" (patienter 5-10mn jusqu’à la fin de l’exécution) :

```bash
python main.py

```
#### 10. Accéder aux data

```bash
cd data     # Pour accéder aux données des livres de chaque catégorie au format csv
cd data/img # Pour accéder aux images des livres 

```
## Running locally the python script (in en)

#### 1. Open Shell

#### 2. Navigate into a work directory (ex "my documents) :

```bash
# to navigate in a terminal:
  pwd               # print working directory
  ls                # list folder elements
  cd ..             # navigate to the parent folder
  cd 'name_dossier' # navigate to a son folder 
```

#### 3. Create a new folder "etl_script" where you could import the repo :

```bash
  mkdir etl_script
```

#### 4. Navigate to etl_script/ :

```bash
  cd etl_script
```

#### 5. Clone the repo :

```bash
  git clone https://github.com/Nidal94320/OC_P2.git
```

#### 6. Create a new virtuel environment  through the command :

```bash
  python -m venv env
```

#### 7. Switch on the new virtuel environment you just created it :
```bash
env/Scripts/activate # under Windows
source env/bin/activate # under Mac

```
#### 8. Install required Python packages :

```bash
pip install –r requirements.txt

```
#### 9. Run the script :

```bash
python main.py

```
#### 10. Get data :

```bash
cd data     # To get books data through csv files (more info about how to read csv files https://www.youtube.com/watch?v=XsTvCcejcYE)
cd data/img # to get books images 

```


## Feedback/Question

If you have any feedback or questions, please reach out to me at nidalchateur@gmail.com

