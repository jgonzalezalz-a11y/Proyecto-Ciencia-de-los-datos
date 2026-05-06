from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def preprocesar_datos(datos):
    """
    Convierte el JSON del formulario en un vector numérico
    con el mismo orden del dataset final
    """

    # --- 1. EXTRAER DATOS (todos los del formulario) ---
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

    branch = datos.get('branch')

    # --- 2. ONE HOT ENCODING (branch) ---
    branch_CSE = 1 if branch == 'CSE' else 0
    branch_Civil = 1 if branch == 'Civil' else 0
    branch_ECE = 1 if branch == 'ECE' else 0
    branch_EEE = 1 if branch == 'EEE' else 0
    branch_IT = 1 if branch == 'IT' else 0
    branch_Mechanical = 1 if branch == 'Mechanical' else 0

    # --- 3. VECTOR FINAL (ORDEN CRÍTICO) ---
    features = [
        age,
        gender,
        cgpa,
        college_tier,
        internships,
        projects,
        certifications,
        coding_score,
        aptitude,
        communication,
        logical,
        hackathons,
        github,
        linkedin,
        mock,
        attendance,
        backlogs,
        extracurricular,
        leadership,
        volunteer,
        study_hours,
        branch_CSE,
        branch_Civil,
        branch_ECE,
        branch_EEE,
        branch_IT,
        branch_Mechanical
    ]

    return features


@app.route('/predict', methods=['POST'])
def predict():
    try:
        datos = request.get_json()

        # Procesar datos
        vector = preprocesar_datos(datos)

        # --- MODELO SIMULADO (lógica simple) ---
        contratado = False
        if vector[2] > 7 and vector[7] > 65 and vector[8] > 50:
            contratado = True

        salario = 0
        if contratado:
            salario = (
                vector[2] * 1.5 +     # CGPA
                vector[4] * 0.7 +     # Internships
                vector[7] * 0.08 +    # Coding
                vector[13] * 0.002    # LinkedIn
            )

        return jsonify({
            "status": "success",
            "resultado_contratacion": contratado,
            "resultado_salario": round(salario, 2)
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400


if __name__ == '__main__':
    app.run(debug=True, port=5000)
