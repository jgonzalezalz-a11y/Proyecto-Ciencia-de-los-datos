let ultimaPrediccion = {};

document.getElementById('predictionForm').addEventListener('submit', function(e) {
    e.preventDefault();
    realizarPrediccion();
});

function realizarPrediccion() {

    // 🔹 Capturar TODOS los campos incluyendo el método de machine learning seleccionado
    const data = {
        method: document.getElementById("method").value, // Envía 'ensemble', 'mlp' o 'knn'
        age: document.getElementById("age").value,
        gender: document.getElementById("gender").value,
        cgpa: document.getElementById("cgpa").value,
        college_tier: document.getElementById("college_tier").value,
        branch: document.getElementById("branch").value,
        internships_count: document.getElementById("internships_count").value,
        projects_count: document.getElementById("projects_count").value,
        certifications_count: document.getElementById("certifications_count").value,
        coding_skill_score: document.getElementById("coding_skill_score").value,
        aptitude_score: document.getElementById("aptitude_score").value,
        communication_skill_score: document.getElementById("communication_skill_score").value,
        logical_reasoning_score: document.getElementById("logical_reasoning_score").value,
        hackathons_participated: document.getElementById("hackathons_participated").value,
        github_repos: document.getElementById("github_repos").value,
        linkedin_connections: document.getElementById("linkedin_connections").value,
        mock_interview_score: document.getElementById("mock_interview_score").value,
        attendance_percentage: document.getElementById("attendance_percentage").value,
        backlogs: document.getElementById("backlogs").value,
        extracurricular_score: document.getElementById("extracurricular_score").value,
        leadership_score: document.getElementById("leadership_score").value,
        volunteer_experience: document.getElementById("volunteer_experience").value,
        study_hours_per_day: document.getElementById("study_hours_per_day").value
    };

    const endpoint = "http://127.0.0.1:5000/predict";

    fetch(endpoint, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(res => {
        if (!res.ok) {
            return res.json().then(err => { throw new Error(err.message); });
        }
        return res.json();
    })
    .then(data => {

        // Almacenar en caché local la última inferencia por si se requiere auditar
        ultimaPrediccion = {
            methodUsed: data.modelo_utilizado,
            estadoFinal: data.resultado_contratacion,
            fecha: new Date().toLocaleDateString()
        };

        const resultSection = document.getElementById('resultSection');
        const statusEl = document.getElementById('predictionStatus');
        const salaryEl = document.getElementById('predictionSalary');
        const modelBadgeEl = document.getElementById('usedModelBadge');

        // Resetear clases de Bootstrap previas para evitar acumulación de colores
        resultSection.className = 'result-section alert text-center shadow-sm';
        resultSection.style.display = 'block';

        // Aseguramos que la etiqueta secundaria de salario/sugerencias esté completamente vacía siempre
        if (salaryEl) {
            salaryEl.innerText = ""; 
        }

        if (data.resultado_contratacion === true) {
            resultSection.classList.add('alert-success');
            statusEl.innerText = "¡Estudiante Contratado (Placed)! 🎉";
        } else {
            resultSection.classList.add('alert-danger');
            statusEl.innerText = "No Contratado (Not Placed) 😔";
        }

        // Inyectar visualmente el modelo que computó el resultado en el servidor
        if (modelBadgeEl && data.modelo_utilizado) {
            modelBadgeEl.innerText = "⚙️ Motor de cálculo activo: " + data.modelo_utilizado;
        }
    })
    .catch(error => {
        console.error("Error operacional del Pipeline:", error);
        alert("⚠️ Error en el sistema predictivo: " + error.message);
    });
}
