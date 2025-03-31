# Chatbot RAG (Retrieval Augmented Generation)

Ce projet implémente un chatbot utilisant l'approche RAG (Retrieval Augmented Generation), qui enrichit les réponses du modèle avec des données contextuelles.

Ce projet est basé sur [le tutoriel RAG](https://www.youtube.com/watch?v=tcqEUSNCn8I&ab_channel=pixegami) de [pixegami](https://github.com/pixegami)

## Installation

```bash	
git clone https://github.com/Naimdeb/Python-RAG-LLM.git
```

```bash
pip install -r requirements.txt
```

## Prérequis

- Python version 3.8 ou supérieure
- Dépendances listées dans `requirements.txt`
- Clé API Mistral AI disponible [ici](https://console.mistral.ai/api-keys) (compte requis)
- Clé API Langsmith disponible [ici](https://smith.langchain.com/) (compte requis) (optionelle)

## Configuration

1. Dupliquez le fichier `.env.example` et renommez-le `.env`.
2. Configurez vos clés API dans le fichier `.env`.

## Utilisation
1. Placez vos documents dans le dossier `data/`. Le programme n'accepte que les fichiers .txt.

2. Exécutez le script de création de la base de données :

   ```bash
   python create_database.py
   ```

3. Lancez le script d'interrogation :

   ```bash
   python query_data.py
   ```

   Options possibles :

   - `--query "Prompt"` : Votre prompt, ou la question à poser au chatbot. Obligatoire.
   - `--similarity float` : Valeur de similarité entre les résultats, par défaut 0.7. Si aucun résultat n'est trouvé ou si le score de similarité est inférieur à 0.7, le programme affiche "Aucun résultat trouvé".


## Structure du projet

- `data/` : Contient les données source.
- `chroma/` : Base de données vectorielle.
- `create_database.py` : Script de création de la base de données.
- `query_data.py` : Script d'interrogation du chatbot.
