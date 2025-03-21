
from langchain_mistralai.embeddings import MistralAIEmbeddings
from langchain_community.vectorstores import Chroma
import argparse
from langchain.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
import os


load_dotenv()

#Prepare the DB

# todo : chekc if can be removed
CHROMA_PATH = "chroma"


PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
Your answer should always be in French, translate it before talking.
Your answer should always start by greeting the user.
"""

def main():
    # --- On crée le CLI ---

    ##Crée une option --query pour l'utiliser quand on crée
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", type=str, required=True)
    args = parser.parse_args()

    query_text = args.query

    # --- On prépare la DB ---

    #initialise MistralAiEmbeddings
    embedding_function = MistralAIEmbeddings(model="mistral-embed")
    # On initialise la db Chroma
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # --- On recherche la DB ---

    # todo : pourquoi pas d'autres 
    #On fait la recherche avec le query text donné par l'utilisateur, et on affiche les 3 plus proches
    # Results est un tuple de doc et _score ?
    results = db.similarity_search_with_relevance_scores(query_text, k=3)

    # Failsafe au cas ou y'a 0 résultat ou que le score de similarité est inferieur a 0.7
    if len(results) == 0 or results[0][1] < 0.7:
        print (f"Aucun résultat trouvé pour votre query")
        return
    
    # On join chaque doc et son score en une seule string, avec une délimitation ---
    # Fait une boucle sur results en décomposant chaque tuple en doc et _score
    # Puis on récupère doc.page_content et on le join avec \n\n---\n\n
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])

    # On crée le prompt avec ChatPromptTemplate, on lui donne notre propre template PROMPT_TEMPLATE
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)

    # on remplit context et question du prompt
    prompt = prompt_template.format(context=context_text, question=query_text)

    print (prompt)

    # --- On fait la requête ---

    # On initialise le modèle AI, et on lui donne le prompt
    model = ChatMistralAI()
    response_text = model.predict(prompt)

    # On récupère toutes les métadata de results pour donner les sources
    sources = [doc.metadata.get("source") for doc, _score in results]

    # On l'append dans une seule string avec la réponse de l'IA
    formatted_response = f"Response: {response_text}\nSources: {sources}"


    print (formatted_response)



if __name__ == "__main__":
    main()
    

