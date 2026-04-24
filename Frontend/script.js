document.getElementById('predictionForm').addEventListener('submit', function(e) {
    e.preventDefault();

    
    const cgpa = parseFloat(document.getElementById('cgpa').value);
    const codingScore = parseFloat(document.getElementById('codingScore').value);
    const internships = parseInt(document.getElementById('internships').value);
    const tier = document.getElementById('collegeTier').value;

   
    const resultSection = document.getElementById('resultSection');
    const statusEl = document.getElementById('predictionStatus');
    const salaryEl = document.getElementById('predictionSalary');

    
    let isPlaced = false;
    let estimatedSalary = 0;

    if (cgpa >= 7.5 && codingScore >= 70 && internships >= 1) {
        isPlaced = true;
    
        estimatedSalary = (cgpa * 0.8) + (codingScore * 0.05) + (internships * 1.5);
        if (tier === 'Tier 1') estimatedSalary += 3.0;
    }

    resultSection.style.display = 'block';
    resultSection.className = 'result-section alert text-center'; // Reset de clases de Bootstrap

    if (isPlaced) {
    
        resultSection.classList.add('alert-success');
        statusEl.innerText = "¡Estudiante Contratado (Placed)! 🎉";
        salaryEl.innerText = `Paquete Salarial Estimado: ${estimatedSalary.toFixed(2)} LPA`;
    } else {
        
        resultSection.classList.add('alert-danger');
        statusEl.innerText = "Estudiante No Contratado (Not Placed) 😔";
        salaryEl.innerText = "Recomendamos mejorar las habilidades de programación y buscar proyectos adicionales.";
    }
});