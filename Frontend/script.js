let ultimaPrediccion = {};

document.getElementById('predictionForm').addEventListener('submit', function(e) {
    e.preventDefault();
    realizarPrediccion();
});

function realizarPrediccion() {

    // 🔹 Capturar TODOS los campos (usando los IDs correctos)
    const data = {
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
    .then(res => res.json())
    .then(data => {

        ultimaPrediccion = {
            estadoFinal: data.resultado_contratacion,
            salarioFinal: data.resultado_salario,
            fecha: new Date().toLocaleDateString()
        };

        const resultSection = document.getElementById('resultSection');
        const statusEl = document.getElementById('predictionStatus');
        const salaryEl = document.getElementById('predictionSalary');

        resultSection.style.display = 'block';
        resultSection.className = 'result-section alert text-center';

        if (data.resultado_contratacion === true) {
            resultSection.classList.add('alert-success');
            statusEl.innerText = "¡Estudiante Contratado (Placed)! 🎉";
            salaryEl.innerText = "Salario estimado: " + data.resultado_salario;
        } else {
            resultSection.classList.add('alert-danger');
            statusEl.innerText = "No contratado 😔";
            salaryEl.innerText = "Mejora habilidades técnicas y experiencia.";
        }
    })
    .catch(error => {
        console.error("Error:", error);
        alert("El backend no está corriendo.");
    });
}
