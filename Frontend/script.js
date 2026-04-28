let ultimaPrediccion = {};

document.getElementById('predictionForm').addEventListener('submit', function(e) {
    e.preventDefault();
    realizarPrediccion();
});

function realizarPrediccion() {
    // 1. Capturar los valores que el usuario escribió en el HTML
    var cgpa = document.getElementById("cgpa").value;
    var codingScore = document.getElementById("codingScore").value;
    var internships = document.getElementById("internships").value;
    var tier = document.getElementById("collegeTier").value;
    var branch = document.getElementById("branch").value;
    var projects = document.getElementById("projects").value;
    
    // 2. Definir la ruta hacia tu backend en Python
    var endpoint = "http://127.0.0.1:5000/predict";

    // 3. Enviar los datos usando fetch
    fetch(endpoint, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            cgpa: cgpa,
            codingScore: codingScore,
            internships: internships,
            tier: tier,
            branch: branch,
            projects: projects
        })
    })
    .then(function(response) {
        return response.json();
    })
    .then(function(data) {
        // 4. Guardar el resultado en la variable global
        ultimaPrediccion = {
            cgpaIngresado: cgpa,
            estadoFinal: data.resultado_contratacion,
            salarioFinal: data.resultado_salario,
            fecha: new Date().toLocaleDateString()
        };

        // 5. Mostrar los resultados en la pantalla usando las clases de Bootstrap
        var resultSection = document.getElementById('resultSection');
        var statusEl = document.getElementById('predictionStatus');
        var salaryEl = document.getElementById('predictionSalary');

        resultSection.style.display = 'block';
        resultSection.className = 'result-section alert text-center'; 

        // Evaluamos la respuesta que nos mandó Flask (data.resultado_contratacion)
        if (data.resultado_contratacion === true) {
            resultSection.classList.add('alert-success');
            statusEl.innerText = "¡Estudiante Contratado (Placed)! 🎉";
            salaryEl.innerText = "Paquete Salarial Estimado: " + data.resultado_salario + " LPA";
        } else {
            resultSection.classList.add('alert-danger');
            statusEl.innerText = "Estudiante No Contratado (Not Placed) 😔";
            salaryEl.innerText = "Recomendamos mejorar las habilidades de programación y buscar proyectos adicionales.";
        }
    })
    .catch(function(error){
        console.log("Error en la conexión con el servidor: ", error);
        alert("Asegúrate de que el backend (app.py) esté corriendo.");
    });
}
