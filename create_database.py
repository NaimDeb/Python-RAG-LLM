from langchain_mistralai.chat_models import ChatMistralAI
from langchain_mistralai.embeddings import MistralAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain.document_loaders import DirectoryLoader


DATA_PATH = "data/books"


def generate_data():
    documents =


# fonction load documents qui transforme tt le dossier en un seul document avec content et metadata
def load_documents():
    loader = DirectoryLoader(DATA_PATH, glob="*.txt")
    documents = loader.load()
    return documents

# On appelle text splitter pour découper notre document en morceaux
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=500,
    length_function=len,
    add_start_index=True,
)

def split_text(documents: list[Document])


# On coupe tout
chunks = text_splitter.split_documents(load_documents())
print(f'Découpé {len(DATA_PATH)} documents en {len(chunks)} morceaux')