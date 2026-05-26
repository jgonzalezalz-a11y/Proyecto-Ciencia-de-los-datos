# Proyecto Ciencia de los datos: Modelo predictivo de empleabilidad estudiantil basado en variables académicas y laborales
Daniel Esteban Flórez Cobos (1000.150.507), Juan Esteban Gonzalez Alzate (1055.751.386)

## Descripción del Proyecto
Este proyecto tiene como objetivo analizar los factores que influyen en la empleabilidad de estudiantes universitarios mediante técnicas de análisis de datos. A partir de un enfoque exploratorio, se busca identificar qué variables tienen mayor relación con la probabilidad de que un estudiante sea contratado, permitiendo entender mejor las dinámicas actuales del mercado laboral y la importancia de diferentes competencias en el proceso de selección.
## Requisitos del sistema Antes de ejecutar el proyecto, se debe tener instalado:
Python (Versión 3.10 o superior). Verifica con: python --version
Pip (Gestor de paquetes de Python). Verifica con: pip --version
Un navegador web moderno (Google Chrome, Mozilla Firefox, Microsoft Edge, etc.).
##Pasos para la ejecucón
Si deseas descargar el proyecto completo desde el repositorio de GitHub y ejecutarlo en Visual Studio Code, sigue estos pasos estructurados:

### 1. Preparación de la Carpeta Raíz
Para mantener una estructura limpia y asegurar la correcta comunicación relativa entre los componentes, se recomienda consolidar todo dentro de un directorio principal:
1. Crea una carpeta vacía en tu ordenador y nómbrala **`matriz`**.
2. Abre **Visual Studio Code**.
3. Ve a `Archivo` > `Abrir carpeta...` (File > Open Folder...) y selecciona la carpeta **`matriz`** que acabas de crear.

### 2. Clonación del Repositorio
1. Abre una terminal integrada en Visual Studio Code (`Ctrl + Ñ` o `Terminal` > `Nueva Terminal`).
2. Clona el repositorio de GitHub directamente dentro de tu carpeta activa ejecutando:
   ```bash
   git clone <URL_DE_TU_REPOSITORIO_GITHUB> .

   Paso a paso:

Instalación de dependencias
En la carpeta raíz del proyecto (matriz), abrir una terminal y ejecutar:

Bash
pip install flask flask-cors pandas numpy scikit-learn joblib
Esto instala todas las librerías necesarias para procesar los datos, levantar el servidor y ejecutar los modelos de Inteligencia Artificial.

Ejecución del backend
Abrir una terminal en Visual Studio Code y ubicarse en la carpeta:

Bash
cd BACKEND
Ejecutar el servidor de Flask:

Bash
python app.py
Cuando aparezca el mensaje en la consola:

Plaintext
* Running on http://127.0.0.1:5000
el backend ya estará funcionando correctamente y listo para recibir datos.

Ejecución del frontend
El frontend funciona simplemente abriendo el archivo de la interfaz gráfica:

Plaintext
FRONTEND/index.html
Pasos:

Abrir la carpeta FRONTEND/ en el explorador de archivos.

Hacer doble clic en el archivo index.html (la interfaz se abrirá automáticamente en tu navegador web).

Ingresar los datos del estudiante (CGPA, carrera, pasantías, conexiones de LinkedIn, etc.).

Seleccionar el modelo de predicción que deseas evaluar (KNN, MLP o Ensamble).

Presionar el botón Predecir Empleabilidad.

Nota: Para que la comunicación sea exitosa, la terminal del backend con Flask debe mantenerse corriendo en todo momento.

Cómo funciona la comunicación
El frontend emite una solicitud HTTP asíncrona enviando los datos del perfil del alumno en un paquete JSON hacia el backend. El backend recibe la información, la transforma a través del escalador estadístico, ejecuta la predicción con el modelo de Machine Learning seleccionado y calcula el salario estimado. Finalmente, el backend retorna la respuesta y el frontend actualiza la pantalla de inmediato mostrando el veredicto de contratación y el sueldo calculado.
1. # Preprocesamiento de Datos
   1. ## Dataset:
      El conjunto de datos fue obtenido de la plataforma Kaggle y contiene 100.000 registros con 26 variables relacionadas con estudiantes universitarios. Estas variables incluyen información demográfica, académica y de desarrollo profesional, tales como edad, género, promedio académico (CGPA), número de pasantías, proyectos realizados, certificaciones, habilidades técnicas, razonamiento lógico, comunicación, entre otras. Además, se incluye una variable objetivo denominada `placement_status`, que indica si el estudiante fue colocado laboralmente o no.

      Para garantizar la calidad y utilidad del dataset, se llevó a cabo un proceso de preprocesamiento estructurado. Inicialmente, se realizó una exploración general para identificar tipos de datos, distribución de valores y verificar la ausencia de datos nulos, lo cual permitió confirmar la integridad del conjunto de datos. Posteriormente, se eliminaron variables consideradas irrelevantes para el análisis, como identificadores únicos y variables que no aportaban valor predictivo al objetivo del estudio.
      

      A continuación, se transformaron las variables categóricas a formato numérico, utilizando codificación binaria para variables como género, experiencia en voluntariado y estado de colocación laboral. Asimismo, se aplicó una codificación ordinal para variables con jerarquía, como el nivel de la institución educativa. Para variables categóricas con múltiples categorías, se utilizó la técnica de One-Hot Encoding, generando nuevas variables binarias que permiten representar cada categoría sin introducir sesgos de orden.

      Finalmente, se realizó una conversión general de los datos a formato numérico, obteniendo un dataset completamente estructurado y adecuado para su análisis y posterior aplicación en modelos de machine learning.
      
2. # Implementación del código fuente.
   1. ## FrontEnd
      Una interfaz web responsiva y limpia construida con tecnologías nativas que permite al usuario interactuar directamente con la Inteligencia Artificial. Recopila variables académicas, técnicas y extracurriculares:
* **Datos Académicos:** Promedio de calificaciones (`CGPA`), Carrera (*Stream*), Experiencia previa en pasantías (*Internships*).
* **Habilidades Técnicas:** Dominio de lenguajes de programación, proyectos académicos realizados.
* **Métricas Sociales/Extracurriculares:** Conexiones en LinkedIn, participación en actividades de voluntariado, histórico de asistencia a clases.
* **Modelo Preferido:** Selector dinámico del algoritmo de inferencia (KNN, MLP o Ensamble).
   2. ## BackEnd
(API REST en Flask)
Recibir los datos desde el frontend Procesarlos Seleccionar el modelo solicitado Retornar la predicción generada El backend contiene: Código de la API (app.py) Modelos entrenados (.pkl) Escaladores y columnas del One-Hot Encoding Archivos de datos (.csv y .json)
* **Ingeniería de Características:** Transforma las solicitudes asíncronas en un vector ordenado de 27 dimensiones mediante *One-Hot Encoding*.
* **Estandarización:** Normaliza las magnitudes numéricas en tiempo real a través de un transformador estadístico (`scaler.pkl`).
  3. ## Estructura
  Plaintext
matriz/
│
├── BACKEND/
│   ├── data/
│   │   └── student_placement.csv
│   │
│   ├── app.py
│   ├── entrenar_ensamble.py
│   ├── knn_model.pkl
│   ├── mlp_model.pkl
│   ├── ensemble_model.pkl
│   ├── scaler.pkl
│   └── ohe_columns.pkl
│
└── FRONTEND/
    ├── index.html
    ├── script.js
    └── styles.css

   3. ## Análisis Exploratorio de Datos
      En esta etapa se realizó un análisis de correlación entre las variables del dataset con el fin de identificar relaciones relevantes y posibles patrones. Se construyó una matriz de correlación que permitió evaluar la intensidad y dirección de la relación entre cada variable y la variable objetivo.

      Adicionalmente, se desarrolló un ranking de variables basado en su correlación con `placement_status`, lo que permitió identificar de manera ordenada cuáles factores tienen mayor influencia en la empleabilidad. Este análisis evidenció que variables relacionadas con la experiencia práctica, como el número de pasantías y proyectos realizados, así como habilidades técnicas y desempeño en entrevistas simuladas, presentan una mayor relación con la colocación laboral.

   4. ## Tecnologías Utilizadas
         - Python
         - Pandas
         - NumPy
         - Seaborn
         - Matplotlib

   5. ## Resultados y Conclusiones
      Los resultados obtenidos indican que la empleabilidad de los estudiantes no depende exclusivamente del rendimiento académico, sino que está fuertemente influenciada por factores relacionados con la experiencia práctica y el desarrollo de habilidades técnicas. En particular, variables como pasantías, proyectos y habilidades de programación destacan como los principales determinantes en la probabilidad de conseguir empleo.

      Asimismo, se observó que habilidades cognitivas y blandas, como el razonamiento lógico y la comunicación, tienen un impacto positivo, aunque en menor medida. Por otro lado, el promedio académico presenta una relación más débil, lo que sugiere que, en el contexto analizado, las empresas valoran en mayor medida las competencias aplicadas y la experiencia real del estudiante.







