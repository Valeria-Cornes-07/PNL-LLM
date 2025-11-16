import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from huggingface_hub import hf_hub_download

# ======================================
# Cargar variables de entorno (API key)
# ======================================
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if api_key:
    os.environ["GOOGLE_API_KEY"] = api_key
else:
    raise ValueError("GOOGLE_API_KEY no encontrada. Configura el secret en HF Spaces.")

DATA_PATH = "./documentos"
CHROMA_DB_PATH = "./chroma_db3"

def main():
    print("🚀 Iniciando proceso de ingesta...")

    # Verificar que la carpeta de datos existe
    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(f"No existe la carpeta de documentos: {DATA_PATH}")

    pdf_files = [f"UNIDAD_{i}.pdf" for i in range(1, 13)]
    all_chunks = []

    for pdf_name in pdf_files:
        pdf_path = os.path.join(DATA_PATH, pdf_name)  # ✅ CORREGIDO AQUÍ

        if not os.path.exists(pdf_path):
            print(f"⚠️ Archivo no encontrado: {pdf_name}, se omite.")
            continue

        # Cargar PDF
        loader = PyPDFLoader(pdf_path)
        documents = loader.load()

        # Dividir texto en chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=100
        )
        chunks = text_splitter.split_documents(documents)
        all_chunks.extend(chunks)

        print(f"✅ Procesado {pdf_name}: {len(chunks)} chunks")

    if not all_chunks:
        raise ValueError("No se cargaron documentos. Verifica que los PDFs existan.")

    # Crear embeddings con HuggingFace
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Crear base vectorial con Chroma
    vector_db = Chroma.from_documents(
        documents=all_chunks,
        embedding=embeddings,
        persist_directory=CHROMA_DB_PATH,
        collection_name="mineria_datos"
    )

    vector_db.persist()
    print(f"🎯 Total: {len(all_chunks)} chunks guardados en {CHROMA_DB_PATH}")

if __name__ == "__main__":
    main()