from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite la comunicación con el frontend

def preprocesar_datos(datos):
    """
    Esta función convierte el JSON del formulario en una lista de 
    números procesada.
    """
    # 1. Mapeos manuales
    dict_tier = {'Tier 1': 1, 'Tier 2': 2, 'Tier 3': 3}
    # (Asumimos valores por defecto para campos que no están en el formulario básico)
    
    # 2. Extraer valores del JSON
    cgpa = float(datos.get('cgpa', 0))
    coding_score = float(datos.get('codingScore', 0))
    internships = int(datos.get('internships', 0))
    projects = int(datos.get('projects', 0))
    tier_num = dict_tier.get(datos.get('tier'), 3)
    branch_seleccionada = datos.get('branch')

    # 3. One-Hot Encoding manual para 'branch' (Las 6 columnas de especialidad)
    # Inicializamos todas en 0
    branch_CSE = 1 if branch_seleccionada == 'CSE' else 0
    branch_Civil = 1 if branch_seleccionada == 'Civil' else 0
    branch_ECE = 1 if branch_seleccionada == 'ECE' else 0
    branch_EEE = 1 if branch_seleccionada == 'EEE' else 0
    branch_IT = 1 if branch_seleccionada == 'IT' else 0
    branch_Mechanical = 1 if branch_seleccionada == 'Mechanical' else 0

    # 4. Crear el vector de características (Feature Vector)
    # NOTA: Valores 'quemados' (0 o promedios) para las variables 
    # que están en el dataset pero no en el formulario actual (como age, aptitude_score, etc.)
    # El orden debe ser IDENTICO al de de df.columns
    features = [
        21,          # age (promedio)
        1,           # gender (1=Male, 0=Female)
        cgpa,        # cgpa
        tier_num,    # college_tier
        internships, # internships_count
        projects,    # projects_count
        2,           # certifications_count (default)
        coding_score,# coding_skill_score
        70,          # aptitude_score (default)
        70,          # communication_skill_score (default)
        70,          # logical_reasoning_score (default)
        1,           # hackathons_participated (default)
        4,           # github_repos (default)
        500,         # linkedin_connections (default)
        coding_score,# mock_interview_score (usamos coding_score como proxy)
        85,          # attendance_percentage (default)
        0,           # backlogs
        60,          # extracurricular_score
        55,          # leadership_score
        1,           # volunteer_experience
        4,           # study_hours_per_day
        # Las 6 columnas de branch (dummies)
        branch_CSE, branch_Civil, branch_ECE, branch_EEE, branch_IT, branch_Mechanical
    ]
    
    return features

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # A. Recibir datos
        datos_recibidos = request.get_json()
        
        # B. Preprocesar (Transformar a números)
        vector_final = preprocesar_datos(datos_recibidos)
        
        # C. Lógica de Predicción (Simulada para esta entrega)
        # En la Entrega 3, aquí se usará: modelo.predict([vector_final])
        es_contratado = False
        if vector_final[2] > 7.0 and vector_final[7] > 65: # Si CGPA > 7 y Coding > 65
            es_contratado = True
        
        salario_estimado = 0
        if es_contratado:
            # Fórmula basada en los hallazgos de correlación
            salario_estimado = (vector_final[2] * 1.2) + (vector_final[4] * 0.5) + (vector_final[7] * 0.05)

        # D. Respuesta
        return jsonify({
            "status": "success",
            "resultado_contratacion": es_contratado,
            "resultado_salario": round(salario_estimado, 2),
            "vector_procesado": vector_final # Útil para depurar
        })

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)