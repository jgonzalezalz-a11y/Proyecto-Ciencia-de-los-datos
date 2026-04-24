# 🎓 Modelo Predictivo de Empleabilidad Estudiantil basado en Variables Académicas y Laborales

Este repositorio contiene la implementación inicial (Frontend) de un sistema web diseñado para estimar el estado de contratación (empleabilidad) y el paquete salarial de estudiantes universitarios, basado en su perfil académico y habilidades.


 📋 Resumen del Proyecto y Requerimientos

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

### 4. Formulario y Lógica de Predicción (Desacoplada)
Actualmente, el frontend cuenta con un formulario que captura las variables más relevantes. 

## 🛠️ Estructura de Archivos

```text
/
├── index.html   # Estructura principal de la página y formulario.
├── styles.css   # Estilos personalizados (complementarios a Bootstrap).
└── script.js    # Lógica de simulación de predicción y manejo del DOM.
