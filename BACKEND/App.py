from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
import os

app = Flask(__name__)
CORS(app)

# ── 1. CONFIGURACIÓN DE ARCHIVOS BINARIOS (.PKL) ─────────────────────────────
# Definimos los nombres de los archivos que deben estar en la misma carpeta raíz
SCALER_PATH = 'scaler.pkl'
KNN_PATH = 'knn_model.pkl'
MLP_PATH = 'mlp_model (1).pkl'  # Mantiene el nombre exacto con el espacio y paréntesis
ENSEMBLE_PATH = 'ensemble_model.pkl'

# Diccionario global para almacenar los modelos precargados
modelos_db = {}
scaler = None

print("📦 Cargando tuberías de Machine Learning en memoria RAM...")

try:
    # Carga obligatoria del escalador para normalizar los datos
    if os.path.exists(SCALER_PATH):
        scaler = joblib.load(SCALER_PATH)
        print("✅ Escalador estadístico (scaler.pkl) acoplado con éxito.")
    else:
        print(f"❌ ERROR CRÍTICO: No se halló el archivo '{SCALER_PATH}' en esta carpeta.")

    # Carga de algoritmos optimizados previamente en tu Colab
    if os.path.exists(KNN_PATH):
        modelos_db['knn'] = joblib.load(KNN_PATH)
        print("✅ Clasificador K-Neighbors (KNN) cargado.")
        
    if os.path.exists(MLP_PATH):
        modelos_db['mlp'] = joblib.load(MLP_PATH)
        print("✅ Clasificador Red Neuronal (MLP) cargado.")
        
    if os.path.exists(ENSEMBLE_PATH):
        modelos_db['ensemble'] = joblib.load(ENSEMBLE_PATH)
        print("✅ Clasificador Híbrido Votante (Ensemble) cargado.")

except Exception as e:
    print(f"⚠️ Error sistémico en la inicialización de los archivos binarios: {str(e)}")


# ── 2. PROCESAMIENTO VECTORIAL DE ENTRADAS (27 VARIABLES) ────────────────────
def preprocesar_datos(datos):
    """
    Formatea los campos del JSON entrante garantizando el tipo de dato correcto
    y manteniendo el orden estricto de las 27 dimensiones requeridas por los modelos.
    """
    age = int(datos.get('age', 21))
    gender = int(datos.get('gender', 1))
    cgpa = float(datos.get('cgpa', 0))
    college_tier = int(datos.get('college_tier', 3))
    internships = int(datos.get('internships_count', 0))
    projects = int(datos.get('projects_count', 0))
    certifications = int(datos.get('certifications_count', 0))
    coding_score = float(datos.get('coding_skill_score', 0))
    aptitude = float(datos.get('aptitude_score', 0))
    communication = float(datos.get('communication_skill_score', 0))
    logical = float(datos.get('logical_reasoning_score', 0))
    hackathons = int(datos.get('hackathons_participated', 0))
    github = int(datos.get('github_repos', 0))
    linkedin = int(datos.get('linkedin_connections', 0))
    mock = float(datos.get('mock_interview_score', 0))
    attendance = float(datos.get('attendance_percentage', 0))
    backlogs = int(datos.get('backlogs', 0))
    extracurricular = float(datos.get('extracurricular_score', 0))
    leadership = float(datos.get('leadership_score', 0))
    volunteer = int(datos.get('volunteer_experience', 0))
    study_hours = float(datos.get('study_hours_per_day', 0))

    branch = datos.get('branch', '')

    # Mapeo manual síncrono equivalente a pd.get_dummies() realizado en el dataset
    branch_CSE = 1 if branch == 'CSE' else 0
    branch_Civil = 1 if branch == 'Civil' else 0
    branch_ECE = 1 if branch == 'ECE' else 0
    branch_EEE = 1 if branch == 'EEE' else 0
    branch_IT = 1 if branch == 'IT' else 0
    branch_Mechanical = 1 if branch == 'Mechanical' else 0

    features = [
        age, gender, cgpa, college_tier,
        internships, projects, certifications,
        coding_score, aptitude, communication,
        logical, hackathons, github,
        linkedin, mock, attendance,
        backlogs, extracurricular, leadership,
        volunteer, study_hours,
        branch_CSE, branch_Civil, branch_ECE,
        branch_EEE, branch_IT, branch_Mechanical
    ]
    return features


# ── 3. PUNTO DE ACCESO PARA INFERENCIA DINÁMICA ───────────────────────────────
@app.route('/predict', methods=['POST'])
def predict():
    try:
        datos = request.get_json()
        
        # Extraer el método seleccionado por el usuario en el frontend (Por defecto Ensemble)
        metodo_solicitado = datos.get('method', 'ensemble').lower()
        
        # Validar que tanto el modelo elegido como el escalador existan operacionalmente
        if metodo_solicitado not in modelos_db or scaler is None:
            return jsonify({
                "status": "error",
                "message": f"El método computacional '{metodo_solicitado}' o el escalador no se encuentran inicializados en el servidor."
            }), 500
            
        # Seleccionar el clasificador activo dinámicamente
        modelo_activo = modelos_db[metodo_solicitado]
        
        # Construir matriz bidimensional (1, 27) y normalizar con el StandardScaler real
        vector_nativo = preprocesar_datos(datos)
        vector_array = np.array([vector_nativo])
        vector_escalado = scaler.transform(vector_array)
        
        # Inferencia real ejecutada por el modelo matemático elegido
        prediccion_clase = modelo_activo.predict(vector_escalado)[0]
        contratado = bool(prediccion_clase == 1)

        # Regla de negocio matemática para el cálculo del paquete salarial estimado (LPA)
        salario = 0.0
        if contratado:
            salario = (
                vector_nativo[2] * 1.5 +     # Coeficiente CGPA
                vector_nativo[4] * 0.7 +     # Coeficiente de Internships
                vector_nativo[7] * 0.08 +    # Coeficiente de Coding skill
                vector_nativo[13] * 0.002    # Coeficiente de LinkedIn
            )

        # Retorno HTTP estructurado hacia JavaScript
        return jsonify({
            "status": "success",
            "modelo_utilizado": metodo_solicitado.upper(),
            "resultado_contratacion": contratado,
            "resultado_salario": round(salario, 2)
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Fallo en la inferencia del pipeline: {str(e)}"
        }), 400


if __name__ == '__main__':
    # Inicialización local en el puerto estándar 5000
    app.run(debug=True, port=5000)
