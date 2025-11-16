---
title: MIA CHATBOT
emoji: 🧠
colorFrom: pink
colorTo: purple
sdk: streamlit
app_file: app.py
pinned: false
---

# Sistema RAG para Minería de Datos

Desarrollado como Trabajo Integrador N°2 - Procesamiento del Lenguaje Natural e Introducción a LLMs (IFTS 24)

Sistema de Retrieval-Augmented Generation (RAG) que permite consultar información de las unidades del curso de Minería de Datos mediante búsqueda semántica.

## Cómo usar

1. Escribe tu pregunta sobre Minería de Datos en el campo de texto
2. Haz click en "Consultar"
3. El sistema buscará información relevante y generará una respuesta fundamentada
4. Verás las fuentes citadas que se usaron para generar la respuesta

## Características

- Consultas en lenguaje natural
- Respuestas fundamentadas con citas
- Interfaz intuitiva
- Soporte para español técnico

## Tecnologías

- **LLM**: google/flan-t5-large
- **Embeddings**: Sentence Transformers (all-MiniLM-L6-v2)
- **Base de datos**: ChromaDB
- **Interfaz**: Streamlit

