***Análisis de NLP: Análisis de Canciones de Gustavo Cerati***

**Descripción**

En este trabajo, voy a obtener la discografia de Gustavo Cerati mediante la técnica de web scrapping. La misma generara un corpus de 70 canciones que van desde el año 1993 al 2009. La fuente de la información proviene de la web letras.com

Como fan de Cerati, elegi analizar sus canciones ya que son lertras con muchos significados, desde lo superficial y mundano a lo profundo y etereo, haciendo escala en metáforas relacionadas al amor, muerte, vida y lealtad. En este análisis, me gustaria poder ver más allá de sus letras, en qué momento personal se encontraba Gustavo Cerati al momento de componer sus discos. El propósito de este proyecto es analizar la similitud o no similitud entre las canciones de los discos de Gustavo Cerati.

Descubrí que ciertas palabras que creía frecuentes en todos los discos (como “amor” o “vida”) tienen una presencia más fuerte en discos específicos, lo que refleja cambios temáticos a lo largo de su carrera. Se confirmaron hipótesis iniciales sobre la concentración de vocabulario relacionado con emociones y relaciones personales, aunque también surgieron términos inesperados ligados a crítica social. Me sorprendió que algunas canciones con palabras distintas aparecieran muy cercanas en similitud semántica usando embeddings, mostrando relaciones que no se ven con BoW o TF-IDF.

**Información del Corpus**

- Tipo: Música

- Tamaño: 70 textos, aproximadamente 3651 palabras totales

- Fuentes principales : www.letras.com

- Período temporal: 1999-2004

- Criterios de selección: Trayectoria solista de Cerati, tras su salida de Soda Stereo y previa a su fallecimiento.


**Técnicas de NLP Aplicadas**

- Preprocesamiento de texto (limpieza, tokenización, stopwords)

- Análisis con Bag of Words (BoW) y TF-IDF

- Análisis con Word Embeddings (spaCy)

- Técnica complementaria aplicada: Análisis de Senimientos con TextBlob

**Principales Hallazgos**

- Descubrí que ciertas palabras que creía frecuentes en todos los discos (como “amor” o “vida”) tienen una presencia más fuerte en discos específicos, lo que refleja cambios temáticos a lo largo de su carrera.
- Se confirmaron hipótesis iniciales sobre la concentración de vocabulario relacionado con emociones y relaciones personales, aunque también surgieron términos inesperados ligados a crítica personal (propia y ajena).



**Tecnologías Utilizadas**

trafilatura: 2.0.0
scikit-learn: 1.6.1
requests: 2.32.4
beautifulsoup4: 4.13.5
wordcloud: 1.9.4
numpy: 1.26.4
Pillow: 11.3.0
nltk: 3.9.1
matplotlib: 3.10.0
spacy: 3.8.7
pandas: 2.2.2
plotly: 5.24.1
gradio: 5.44.1
gensim: 4.3.3
TextBlob: 0.19.0

**Instrucciones de Reproducción**

1. Clonar este repositorio

2.Instalar dependencias: `pip install -r requirements.txt`

3. Ejecutar el notebook: `jupyter notebook notebooks/Cornes_TP_Integrador_Cerati`

**Limitaciones y Trabajo Futuro**

- No se pudo capturar completamente el tono poético o irónico de algunas letras, ya que ni BoW ni embeddings analizan metáforas profundas o estilo literario.
- Mejoraría la representación de canciones largas, utilizando embeddings contextualizados (tipo BERT) para cada verso, y analizando cambios de tono a nivel de estrofa.

**Autor**

Valeria Cornes - 28170133@ifts24.edu.ar

Trabajo Integrador - NLP - 25-09-2025