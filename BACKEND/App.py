from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# --- (Mantén tu función preprocesar_datos exactamente como la tenías) ---
def preprocesar_datos(datos):
    dict_tier = {'Tier 1': 1, 'Tier 2': 2, 'Tier 3': 3}
    age = int(datos.get('age', 21))
    gender = int(datos.get('gender', 1))
    cgpa = float(datos.get('cgpa', 0))
    tier_num = dict_tier.get(datos.get('tier'), 3)
    internships = int(datos.get('internships', 0))
    projects = int(datos.get('projects', 0))
    certifications = int(datos.get('certifications', 0))
    coding_score = float(datos.get('codingScore', 0))
    aptitude_score = float(datos.get('aptitudeScore', 0))
    communication_score = float(datos.get('communicationScore', 0))
    logical_score = float(datos.get('logicalScore', 0))
    hackathons = int(datos.get('hackathons', 0))
    github_repos = int(datos.get('githubRepos', 0))
    linkedin = int(datos.get('linkedin', 0))
    mock_interview = float(datos.get('mockInterview', 0))
    attendance = float(datos.get('attendance', 0))
    backlogs = int(datos.get('backlogs', 0))
    extracurricular = float(datos.get('extracurricular', 0))
    leadership = float(datos.get('leadership', 0))
    volunteer = int(datos.get('volunteer', 0))
    study_hours = int(datos.get('studyHours', 0))
    
    branch_seleccionada = datos.get('branch')

    branch_CSE = 1 if branch_seleccionada == 'CSE' else 0
    branch_Civil = 1 if branch_seleccionada == 'Civil' else 0
    branch_ECE = 1 if branch_seleccionada == 'ECE' else 0
    branch_EEE = 1 if branch_seleccionada == 'EEE' else 0
    branch_IT = 1 if branch_seleccionada == 'IT' else 0
    branch_Mechanical = 1 if branch_seleccionada == 'Mechanical' else 0

    features = [
        age, gender, cgpa, tier_num, internships, projects, certifications,
        coding_score, aptitude_score, communication_score, logical_score,
        hackathons, github_repos, linkedin, mock_interview, attendance,
        backlogs, extracurricular, leadership, volunteer, study_hours,
        branch_CSE, branch_Civil, branch_ECE, branch_EEE, branch_IT, branch_Mechanical
    ]
    return features


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # 1. Recibir los datos del frontend
        datos_entrada = request.get_json()
        
        # 2. Preprocesarlos (Convertirlos al vector numérico)
        vector_caracteristicas = preprocesar_datos(datos_entrada)

        # 3. ELIMINAMOS LA LÓGICA FALSA. 
        # AHORA SOLO CONFIRMAMOS QUE EL BACKEND RECIBIÓ Y PROCESÓ LOS DATOS.
        return jsonify({
            "status": "success",
            "mensaje": "Conexión Frontend-Backend exitosa.",
            "longitud_vector": len(vector_caracteristicas),
            "vector": vector_caracteristicas
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
