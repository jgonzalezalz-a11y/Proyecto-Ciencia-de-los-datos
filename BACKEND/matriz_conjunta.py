import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 1. Definir las matrices reales de tu entrenamiento
matrices = {
    "K-Nearest Neighbors (KNN)": np.array([[3266, 5842], [3477, 7415]]),
    "Red Neuronal (MLP)": np.array([[2277, 6831], [1821, 9071]]),
    "Ensamble Híbrido": np.array([[3649, 5459], [3621, 7271]])
}

labels = ['Not Placed', 'Placed']

# 2. Configurar el lienzo de Matplotlib (1 fila, 3 columnas)
fig, axes = plt.subplots(1, 3, figsize=(18, 5), sharey=False)
fig.suptitle('Comparativa Conjunta de Matrices de Confusión', fontsize=16, fontweight='bold', y=1.05)

# 3. Iterar sobre cada modelo y dibujar su mapa de calor (Heatmap)
for i, (nombre_modelo, matriz) in enumerate(matrices.items()):
    sns.heatmap(
        matriz, 
        annot=True, 
        fmt='d', 
        cmap='Blues', 
        xticklabels=labels, 
        yticklabels=labels, 
        ax=axes[i],
        cbar=False, # Quitamos la barra lateral para que se vea más limpio
        annot_kws={"size": 14, "weight": "bold"}
    )
    
    # Configurar títulos y etiquetas para cada sub-gráfico
    axes[i].set_title(nombre_modelo, fontsize=13, fontweight='bold', pad=10)
    axes[i].set_xlabel('Predicción del Modelo', fontsize=11)
    if i == 0:
        axes[i].set_ylabel('Clase Real (Data Original)', fontsize=11)

# Adjustar el espacio entre los gráficos
plt.tight_layout()

# 4. Guardar la imagen en alta definición para tu informe
plt.savefig('matriz_confusion_conjunta.png', dpi=300, bbox_inches='tight')
plt.show()
