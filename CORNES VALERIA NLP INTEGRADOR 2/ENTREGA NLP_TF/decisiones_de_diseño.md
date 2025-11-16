## Punto 4: Definí tu stack


| Componente | Tecnología elegida | Justificación |
|------------|-------------------|---------------|
| LLM | Gemini |Modelo potente y accesible|
| Embeddings | Hugging Face | Para despliegue en la plataforma sin conflictos  |
| Vector DB | ChromaDB | Obligatorio |
| Orquestación | LangChain | Obligatorio |
| Interfaz | Streamlit | Obligatorio |
| Deployment |  HF Spaces | Accesible con link |
| Interfaz | Streamlit | Obligatorio |

### Decisiones de Diseño

#### ¿Por qué elegí gemini-2.5-flash?

Porque es un LLM conversacional robusto aun en su versión flash. En este caso tengo acceso gratuito a la API de Gemini por ser estudiante (Acceso libre por un año). Su implementación es sencilla y no me implica descargar un modelo de HuggingFace que puede ser pesado.

#### ¿Por qué chunk_zise 1000 con 100 overlap?

Porque al definir un tamaño máximo de 1000 caracteres con un solapamiento entre chunks de 100 caracteres, se conserva mejor el contexto entre fragmentos.

#### ¿Por qué top-k = 4?

En este caso, definií el k=4 para que el modelo, al momento de buscar similitudes semánticas en la base vectorial, limite su búsqueda a los 4 resultados más relevantes.

