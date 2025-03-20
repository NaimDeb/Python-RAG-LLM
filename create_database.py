from langchain_mistralai.chat_models import ChatMistralAI
from langchain_mistralai.embeddings import MistralAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain.document_loaders import DirectoryLoader
import os
import shutil
from dotenv import load_dotenv


load_dotenv()

DATA_PATH = "data/books"
CHROMA_PATH = "chroma"


def main():
    generate_data()




def generate_data():
    documents = load_documents()
    chunks = split_text(documents)
    # save_to_chroma




# fonction load documents qui transforme tt le dossier en un seul document avec content et metadata
def load_documents():
    loader = DirectoryLoader(DATA_PATH, glob="*.txt")
    documents = loader.load()
    return documents

# On appelle text splitter pour découper notre document en morceaux
def split_text(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=500,
        length_function=len,
        add_start_index=True,
    )
    chunks = text_splitter.split_documents(documents)
    print(f'Découpé {len(DATA_PATH)} documents en {len(chunks)} morceaux')

    # document = chunks[10]
    # print(document.page_content)
    # print(document.metadata)

    return chunks


def save_to_chroma(chunks):
    #Clear the database
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)

    # Create a new DB from the documents.
    db = Chroma.from_documents(
        chunks,  ,persist_directory=CHROMA_PATH
    )
    db.persist()
    print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}.")


if __name__ == "__main__":
    main()
