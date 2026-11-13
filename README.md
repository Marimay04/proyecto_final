# 🎬 CINEMA ANALYTICS
## Plataforma de Gestión y Análisis de Información Cinematográfica

### 📌 1. Descripción del proyecto

Cinema Analytics es una aplicación web desarrollada como proyecto final de la asignatura Programación Aplicada.
Su propósito es facilitar la consulta, gestión, visualización y análisis de información relacionada con películas y plataformas de streaming.

La aplicación utiliza una arquitectura que integra diferentes tecnologías:

- **MongoDB Atlas:** almacena los registros de películas.
- **FastAPI:** permite consultar, procesar y administrar la información mediante una API REST.
- **Streamlit:** proporciona una interfaz gráfica interactiva para los usuarios.
- **Python:** permite desarrollar la lógica del sistema e integrar sus componentes.
- **Google Gemini:** incorpora inteligencia artificial para responder preguntas en lenguaje natural sobre los datos disponibles.

La plataforma permite consultar películas, aplicar filtros, visualizar estadísticas, agregar nuevos registros y realizar preguntas mediante inteligencia artificial.

Además, Cinema Analytics cuenta con una interfaz de temática cinematográfica, inspirada en las galas de premiación Oscar, que utiliza colores negros y dorados para ofrecer una experiencia visual atractiva.

### 🎯 2. Objetivo general

Desarrollar una aplicación web que permita gestionar, consultar y analizar información cinematográfica almacenada en MongoDB, integrando herramientas de programación, visualización de datos e inteligencia artificial.

### 🎯 3. Objetivos específicos

- Implementar una API REST mediante FastAPI para consultar y administrar registros cinematográficos.

- Establecer una conexión con MongoDB Atlas para acceder a la información almacenada.

- Diseñar una interfaz interactiva utilizando Streamlit que facilite la consulta y visualización de los datos.

- Incorporar herramientas de filtrado, estadísticas y representación gráfica de la información.

- Permitir la creación de nuevos registros de películas mediante formularios conectados con la API.

- Integrar Google Gemini para responder preguntas en lenguaje natural a partir de una muestra de los datos.

- Aplicar buenas prácticas de organización del código, documentación y protección de variables de entorno.


## 🏗️ 4. Arquitectura del sistema

Cinema Analytics utiliza una arquitectura cliente-servidor que permite separar la interfaz gráfica, la lógica del programa y el almacenamiento de información.

El sistema está compuesto por cuatro elementos principales:

1. **Frontend (Streamlit):** interfaz mediante la cual el usuario interactúa con la aplicación.
2. **Backend (FastAPI):** procesa las solicitudes y ejecuta las operaciones necesarias.
3. **Base de datos (MongoDB Atlas):** almacena los registros cinematográficos.
4. **Inteligencia artificial (Google Gemini):** genera respuestas en lenguaje natural a partir de una muestra de los datos.

### 4.1. Diagrama de arquitectura

```text
                  👤 USUARIO
                      |
                      v
              🎬 CINEMA ANALYTICS
                  (Streamlit)
                      |
                      | Solicitudes HTTP
                      v
                 ⚙️ FASTAPI
                   (Backend)
                      |
           +----------+----------+
           |                     |
           v                     v
      🗄️ MONGODB             🤖 GEMINI
      (Base de datos)        (IA externa)
           |                     ^
           |                     |
           +---- Datos ----------+
                      |
                      v
               ⚙️ FASTAPI
                      |
                      v
               🎬 STREAMLIT
                      |
                      v
                  👤 USUARIO
```

**Nota:** FastAPI es el encargado de consultar MongoDB y enviar una muestra de los registros a Gemini. MongoDB no se comunica directamente con Gemini.

### 4.2. Funcionamiento del sistema

El proceso general de funcionamiento se desarrolla de la siguiente manera:

1. El usuario ingresa a la aplicación Cinema Analytics desde su navegador.

2. Streamlit presenta una interfaz gráfica con herramientas para consultar, filtrar, visualizar y registrar información de películas.

3. Cuando el usuario realiza una acción, Streamlit envía una solicitud HTTP a FastAPI.

4. FastAPI interpreta la solicitud y, dependiendo de la operación, consulta o modifica los registros almacenados en MongoDB Atlas.

5. MongoDB devuelve la información solicitada y FastAPI la transforma en una respuesta JSON.

6. Streamlit recibe la respuesta y presenta los resultados mediante tablas, indicadores o gráficos.

7. Si el usuario realiza una pregunta mediante inteligencia artificial, FastAPI obtiene una muestra de hasta 30 registros de MongoDB y la envía a Google Gemini junto con la pregunta.

8. Gemini genera una respuesta que FastAPI devuelve a Streamlit para mostrarla al usuario.


## 🛠️ 5. Tecnologías utilizadas

### 5.1. Python

Python es el lenguaje principal utilizado para desarrollar Cinema Analytics.

Permite implementar la lógica de programación, gestionar solicitudes HTTP, procesar información y conectar las diferentes tecnologías del sistema.

### 5.2. FastAPI

FastAPI es un framework de Python utilizado para desarrollar el backend mediante una API REST.

En Cinema Analytics permite:

- Consultar películas almacenadas en MongoDB.
- Filtrar información mediante parámetros.
- Obtener estadísticas utilizando operaciones de agregación.
- Registrar nuevas películas.
- Procesar preguntas dirigidas a Gemini.

Además, FastAPI genera documentación interactiva de sus endpoints mediante Swagger UI, disponible en la ruta `/docs`.

### 5.3. MongoDB Atlas

MongoDB Atlas es un servicio de base de datos en la nube que permite almacenar y administrar información.

Cinema Analytics utiliza:

- **Base de datos:** `proyecto_streaming`
- **Colección:** `peliculas`

La información se almacena en documentos con una estructura similar a JSON.

Entre sus campos se encuentran el título, la popularidad, la calificación promedio, el conteo de votos, la fecha de lanzamiento y el idioma original.

### 5.4. Streamlit

Streamlit es un framework de Python que permite desarrollar aplicaciones web interactivas.

En el proyecto se utiliza para:

- Presentar la información mediante tablas.
- Aplicar filtros a los registros.
- Mostrar indicadores numéricos.
- Generar gráficos estadísticos.
- Registrar nuevas películas mediante formularios.
- Enviar preguntas al asistente de inteligencia artificial.

La interfaz utiliza una temática cinematográfica con colores negros y dorados, acompañada de un fondo inspirado en las galas de premiación.

### 5.5. Google Gemini

Google Gemini es un servicio de inteligencia artificial generativa.

Cinema Analytics utiliza su API para responder preguntas escritas en lenguaje natural.

FastAPI proporciona a Gemini una muestra de hasta 30 documentos de MongoDB y la pregunta del usuario.

El modelo procesa esa información y genera una respuesta en español.

**Limitación:** las respuestas de Gemini se basan en la muestra proporcionada. Por lo tanto, no necesariamente representan la totalidad de registros de la base de datos.

### 5.6. Otras herramientas

- **PyMongo:** permite establecer la conexión entre Python y MongoDB.
- **Pandas:** facilita la organización de registros en tablas y el procesamiento de datos.
- **Requests:** permite realizar solicitudes HTTP entre componentes y servicios externos.
- **Pydantic:** valida la estructura y los tipos de datos recibidos por FastAPI.
- **python-dotenv:** permite cargar variables de entorno desde el archivo `.env`.
- **Git:** administra el historial de cambios del código.
- **GitHub:** permite almacenar y compartir el repositorio entre los integrantes del equipo.
- **Visual Studio Code:** entorno utilizado para desarrollar y ejecutar el proyecto.


## 🎬 6. Funcionalidades principales

Cinema Analytics permite interactuar con información cinematográfica mediante una interfaz web conectada a una API REST y una base de datos MongoDB.

### 6.1. Consulta de películas

El usuario puede visualizar los registros almacenados en la colección `peliculas`.

La aplicación muestra información como:

- Título de la película.
- Popularidad.
- Calificación promedio.
- Cantidad de votos.
- Fecha de lanzamiento.
- Idioma original.
- Géneros y plataformas de streaming, cuando estén disponibles.

Los resultados se presentan mediante una tabla interactiva desarrollada con Streamlit.

### 6.2. Filtrado de información

Cinema Analytics permite seleccionar un campo de los registros y aplicar filtros por valores específicos.

El frontend envía los parámetros de búsqueda a FastAPI, que consulta MongoDB y devuelve los resultados.

Actualmente, el filtrado se realiza mediante coincidencias exactas entre campos y valores.

### 6.3. Estadísticas y visualización

El sistema permite realizar operaciones estadísticas mediante las funciones de agregación de MongoDB.

El usuario puede seleccionar:

- Un campo para agrupar los registros.
- Un campo numérico para sumar sus valores.

FastAPI procesa la solicitud y devuelve los resultados, que Streamlit presenta mediante tablas y gráficos de barras.

La interfaz también muestra indicadores calculados sobre los registros consultados.

### 6.4. Registro de nuevas películas

La aplicación dispone de un formulario que permite enviar nuevos registros a MongoDB.

Los campos del formulario son:

- Título.
- Popularidad.
- Calificación promedio.
- Conteo de votos.
- Fecha de lanzamiento.
- Idioma original.

FastAPI utiliza Pydantic para validar la estructura de los datos recibidos antes de almacenarlos.

Actualmente, el formulario utiliza valores enteros para popularidad, calificación promedio y conteo de votos.

### 6.5. Consultas mediante inteligencia artificial

Cinema Analytics incorpora una función de preguntas en lenguaje natural utilizando Google Gemini.

El usuario escribe una pregunta relacionada con las películas y FastAPI:

1. Recibe la pregunta.
2. Consulta una muestra de hasta 30 documentos de MongoDB.
3. Construye un mensaje con los datos y la pregunta.
4. Envía la solicitud a Gemini.
5. Recibe la respuesta generada.
6. Devuelve el resultado a Streamlit.

Esta funcionalidad permite explorar la información mediante preguntas escritas en español.

**Limitación:** Gemini únicamente recibe una muestra de los registros y no realiza una consulta exhaustiva de toda la colección.

---

## ⚙️ 7. Endpoints de FastAPI

Los endpoints son rutas de la API que permiten realizar operaciones sobre los datos.

La documentación interactiva está disponible en:

`http://127.0.0.1:8000/docs`

La dirección anterior corresponde a la configuración predeterminada. Si el servidor se inicia en otro puerto, debe utilizarse ese puerto.

### 7.1. GET /

**Función:** mostrar un mensaje de bienvenida de la API.

**Ejemplo:**

`GET http://127.0.0.1:8000/`

Devuelve información general sobre el servicio.

### 7.2. GET /datos

**Función:** consultar los registros almacenados en MongoDB.

**Parámetros opcionales:**

| Parámetro | Descripción |
|---|---|
| `campo` | Campo utilizado para filtrar. |
| `valor` | Valor que debe coincidir con el campo. |
| `limite` | Cantidad máxima de registros que se devuelven. |

**Ejemplo:**

`GET http://127.0.0.1:8000/datos?limite=5`

Este endpoint devuelve una respuesta JSON con la cantidad de documentos recuperados y sus datos.

### 7.3. GET /estadisticas

**Función:** agrupar registros y sumar los valores de un campo numérico.

**Parámetros:**

| Parámetro | Descripción |
|---|---|
| `agrupar_por` | Campo utilizado para formar los grupos. |
| `sumar` | Campo numérico cuyos valores se suman. |

**Ejemplo:**

`GET http://127.0.0.1:8000/estadisticas?agrupar_por=idioma_original&sumar=conteo_votos`

Esta consulta agrupa los registros por idioma original y suma el conteo de votos de cada grupo.

El resultado incluye la suma y la cantidad de registros correspondientes a cada grupo.

### 7.4. POST /datos

**Función:** crear un nuevo registro cinematográfico.

**Ejemplo de solicitud JSON:**

```json
{
  "titulo": "Película de ejemplo",
  "popularidad": 100,
  "calificacion_promedio": 8,
  "conteo_votos": 1500,
  "fecha_lazamiento": "2026-11-10",
  "idioma_original": "es"
}
```

FastAPI valida la información utilizando el modelo `NuevoRegistro`.

Si la operación se completa correctamente, devuelve un mensaje de confirmación y el identificador del registro creado.

**Nota técnica:** actualmente se utiliza `fecha_lazamiento` en el modelo de creación. Se conserva ese nombre por compatibilidad con el código implementado.

### 7.5. POST /preguntar

**Función:** procesar preguntas en lenguaje natural mediante Google Gemini.

**Ejemplo de solicitud JSON:**

```json
{
  "pregunta": "Menciona tres películas de los datos disponibles"
}
```

FastAPI consulta una muestra de películas, construye el mensaje para Gemini y devuelve la respuesta generada.

**Ejemplo de estructura de respuesta:**

```json
{
  "respuesta": "Respuesta generada por Gemini."
}
```

Para utilizar esta funcionalidad es necesario configurar `GEMINI_API_KEY` en el archivo `.env`.

La integración con Gemini requiere conexión a internet y disponibilidad del servicio externo.


## 💻 8. Instalación y configuración

Esta sección explica cómo instalar, configurar y ejecutar Cinema Analytics en un computador.

### 8.1. Requisitos previos

Para ejecutar el proyecto es necesario contar con:

- Python 3.11 o superior, compatible con las dependencias del proyecto.
- Visual Studio Code u otro editor de código.
- Git para clonar el repositorio.
- Conexión a internet.
- Acceso autorizado a MongoDB Atlas.
- Una clave válida de Google Gemini para utilizar la inteligencia artificial.

### 8.2. Clonar el repositorio

Abre una terminal y ejecuta:

```bash
git clone https://github.com/Gabrielapi0/proyecto_final.git
```

Después ingresa a la carpeta:

```bash
cd proyecto_final
```

Este procedimiento descarga una copia del código almacenado en GitHub.

### 8.3. Crear el entorno virtual

Se recomienda utilizar un entorno virtual para mantener las dependencias del proyecto separadas de otras instalaciones de Python.

En Windows:

```powershell
python -m venv venv
```

Activar el entorno:

```powershell
.\venv\Scripts\Activate.ps1
```

Si PowerShell bloquea la activación, puede habilitarse la ejecución de scripts únicamente para la sesión actual:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

Después vuelve a activar el entorno virtual.

Cuando esté activo, aparecerá `(venv)` al comienzo de la terminal.

### 8.4. Instalar las dependencias

Con el entorno virtual activado, ejecuta:

```powershell
python -m pip install -r requirements.txt
```

Este comando instala las librerías especificadas en el proyecto.

Para comprobar posibles conflictos entre dependencias:

```powershell
python -m pip check
```

### 8.5. Configurar las variables de entorno

Cinema Analytics utiliza variables de entorno para proteger la información de conexión a servicios externos.

En la carpeta principal del proyecto crea un archivo llamado:

`.env`

Agrega las siguientes variables:

```env
MONGO_URI=TU_CADENA_DE_CONEXION_MONGODB
GEMINI_API_KEY=TU_CLAVE_PRIVADA_DE_GEMINI
```

Reemplaza los valores de ejemplo por las credenciales correspondientes.

**Importante:**

- No publiques el archivo `.env` en GitHub.
- No escribas contraseñas directamente en el código.
- No compartas claves mediante capturas de pantalla.
- Comprueba que `.env` esté incluido en `.gitignore`.
- Revoca y reemplaza cualquier clave que haya quedado expuesta.

Para comprobar que el archivo está ignorado por Git:

```powershell
git check-ignore -v .env
```

### 8.6. Configurar MongoDB Atlas

La aplicación utiliza:

- Base de datos: `proyecto_streaming`
- Colección: `peliculas`

Para establecer la conexión:

1. Accede a MongoDB Atlas.
2. Verifica que tengas permisos sobre la base de datos.
3. Obtén una cadena de conexión válida.
4. Guarda la cadena en la variable `MONGO_URI` del archivo `.env`.
5. Comprueba que la dirección IP del computador esté autorizada en las opciones de acceso de red de MongoDB Atlas.

Por seguridad, se recomienda autorizar únicamente las direcciones IP necesarias.

### 8.7. Configurar Google Gemini

La aplicación utiliza la API de Google Gemini para responder preguntas sobre películas.

Para configurar esta funcionalidad:

1. Accede a Google AI Studio.
2. Genera una clave de API para un proyecto autorizado.
3. Guarda la clave en `GEMINI_API_KEY` dentro del archivo `.env`.
4. Comprueba que el modelo configurado en `api.py` esté disponible para tu proyecto.
5. Reinicia FastAPI después de modificar las variables de entorno.

La disponibilidad de los modelos puede cambiar. Si aparece un error HTTP 404, verifica que el identificador del modelo exista y esté disponible para la clave utilizada.

### 8.8. Ejecutar FastAPI

Abre una terminal con el entorno virtual activado y ejecuta:

```powershell
python -m uvicorn api:app --reload --env-file .env --port 8000
```

Si el puerto está ocupado, puedes utilizar otro puerto disponible, por ejemplo:

```powershell
python -m uvicorn api:app --reload --env-file .env --port 8002
```

Cuando el servidor inicie correctamente, aparecerá un mensaje similar a:

```text
INFO: Application startup complete.
```

Para consultar la documentación interactiva de la API, abre:

`http://127.0.0.1:8000/docs`

Si utilizaste el puerto 8002:

`http://127.0.0.1:8002/docs`

### 8.9. Configurar la dirección de la API

En el archivo `dashboard.py` se encuentra la variable:

```python
API = "http://127.0.0.1:8002"
```

Esta dirección indica dónde se encuentra ejecutándose FastAPI.

**El puerto configurado en `dashboard.py` debe coincidir con el puerto utilizado para iniciar FastAPI.**

Por ejemplo, si FastAPI utiliza el puerto 8000, modifica la variable:

```python
API = "http://127.0.0.1:8000"
```

### 8.10. Ejecutar Streamlit

Mantén FastAPI ejecutándose y abre una segunda terminal.

Activa el entorno virtual y ejecuta:

```powershell
python -m streamlit run dashboard.py
```

Streamlit normalmente inicia la aplicación en:

`http://localhost:8501`

Desde allí podrás utilizar Cinema Analytics.

### 8.11. Verificar el funcionamiento

Para comprobar que la aplicación funciona correctamente:

1. Inicia FastAPI.
2. Abre la ruta `/docs` y verifica que aparezcan los endpoints.
3. Ejecuta una consulta `GET /datos` y comprueba que MongoDB devuelva registros.
4. Inicia Streamlit.
5. Comprueba que aparezca la interfaz Cinema Analytics.
6. Revisa los filtros, indicadores, estadísticas y tablas.
7. Verifica que el formulario permita introducir datos de una película.
8. Prueba una pregunta mediante Gemini.

**Precaución:** el botón para guardar películas realiza una operación de escritura sobre MongoDB. Evita insertar registros de prueba en la base de datos compartida sin autorización.

---

## 🔧 9. Solución de problemas frecuentes

| Problema | Posible solución |
|---|---|
| Python no se reconoce | Verifica la instalación y la configuración de PATH. |
| No aparece `(venv)` | Activa el entorno virtual. |
| PowerShell bloquea scripts | Utiliza una política de ejecución temporal para la sesión. |
| Falta alguna librería | Ejecuta `python -m pip install -r requirements.txt`. |
| Falta `MONGO_URI` | Comprueba que esté definida en `.env`. |
| No conecta a MongoDB | Verifica la URI, las credenciales y los permisos de red. |
| Falta `GEMINI_API_KEY` | Comprueba la variable y reinicia FastAPI. |
| Gemini devuelve 404 | Verifica el identificador y la disponibilidad del modelo. |
| Gemini devuelve 401 o 403 | Revisa la clave y los permisos del servicio. |
| El puerto está ocupado | Detén el servidor anterior o utiliza otro puerto. |
| Streamlit no conecta con FastAPI | Comprueba que ambas aplicaciones utilicen el mismo puerto de API. |
| Error 422 al registrar datos | Verifica que los campos enviados coincidan con el modelo de Pydantic. |

### 9.1. Recomendaciones de seguridad

Las credenciales de MongoDB y Gemini deben permanecer exclusivamente en las variables de entorno.

El archivo `.gitignore` debe incluir, como mínimo:

```gitignore
.env
venv/
__pycache__/
```

Antes de publicar cambios, revisa los archivos incluidos en el commit y asegúrate de no compartir credenciales privadas.

---
---

## 📁 10. Estructura del proyecto

Cinema Analytics organiza sus principales componentes en archivos independientes, facilitando el desarrollo, mantenimiento y comprensión del sistema.

### 10.1. Organización de archivos

La siguiente estructura muestra los archivos principales utilizados por la aplicación:

```text
proyecto_final/
│
├── api.py
├── dashboard.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── assets/
│   └── fondo_cine.png
│
└── .env (archivo privado, no incluido en GitHub)
```

### 10.2. Descripción de los archivos

| Archivo | Función |
|---|---|
| api.py | Implementa el backend mediante FastAPI y administra las solicitudes a MongoDB y Gemini. |
| dashboard.py | Desarrolla la interfaz gráfica de Cinema Analytics utilizando Streamlit. |
| requirements.txt | Contiene las dependencias necesarias para ejecutar el proyecto. |
| README.md | Documenta las características, tecnologías, instalación y funcionamiento de la aplicación. |
| .gitignore | Evita que Git incluya archivos privados o innecesarios. |
| assets/fondo_cine.png | Imagen utilizada como fondo de la interfaz cinematográfica. |
| .env | Almacena las variables privadas MONGO_URI y GEMINI_API_KEY. |

El archivo `.env` debe crearse localmente y nunca debe publicarse en el repositorio.

---

## ⚠️ 11. Limitaciones y consideraciones técnicas

Aunque Cinema Analytics integra diferentes funcionalidades, existen algunas consideraciones que deben tenerse en cuenta.

### 11.1. Consultas mediante inteligencia artificial

La integración con Gemini utiliza una muestra de hasta 30 documentos de MongoDB.

Por esta razón, las respuestas generadas no necesariamente representan toda la colección de películas.

Además, el funcionamiento de esta herramienta depende de la conexión a internet y de la disponibilidad del servicio de Google.

### 11.2. Filtrado de información

El sistema permite filtrar registros por campos y valores específicos.

Actualmente, las consultas utilizan coincidencias exactas, por lo que algunos filtros pueden depender del tipo de dato almacenado.

### 11.3. Estadísticas

Las estadísticas se generan mediante operaciones de agrupación y suma realizadas en MongoDB.

Por ello, los resultados dependen de los campos seleccionados y de la estructura de los registros almacenados.

### 11.4. Registro de películas

El formulario permite crear nuevos registros mediante la API.

Actualmente, el modelo de validación utiliza números enteros para popularidad, calificación promedio y conteo de votos.

Asimismo, los registros nuevos pueden contener menos campos que los documentos originales de la colección.

### 11.5. Ejecución local

La aplicación está configurada para ejecutarse localmente mediante FastAPI y Streamlit.

Para utilizarla desde otro computador, es necesario instalar sus dependencias, configurar las variables de entorno y establecer correctamente la dirección de la API.

---

## 🚀 12. Posibles mejoras futuras

Como oportunidades de mejora se plantean:

- Incorporar búsquedas parciales por título de película.
- Implementar filtros combinados por idioma, popularidad y calificación.
- Permitir calificaciones con valores decimales.
- Agregar funciones para actualizar y eliminar registros.
- Mejorar las estadísticas con nuevos indicadores cinematográficos.
- Ampliar las consultas de inteligencia artificial para analizar conjuntos de datos más extensos.
- Incorporar controles adicionales de validación y seguridad.
- Facilitar el despliegue de la aplicación en un servidor accesible mediante internet.

Estas propuestas representan posibles desarrollos futuros y no funcionalidades ya implementadas.

---

## 🏆 13. Conclusiones

El desarrollo de Cinema Analytics permitió integrar diferentes herramientas de programación para construir una aplicación web orientada a la gestión y análisis de información cinematográfica.

Mediante MongoDB Atlas se implementó el almacenamiento de datos, mientras que FastAPI permitió desarrollar una API REST para consultar, procesar y registrar información.

Streamlit facilitó la creación de una interfaz interactiva que permite visualizar registros, aplicar filtros y generar gráficos estadísticos.

Adicionalmente, la integración con Google Gemini incorporó la posibilidad de realizar consultas en lenguaje natural utilizando una muestra de los datos disponibles.

El proyecto permitió aplicar conocimientos relacionados con programación en Python, bases de datos, APIs REST, visualización de información, inteligencia artificial y control de versiones mediante Git y GitHub.

En conclusión, Cinema Analytics demuestra cómo diferentes tecnologías pueden integrarse para transformar una colección de datos en una aplicación interactiva que facilita su consulta y análisis.


##  Integrantes

- Gabriela Pinzon
- Juan Eduardo Chiquiza
- Mariana Mayorga
- Juan Jose Robles

**Proyecto:** Cinema Analytics

**Asignatura:** Programación Aplicada

**Tipo de proyecto:** Proyecto final universitario

**Año:** 2026
