Proyecto Ciencia de los datos:
Daniel Esteban Flórez Cobos (1000.150.507), Juan Esteban Gonzalez Alzate (1055.751.386)
# Modelo Predictivo de Empleabilidad Estudiantil basado en Variables Académicas y Laborales

# Proyecto de Análisis de Empleabilidad de Estudiantes

## Descripción del Proyecto
Este proyecto tiene como objetivo analizar los factores que influyen en la empleabilidad de estudiantes universitarios mediante técnicas de análisis de datos. A partir de un enfoque exploratorio, se busca identificar qué variables tienen mayor relación con la probabilidad de que un estudiante sea contratado, permitiendo entender mejor las dinámicas actuales del mercado laboral y la importancia de diferentes competencias en el proceso de selección.

1.
## Dataset
El conjunto de datos fue obtenido de la plataforma Kaggle y contiene 100.000 registros con 26 variables relacionadas con estudiantes universitarios. Estas variables incluyen información demográfica, académica y de desarrollo profesional, tales como edad, género, promedio académico (CGPA), número de pasantías, proyectos realizados, certificaciones, habilidades técnicas, razonamiento lógico, comunicación, entre otras. Además, se incluye una variable objetivo denominada `placement_status`, que indica si el estudiante fue colocado laboralmente o no.

## Preprocesamiento de Datos
Para garantizar la calidad y utilidad del dataset, se llevó a cabo un proceso de preprocesamiento estructurado. Inicialmente, se realizó una exploración general para identificar tipos de datos, distribución de valores y verificar la ausencia de datos nulos, lo cual permitió confirmar la integridad del conjunto de datos. Posteriormente, se eliminaron variables consideradas irrelevantes para el análisis, como identificadores únicos y variables que no aportaban valor predictivo al objetivo del estudio.

A continuación, se transformaron las variables categóricas a formato numérico, utilizando codificación binaria para variables como género, experiencia en voluntariado y estado de colocación laboral. Asimismo, se aplicó una codificación ordinal para variables con jerarquía, como el nivel de la institución educativa. Para variables categóricas con múltiples categorías, se utilizó la técnica de One-Hot Encoding, generando nuevas variables binarias que permiten representar cada categoría sin introducir sesgos de orden.

Finalmente, se realizó una conversión general de los datos a formato numérico, obteniendo un dataset completamente estructurado y adecuado para su análisis y posterior aplicación en modelos de machine learning.

## Análisis Exploratorio de Datos
En esta etapa se realizó un análisis de correlación entre las variables del dataset con el fin de identificar relaciones relevantes y posibles patrones. Se construyó una matriz de correlación que permitió evaluar la intensidad y dirección de la relación entre cada variable y la variable objetivo.

Adicionalmente, se desarrolló un ranking de variables basado en su correlación con `placement_status`, lo que permitió identificar de manera ordenada cuáles factores tienen mayor influencia en la empleabilidad. Este análisis evidenció que variables relacionadas con la experiencia práctica, como el número de pasantías y proyectos realizados, así como habilidades técnicas y desempeño en entrevistas simuladas, presentan una mayor relación con la colocación laboral.

## Resultados y Conclusiones
Los resultados obtenidos indican que la empleabilidad de los estudiantes no depende exclusivamente del rendimiento académico, sino que está fuertemente influenciada por factores relacionados con la experiencia práctica y el desarrollo de habilidades técnicas. En particular, variables como pasantías, proyectos y habilidades de programación destacan como los principales determinantes en la probabilidad de conseguir empleo.

Asimismo, se observó que habilidades cognitivas y blandas, como el razonamiento lógico y la comunicación, tienen un impacto positivo, aunque en menor medida. Por otro lado, el promedio académico presenta una relación más débil, lo que sugiere que, en el contexto analizado, las empresas valoran en mayor medida las competencias aplicadas y la experiencia real del estudiante.

## Tecnologías Utilizadas
- Python
- Pandas
- NumPy
- Seaborn
- Matplotlib

2.

## Implementación del código fuente.
## FrontEnd


## Backend


