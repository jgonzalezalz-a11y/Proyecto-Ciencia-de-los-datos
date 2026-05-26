import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import joblib
import random

print("🔵 [KNN] 1. Cargando y preprocesando datos...")
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

joblib.dump(scaler, 'scaler.pkl')

print("🔵 [KNN] 2. Iniciando Monte Carlo (30 iteraciones)...")
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
mejor_knn_params = None
mejor_knn_cv = 0

for i in range(30):
    params = {
        'n_neighbors': random.choice(range(3, 25, 2)),
        'weights':     random.choice(['uniform', 'distance']),
        'metric':      random.choice(['minkowski', 'manhattan', 'chebyshev']),
        'p':           random.choice([1, 2])
    }
    modelo = KNeighborsClassifier(**params)
    cv_scores = cross_val_score(modelo, X_train_scaled, y_train, cv=cv, scoring='accuracy', n_jobs=1)
    cv_mean = cv_scores.mean()

    if cv_mean > mejor_knn_cv:
        mejor_knn_cv = cv_mean
        mejor_knn_params = params

print(f"🏆 Mejor KNN Parámetros → {mejor_knn_params}")

print("\n" + "="*60)
print("📊 ESTADÍSTICAS FINALES — KNN")
print("="*60)
knn_final = KNeighborsClassifier(**mejor_knn_params)
knn_final.fit(X_train_scaled, y_train)

y_pred_knn = knn_final.predict(X_test_scaled)
acc_knn = accuracy_score(y_test, y_pred_knn)

print(f"Accuracy en Test: {acc_knn:.4f}")
print("\nReporte de Clasificación:")
print(classification_report(y_test, y_pred_knn, target_names=['Not Placed', 'Placed']))
print("Matriz de Confusión:")
print(confusion_matrix(y_test, y_pred_knn))
print("="*60)

joblib.dump(knn_final, 'knn_model.pkl')
print("✅ ¡Archivo 'knn_model.pkl' generado con éxito!")