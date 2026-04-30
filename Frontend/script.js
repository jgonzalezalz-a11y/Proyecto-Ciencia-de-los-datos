let ultimaPrediccion = {};

document.getElementById('predictionForm').addEventListener('submit', function(e) {
    e.preventDefault();
    realizarPrediccion();
});

function realizarPrediccion() {
    // 1. Capturar TODOS los valores que el usuario escribió en el nuevo HTML
    // Perfil y Académico
    var age = document.getElementById("age").value;
    var gender = document.getElementById("gender").value;
    var tier = document.getElementById("collegeTier").value;
    var branch = document.getElementById("branch").value;
    var cgpa = document.getElementById("cgpa").value;
    var attendance = document.getElementById("attendance").value;
    var backlogs = document.getElementById("backlogs").value;
    var studyHours = document.getElementById("studyHours").value;
    
    // Habilidades
    var codingScore = document.getElementById("codingScore").value;
    var aptitudeScore = document.getElementById("aptitudeScore").value;
    var communicationScore = document.getElementById("communicationScore").value;
    var logicalScore = document.getElementById("logicalScore").value;
    var mockInterview = document.getElementById("mockInterview").value;
    
    // Experiencia y Extra
    var internships = document.getElementById("internships").value;
    var projects = document.getElementById("projects").value;
    var certifications = document.getElementById("certifications").value;
    var hackathons = document.getElementById("hackathons").value;
    var githubRepos = document.getElementById("githubRepos").value;
    var linkedin = document.getElementById("linkedin").value;
    var extracurricular = document.getElementById("extracurricular").value;
    var leadership = document.getElementById("leadership").value;
    var volunteer = document.getElementById("volunteer").value;
    
    // 2. Definir la ruta hacia tu backend en Python
    var endpoint = "http://127.0.0.1:5000/predict";

    // 3. Enviar los datos usando fetch
    fetch(endpoint, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            age: age,
            gender: gender,
            tier: tier,
            branch: branch,
            cgpa: cgpa,
            attendance: attendance,
            backlogs: backlogs,
            studyHours: studyHours,
            codingScore: codingScore,
            aptitudeScore: aptitudeScore,
            communicationScore: communicationScore,
            logicalScore: logicalScore,
            mockInterview: mockInterview,
            internships: internships,
            projects: projects,
            certifications: certifications,
            hackathons: hackathons,
            githubRepos: githubRepos,
            linkedin: linkedin,
            extracurricular: extracurricular,
            leadership: leadership,
            volunteer: volunteer
        })
    })
  .then(function(response) {
        return response.json();
    })
    .then(function(data) {
        // Mostrar los resultados en la pantalla
        var resultSection = document.getElementById('resultSection');
        var statusEl = document.getElementById('predictionStatus');
        var salaryEl = document.getElementById('predictionSalary');

        resultSection.style.display = 'block';
        
        if (data.status === "success") {
            // Un cuadro gris claro muy neutral, solo mostrando el dato técnico
            resultSection.className = 'result-section alert alert-light border text-center shadow-sm'; 
            statusEl.innerText = "Preprocesamiento completado";
            // Imprimimos el vector real que devolvió Python
            salaryEl.innerHTML = "<strong>Vector resultante listo para el modelo:</strong><br>[" + data.vector.join(", ") + "]";
        } else {
            resultSection.className = 'result-section alert alert-danger text-center shadow-sm'; 
            statusEl.innerText = "Error en el servidor";
            salaryEl.innerText = "Hubo un problema al procesar los datos.";
        }
    })
    .catch(function(error){
        console.log("Error en la conexión con el servidor: ", error);
        alert("Asegúrate de que el backend (app.py) esté corriendo en la terminal.");
    });
}
