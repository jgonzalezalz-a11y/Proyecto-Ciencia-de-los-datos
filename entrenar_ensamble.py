import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import joblib

print("⚙️ [Ensemble] 1. Cargando datos y configurando ensamble...")
df = pd.read_csv('DataSetProyecto.csv')
df = df.drop(['student_id', 'salary_package_lpa', 'sleep_hours'], axis=1)

df['volunteer_experience'] = df['volunteer_experience'].map({'Yes': 1, 'No': 0})
df['gender']               = df['gender'].map({'Male': 1, 'Female': 0})
df['placement_status']     = df['placement_status'].map({'Placed': 1, 'Not Placed': 0})
df['college_tier']         = df['college_tier'].map({'Tier 1': 1, 'Tier 2': 2, 'Tier 3': 3})

df = pd.get_dummies(df, columns=['branch'])
branch_cols = ['branch_CSE', 'branch_Civil', 'branch_ECE', 'branch_EEE', 'branch_IT', 'branch_Mechanical']
for col in branch_cols:
    df[col] = df[col].astype(int) if col in df.columns else 0

FEATURE_COLS = [
    'age', 'gender', 'cgpa', 'college_tier', 'internships_count', 'projects_count', 
    'certifications_count', 'coding_skill_score', 'aptitude_score', 'communication_skill_score',
    'logical_reasoning_score', 'hackathons_participated', 'github_repos', 'linkedin_connections',
    'mock_interview_score', 'attendance_percentage', 'backlogs', 'extracurricular_score',
    'leadership_score', 'volunteer_experience', 'study_hours_per_day',
    'branch_CSE', 'branch_Civil', 'branch_ECE', 'branch_EEE', 'branch_IT', 'branch_Mechanical'
]

X = df[FEATURE_COLS]
y = df['placement_status']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled  = scaler.transform(X_test)

# Configuraciones óptimas basadas en las ejecuciones previas
knn_sub = KNeighborsClassifier(n_neighbors=9, weights='distance', metric='manhattan')
mlp_sub = MLPClassifier(hidden_layer_sizes=(128, 64), activation='relu', max_iter=300, random_state=42, early_stopping=True)

ensemble_final = VotingClassifier(
    estimators=[('knn', knn_sub), ('mlp', mlp_sub)],
    voting='soft'
)

print("⚙️ [Ensemble] 2. Entrenando el modelo de votación híbrido...")
ensemble_final.fit(X_train_scaled, y_train)

print("\n" + "="*60)
print("📊 ESTADÍSTICAS FINALES — ENSEMBLE HÍBRIDO")
print("="*60)
y_pred_ens = ensemble_final.predict(X_test_scaled)
acc_ens = accuracy_score(y_test, y_pred_ens)

print(f"Accuracy en Test: {acc_ens:.4f}")
print("\nReporte de Clasificación:")
print(classification_report(y_test, y_pred_ens, target_names=['Not Placed', 'Placed']))
print("Matriz de Confusión:")
print(confusion_matrix(y_test, y_pred_ens))
print("="*60)

joblib.dump(ensemble_final, 'ensemble_model.pkl')
print("✅ ¡Archivo 'ensemble_model.pkl' generado con éxito!")