# Guía de Configuración del Entorno Local

Esta guía explica cómo configurar y usar el entorno virtual local para trabajar con los notebooks del Módulo 9.

## 📋 Prerequisitos

- Python 3.8 o superior instalado
- pip actualizado: `python -m pip install --upgrade pip`
- Acceso a internet para descargar dependencias

## 🚀 Configuración Inicial (Primera vez)

### 1. Activar el Entorno Virtual

El entorno virtual ya está creado en la carpeta `venv/`. Para activarlo:

**Windows (CMD):**
```cmd
venv\Scripts\activate
```

**Windows (PowerShell):**
```powershell
venv\Scripts\Activate.ps1
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

Deberías ver `(venv)` al inicio de tu línea de comandos.

### 2. Instalar Dependencias

Con el entorno activado, instala todas las dependencias:

```bash
pip install -r requirements.txt
```

Este proceso puede tardar varios minutos dependiendo de tu conexión.

### 3. Configurar API Keys

1. Abre el archivo `.env` en un editor de texto
2. Reemplaza los valores de ejemplo con tus credenciales reales:

```env
OPENAI_API_KEY=sk-tu_clave_real_aqui
GOOGLE_API_KEY=tu_clave_google_aqui
```

**Dónde obtener las claves:**
- OpenAI: https://platform.openai.com/api-keys
- Google Gemini: https://makersuite.google.com/app/apikey

### 4. Configurar Jupyter con el Entorno Virtual

Registra el entorno virtual como kernel de Jupyter:

```bash
python -m ipykernel install --user --name=modulo9-venv --display-name "Python (Modulo 9)"
```

## 💻 Uso Diario

### Iniciar Jupyter Notebook

1. **Activar el entorno** (si no está activado):
   ```bash
   venv\Scripts\activate
   ```

2. **Iniciar Jupyter**:
   ```bash
   jupyter notebook
   ```

3. **Seleccionar el kernel correcto** en el notebook:
   - Menu: Kernel → Change Kernel → "Python (Modulo 9)"

### Ejecutar Scripts Python

Con el entorno activado:

```bash
python tu_script.py
```

### Desactivar el Entorno

Cuando termines de trabajar:

```bash
deactivate
```

## 📦 Gestión de Dependencias

### Agregar una Nueva Dependencia

1. Instalarla en el entorno:
   ```bash
   pip install nombre-paquete
   ```

2. Actualizar requirements.txt:
   ```bash
   pip freeze > requirements.txt
   ```

### Actualizar Dependencias

```bash
pip install -r requirements.txt --upgrade
```

### Ver Paquetes Instalados

```bash
pip list
```

## 🔧 Solución de Problemas

### Error: "venv\Scripts\activate no se reconoce"

**Causa**: PowerShell tiene restricciones de ejecución.

**Solución**:
1. Abre PowerShell como Administrador
2. Ejecuta: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
3. Confirma con "S" (Sí)
4. Intenta activar de nuevo

### Error: "No module named 'xxx'"

**Causa**: La dependencia no está instalada.

**Solución**:
```bash
pip install nombre-del-modulo
```

### Jupyter no encuentra el kernel

**Solución**:
```bash
python -m ipykernel install --user --name=modulo9-venv --display-name "Python (Modulo 9)" --force
```

### Error al cargar .env

**Causa**: El archivo .env no está en el directorio correcto o tiene errores de formato.

**Solución**:
1. Verifica que `.env` esté en el mismo directorio que tus notebooks
2. No uses comillas en los valores
3. No dejes espacios alrededor del `=`

**Correcto:**
```env
OPENAI_API_KEY=sk-abc123
```

**Incorrecto:**
```env
OPENAI_API_KEY = "sk-abc123"
```

### ChromaDB da error de versión

**Solución**:
```bash
pip install chromadb --upgrade
pip install pydantic --upgrade
```

## 📚 Estructura del Proyecto

```
Modulo_9_LLMs_APIS_RAG/
│
├── venv/                          # Entorno virtual (NO subir a git)
├── .env                           # Credenciales (NO subir a git)
├── .gitignore                     # Archivos a ignorar en git
├── requirements.txt               # Dependencias Python
├── README_ENTORNO_LOCAL.md       # Esta guía
│
├── 01_Introduccion_APIs_LLMs.ipynb
├── 02_ChatGPT_Conceptos_Basicos.ipynb
├── 03_Gemini_API_Tareas_NLP.ipynb
├── 04_Carga_Documentos_RAG.ipynb
├── 05_Bases_Datos_Vectoriales.ipynb
├── 06_Sistema_RAG_Completo.ipynb
├── 07_Ollama_LLMs_Locales.ipynb
└── 08_Busqueda_Web_Actualizada.ipynb
```

## 🔒 Seguridad

### ❌ NUNCA hagas esto:

1. Subir `.env` a GitHub/GitLab
2. Compartir tu `.env` por email/chat
3. Hardcodear API keys en el código
4. Incluir claves en capturas de pantalla
5. Hacer commit de `venv/`

### ✅ SIEMPRE haz esto:

1. Mantener `.env` solo localmente
2. Usar `.gitignore` para proteger archivos sensibles
3. Rotar claves periódicamente
4. Usar variables de entorno
5. Revisar qué archivos subes a git

## 🎯 Flujo de Trabajo Recomendado

### Para Google Colab (Recomendado para empezar)

1. Sube el notebook a Colab
2. Usa "Secrets" de Colab para las API keys
3. Instala dependencias con `!pip install` en la primera celda

### Para Desarrollo Local (Recomendado para proyectos serios)

1. Activa el entorno virtual
2. Abre Jupyter Notebook
3. Selecciona el kernel "Python (Modulo 9)"
4. Las API keys se cargan automáticamente desde `.env`

## 📖 Recursos Adicionales

- **Documentación Python venv**: https://docs.python.org/3/library/venv.html
- **Guía pip**: https://pip.pypa.io/en/stable/
- **Jupyter Kernels**: https://jupyter-client.readthedocs.io/en/stable/kernels.html
- **python-dotenv**: https://github.com/theskumar/python-dotenv

## 🆘 Soporte

Si tienes problemas:

1. Verifica que el entorno esté activado (deberías ver `(venv)`)
2. Confirma que estás en el directorio correcto
3. Revisa que `.env` tenga las claves correctas
4. Intenta reinstalar: `pip install -r requirements.txt --force-reinstall`
5. Como último recurso, elimina `venv/` y créalo de nuevo:
   ```bash
   rmdir /s venv          # Windows
   rm -rf venv            # Linux/Mac
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```

---

**Última actualización**: 2025-10-30
