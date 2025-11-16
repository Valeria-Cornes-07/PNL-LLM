# Modulo 9: LLMs, APIs y Sistemas RAG
## Procesamiento del Habla e Introduccion a LLMs

---

## ¿Que es este modulo?

Este modulo final integra todo lo aprendido para construir sistemas inteligentes de procesamiento del lenguaje natural usando modelos de lenguaje grandes (LLMs).

**Vas a aprender a**:
- Conectarte a APIs de LLMs (OpenAI, Gemini)
- Construir sistemas RAG (Recuperacion y Generacion Aumentada)
- Trabajar con bases de datos vectoriales
- Integrar busqueda web y modelos locales
- Crear aplicaciones practicas de procesamiento de texto

---

## Cuaderno 1: Introduccion a APIs y LLMs

### ¿Que es una API?

Una API (Application Programming Interface) es una interfaz que permite que dos sistemas se comuniquen entre si. En nuestro caso, nos permite enviar texto a un modelo de lenguaje (como GPT-4) y recibir una respuesta procesada.

**Analogia**: Sos el cliente en un restaurante, la API es el mozo, y la cocina es el modelo de lenguaje.

---

### Parametros Configurables en LLMs

**Temperature** (0-2): Controla la aleatoriedad de las respuestas
- `0.0` = Deterministico, siempre responde igual (ideal para extraer datos)
- `0.7` = Balance entre creatividad y consistencia
- `1.5-2.0` = Muy creativo y variado

**Model**: Que modelo usar (calidad vs costo vs velocidad)
- `gpt-4o-mini` = Rapido, economico
- `gpt-4o` = Mas potente, mejor razonamiento

---

## Cuaderno 2: ChatGPT - Conceptos Basicos

### ¿Que son los System Prompts?

Los **system prompts** definen el comportamiento del asistente antes de la conversacion. Le indican que rol debe cumplir, como debe responder, y que restricciones debe seguir.

**Ejemplo**: "Sos un asistente experto en literatura argentina. Responde de forma academica pero accesible."

---

### Conversaciones Multi-Turno

Las conversaciones multi-turno permiten mantener **contexto** entre mensajes. El modelo recuerda lo que se dijo anteriormente en la conversacion.

**Roles en la conversacion**:
- `system`: Define el comportamiento del asistente
- `user`: Los mensajes del usuario
- `assistant`: Las respuestas previas del modelo

---

## Cuaderno 3: Gemini API - Tareas de NLP

### Tareas de PLN con Gemini

Gemini de Google puede realizar multiples tareas de Procesamiento del Lenguaje Natural sin necesidad de entrenamiento previo.

**Tareas cubiertas**:
- Sumarizacion (resumir textos)
- Analisis de sentimiento
- Reconocimiento de Entidades (NER)
- Respuesta a preguntas
- Traduccion
- Clasificacion zero-shot

---

### ¿Que es Zero-Shot Classification?

Clasificacion **sin entrenamiento previo**: el modelo puede categorizar textos en clases que nunca vio durante su entrenamiento, solo con las instrucciones que le des en el prompt.

**Ejemplo**: "Clasifica este texto en: queja, elogio, consulta o agradecimiento"

---

## Cuaderno 4: Carga de Documentos para RAG

### ¿Que es Document Loading?

El **Document Loading** es el proceso de cargar, leer y preparar documentos de diferentes formatos (PDF, TXT, HTML, DOCX) para procesarlos con LLMs.

**Libreria clave**: LangChain ofrece "Document Loaders" especializados para cada tipo de archivo.

---

### Text Splitting (Division de Texto)

Los LLMs tienen limites de tokens. El **Text Splitting** divide documentos largos en fragmentos (chunks) mas pequenos que el modelo pueda procesar.

**Parametros importantes**:
- `chunk_size`: Tamano de cada fragmento (ej: 1000 caracteres)
- `chunk_overlap`: Superposicion entre fragmentos (ej: 200 caracteres) para mantener contexto

---

## Cuaderno 5: Bases de Datos Vectoriales

### ¿Que son los Embeddings?

Los **embeddings** son representaciones numericas (vectores) del significado del texto. Textos con significados similares tienen embeddings similares.

**Ejemplo**: "excelente", "genial", "buenisimo" tienen vectores cercanos en el espacio multidimensional.

---

### Busqueda Semantica vs Busqueda Tradicional

**Busqueda tradicional**: Solo encuentra palabras exactas ("asado")

**Busqueda semantica**: Encuentra por significado, aunque uses palabras diferentes
- Buscar "lugar para comer carne" encuentra reviews de parrillas aunque no digan "carne"
- Entiende sinonimos, contexto y modismos argentinos

**Herramienta**: ChromaDB almacena y busca documentos por similitud semantica.

---

## Cuaderno 6: Sistema RAG Completo

### ¿Que es RAG?

**RAG** (Retrieval Augmented Generation) combina busqueda de informacion con generacion de texto.

**Como funciona**:
1. **Retrieval** (Recuperacion): Busca documentos relevantes en tu base vectorial
2. **Augmented Generation**: Pasa esos documentos como contexto a un LLM para generar una respuesta

**Ventaja**: El LLM usa TUS datos especificos, no solo su conocimiento general.

---

### Pipeline Completo de RAG

**Flujo de trabajo**:
1. Usuario hace una pregunta
2. Sistema busca documentos relevantes (busqueda semantica)
3. Documentos se pasan como contexto al LLM
4. LLM genera respuesta basada en esos documentos
5. Respuesta es verificable (sabes que documentos se usaron)

**Aplicaciones**: Chatbots empresariales, asistentes de documentacion, sistemas de recomendacion

---

## Cuaderno 7: Ollama - LLMs Locales

### ¿Que es Ollama?

**Ollama** permite ejecutar modelos de lenguaje directamente en tu computadora, sin necesidad de APIs externas o conexion a internet.

**Ventajas**:
- Privacidad total (los datos no salen de tu maquina)
- Sin costos de API
- Sin limites de uso
- Soberania de datos

---

### Modelos Locales vs APIs en la Nube

**Local (Ollama)**:
- Privado y seguro
- Gratis (despues de descargar)
- Requiere hardware potente
- Modelos mas pequenos

**API en la Nube (OpenAI/Gemini)**:
- Modelos mas potentes
- No requiere hardware especial
- Tiene costo por uso
- Datos salen de tu control

**Estrategia hibrida**: Embeddings locales + LLM en la nube (ahorro de 70-80% en costos)

---

## Cuaderno 8: Busqueda Web Actualizada

### ¿Por que necesitamos busqueda web?

Los LLMs tienen un **knowledge cutoff** (fecha de corte de conocimiento). No saben sobre eventos recientes ni informacion actualizada.

**Solucion**: Integrar busqueda web en tiempo real para darle al LLM informacion fresca sobre:
- Noticias recientes
- Datos actuales (clima, precios, horarios)
- Informacion que cambia frecuentemente

---

### Integracion de LLM + Busqueda Web

**Flujo de trabajo**:
1. Usuario pregunta algo actual ("¿Como esta el dolar hoy?")
2. Sistema detecta que necesita informacion actualizada
3. Realiza busqueda web (SERP API, Bing, Google)
4. Extrae informacion relevante de los resultados
5. Pasa resultados como contexto al LLM
6. LLM genera respuesta basada en datos actualizados

**Resultado**: Respuestas precisas y actualizadas combinando busqueda + generacion

---

## Resumen del Modulo

### Integracion de Todos los Conceptos

Este modulo te preparo para construir **aplicaciones inteligentes de PLN**:

1. **APIs**: Conectarte a modelos potentes
2. **Prompting**: Controlar el comportamiento del modelo
3. **Documentos**: Cargar y procesar informacion
4. **Vectores**: Buscar por significado, no por palabra
5. **RAG**: Combinar busqueda + generacion
6. **Local**: Ejecutar modelos sin internet
7. **Web**: Integrar informacion actualizada

**Objetivo final**: Crear sistemas que responden preguntas usando tus datos especificos y fuentes actualizadas.

---

## Proximos Pasos

### Como aplicar lo aprendido

**Proyectos sugeridos**:
- Chatbot para documentacion empresarial
- Asistente de atencion al cliente con tu base de conocimiento
- Sistema de recomendaciones basado en reviews
- Analizador de noticias con busqueda actualizada
- Tutor personalizado con material educativo especifico

**Herramientas que dominas ahora**:
- OpenAI API / Gemini API
- ChromaDB para busqueda semantica
- LangChain para pipelines complejos
- Ollama para deployment privado
- Gradio para interfaces web rapidas
