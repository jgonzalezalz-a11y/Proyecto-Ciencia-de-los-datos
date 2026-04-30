Primera y segunda entrega Proyecto Ciencia de los datos:
Daniel Esteban Flórez Cobos (1000.150.507), Juan Esteban Gonzalez Alzate (1055.751.386)
# Modelo Predictivo de Empleabilidad Estudiantil basado en Variables Académicas y Laborales

Este repositorio contiene la segunda fase del desarrollo de un sistema web integral diseñado para estimar el estado de contratación y el paquete salarial de estudiantes universitarios. 

En esta **Entrega 2**, el enfoque principal ha sido la construcción de la arquitectura Cliente-Servidor, la canalización de datos (pipeline) y el preprocesamiento de las variables.

---

## 📂 1. Código Fuente

El proyecto sigue una arquitectura desacoplada separando el Frontend del Backend, lo que permite escalabilidad y un flujo de datos limpio:

```text
/
├── 📄 app.py          # Backend (Python/Flask): Motor de preprocesamiento y API REST.
├── 📄 index.html      # Frontend: Interfaz de usuario con 22 variables de entrada.
├── 📄 script.js       # Lógica del cliente: Consumo de la API mediante fetch().
├── 📄 styles.css      # Estilos personalizados (complementarios a Bootstrap).
├── 📄 README.md       # Documentación del proyecto.
└── 📊 student_placement_prediction_dataset_2026.csv # Dataset original (Entrega 1).
Este repositorio contiene la implementación inicial (Frontend) de un sistema web diseñado para estimar el estado de contratación (empleabilidad) y el paquete salarial de estudiantes universitarios, basado en su perfil académico y habilidades.


 Resumen del Proyecto y Requerimientos

Este proyecto nace como respuesta a la necesidad de construir una interfaz intuitiva para un modelo de Machine Learning, utilizando el conjunto de datos `student_placement_prediction_dataset_2026.csv`. 

A continuación, se detalla cómo se abordaron los requerimientos del proyecto:

### 1. Descripción del Dataset
El proyecto se basa en el análisis de un conjunto de datos que detalla el perfil de los estudiantes.
* **Fuente:** `student_placement_prediction_dataset_2026.csv`, es de acceso libre desde la plataforma Kaggle.
* **Variables Predictoras (Features):** Incluye datos académicos y extracurriculares como `cgpa` (promedio), `coding_skill_score`, número de pasantías (`internships_count`), nivel de la universidad (`college_tier`), carrera (`branch`), entre otras.
* **Variables Objetivo (Targets):** * `placement_status`: Clasificación (Contratado / No Contratado).
  * `salary_package_lpa`: Regresión (Estimación del salario en LPA).

### 2. Análisis Preliminar de Datos (EDA)
Antes del desarrollo del modelo (Backend), se planteó la siguiente estrategia de visualización para entender los datos:
* **Distribución de Clases:** Gráficos de barras para evaluar el balance de `placement_status`.
* **Mapas de Calor (Heatmaps):** Para identificar las correlaciones más fuertes con el salario (ej. CGPA y habilidades de programación).
* **Análisis Bivariado:** Uso de Boxplots y Scatter plots para cruzar variables clave (como puntajes de aptitud) contra el estado de contratación.

### 3. Implementación del Frontend
Se construyó una interfaz de usuario limpia, responsiva y fácil de usar, separando las responsabilidades en distintos archivos para mantener las buenas prácticas:
* **HTML5:** Estructura semántica (`index.html`).
* **CSS3 & Bootstrap 5:** Estilos responsivos y diseño de tarjetas (`styles.css` y CDN de Bootstrap).
* **JavaScript (Vanilla):** Captura de eventos del formulario y manipulación del DOM (`script.js`).


 2. Documentación del Sistema
Implementación del Backend con Flask y Creación de API
Se implementó un servidor local utilizando el micro-framework Flask de Python. Se integró la librería flask-cors para permitir el intercambio de recursos de origen cruzado (CORS), asegurando que el Frontend (HTML) pueda comunicarse de manera segura con el servidor.

Se expuso un endpoint RESTful único:

URL: http://127.0.0.1:5000/predict

Método HTTP: POST

Función: Recibir el objeto JSON crudo desde el cliente y devolver el vector matemático transformado.

Conexión entre Frontend y Backend
La interfaz web (index.html) captura 22 variables que abarcan el perfil personal, académico, habilidades técnicas y experiencia extracurricular del estudiante (incluyendo métricas como Hackathons y Repositorios de GitHub).

Al enviar el formulario, script.js intercepta el evento, construye un payload en formato JSON y realiza una petición asíncrona (fetch) al endpoint /predict. Una vez que el Backend responde, la interfaz actualiza el DOM de forma dinámica mostrando el vector resultante sin recargar la página.
🚀 3. Instrucciones de Ejecución
Para desplegar la infraestructura de procesamiento localmente, siga estos pasos:

Prerrequisitos
Python 3.x instalado en el sistema.

Navegador web moderno.

Despliegue
Clonar el repositorio y abrir una terminal en el directorio raíz del proyecto.

Instalar dependencias del servidor:

Bash
pip install flask flask-cors
Iniciar el motor de Backend:

Bash
python app.py
El servidor indicará que está en ejecución en http://127.0.0.1:5000.
