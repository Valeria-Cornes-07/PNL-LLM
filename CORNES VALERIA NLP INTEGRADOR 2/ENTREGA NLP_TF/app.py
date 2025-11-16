# -----------------------------------------
#              IMPORTACIONES
# -----------------------------------------
import streamlit as st

# Vectorstore y Embeddings
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()


# -----------------------------------------
#      CONFIGURACIÓN DE STREAMLIT
# -----------------------------------------
st.set_page_config(
    page_title="RAG Minería de Datos",
    layout="wide",
    page_icon="🧠"  
)


st.title("🧠 Sistema RAG - Minería de Datos")
st.write("Consulta información del curso usando un modelo local con RAG.")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    h1 {
        font-family: 'Poppins', sans-serif;
        color: #7A00CC !important;
        font-weight: 700;
    }
    </style>
""", unsafe_allow_html=True)


st.markdown("""
    <style>
    /* Cambiar color fondo de st.success */
    .stAlert > div {
        background-color: #E8D5FF !important;   /* lila claro */
        color: #4A0E78 !important;              /* violeta oscuro */
        border-left: 0.25rem solid #A259FF !important; /* borde lila */
    }
    /* También ajusto el borde redondeado y padding */
    .stAlert {
        border-radius: 10px !important;
    }
    </style>
""", unsafe_allow_html=True)



# -----------------------------------------
#          CARGA DEL MODELO (GEMINI)
# -----------------------------------------
@st.cache_resource(show_spinner=True)
def cargar_modelo_llm(temp=0.2):
    """
    Carga un modelo Gemini usando SÓLO google-generativeai.
    """
    api_key = os.getenv("GOOGLE_API_KEY", "")
    if not api_key:
        raise ValueError("❌ No se encontró GOOGLE_API_KEY en las variables de entorno.")

    genai.configure(api_key=api_key)

    model_id = "gemini-2.5-flash"

    model = genai.GenerativeModel(
        model_id,
        generation_config={
            "temperature": temp,
            "max_output_tokens": 2048
        }
    )

    return model, model_id


model, model_id = cargar_modelo_llm(0.2)
st.success(f"LLM cargado correctamente: {model_id}")


# -----------------------------------------
#        CARGA DE VECTORSTORE + RETRIEVER
# -----------------------------------------
@st.cache_resource(show_spinner=True)
def cargar_retriever():

    persist_directory = "./chroma_db3"

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = Chroma(
        persist_directory=persist_directory,
        embedding_function=embeddings,
        collection_name="mineria_datos"
    )
    print("Documentos en la colección:", vectorstore._collection.count())


    retriever = vectorstore.as_retriever(search_kwargs={'k': 4})
    return retriever


retriever = cargar_retriever()
st.success("Vectorstore cargado correctamente.")


# -----------------------------------------
#          FUNCIÓN DE RAG MANUAL
# -----------------------------------------
def rag_query(model, retriever, user_question):

    # 1. Buscar documentos
    docs = retriever.get_relevant_documents(user_question)

    print("========== DEBUG RAG ==========")
    print("📌 Pregunta del usuario:", user_question)
    print("📌 Cantidad de documentos recuperados:", len(docs))

    for i, d in enumerate(docs):
        print(f"\n--- Documento {i+1} ---")
        print("Metadata:", d.metadata)
        print("Contenido:", d.page_content[:500], "...\n")

    # 2. Crear contexto
    context_text = "\n\n".join(d.page_content for d in docs)

    print("📌 Largo del contexto:", len(context_text))
    print("\n📌 CONTEXTO (primeros 800 chars):\n", context_text[:800])
    
    # 3. Prompt enviado a Gemini
    prompt = f"""
    Actuá como un experto en Minería de Datos.
    Responde la pregunta SOLO usando el contexto dado.
    CONTEXTO:
    {context_text}
    PREGUNTA:
    {user_question}
    RESPUESTA:
    """

    print("\n📌 PROMPT FINAL ENVIADO A GEMINI (primeros 1000 chars):\n")
    print(prompt[:1000])
    print("\n================================")

    # 4. Llamada a Gemini (RAW)
    response = model.generate_content(prompt)

    print("\n📌 RAW RESPONSE DE GEMINI:")
    print(response)

    # 5. finish_reason del modelo
    try:
        fr = response.candidates[0].finish_reason
        print("\n📌 finish_reason:", fr)
    except:
        print("\n📌 No hay finish_reason disponible")

    # 6. Retorno seguro
    try:
        return response.text, docs
    except:
        print("\n⚠️ ERROR: response.text está vacío")
        return "Respuesta vacía", docs


# -----------------------------------------
#        INTERFAZ STREAMLIT (UI)
# -----------------------------------------
with st.form("formulario_pregunta"):
    pregunta_usuario = st.text_area(
        "Pregunta:",
        placeholder="Escribe tu pregunta aquí...",
        height=120
    )
    enviar = st.form_submit_button("Enviar")

if enviar:

    if not pregunta_usuario.strip():
        st.warning("Por favor, escribe una pregunta.")
        st.stop()

    with st.spinner("Generando respuesta..."):
        try:
            respuesta, documentos = rag_query(model, retriever, pregunta_usuario)

            st.text_area("Respuesta:", respuesta, height=200)

            # Mostrar documentos usados
            with st.expander("🔎 Documentos utilizados"):
                for doc in documentos:
                    st.markdown(f"**Archivo:** {doc.metadata.get('source', '')}")
                    st.write(doc.page_content)
                    st.write("---")

        except Exception as e:
            st.error(f"Error al procesar tu consulta: {e}")