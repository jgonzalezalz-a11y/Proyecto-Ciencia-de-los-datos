import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import joblib
import random

print("🟣 [MLP] 1. Cargando y preprocesando datos...")
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

print("🟣 [MLP] 2. Iniciando Monte Carlo (20 iteraciones)...")
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
mejor_mlp_params = None
mejor_mlp_cv = 0

arquitecturas = [(64, 32), (128, 64), (128, 64, 32), (256, 128), (64, 64, 32)]

for i in range(20):
    params = {
        'hidden_layer_sizes':  random.choice(arquitecturas),
        'activation':          random.choice(['relu', 'tanh']),
        'solver':              'adam',
        'learning_rate_init':  random.choice([0.001, 0.005]),
        'max_iter':            300,
        'random_state':        42,
        'early_stopping':      True,
        'validation_fraction': 0.1,
        'n_iter_no_change':    15,
        'batch_size':          random.choice([128, 256]),
    }
    modelo = MLPClassifier(**params)
    cv_scores = cross_val_score(modelo, X_train_scaled, y_train, cv=cv, scoring='accuracy', n_jobs=-1)
    cv_mean = cv_scores.mean()

    if cv_mean > mejor_mlp_cv:
        mejor_mlp_cv = cv_mean
        mejor_mlp_params = params

print(f"🏆 Mejor Red Neuronal Parámetros → {mejor_mlp_params}")

print("\n" + "="*60)
print("📊 ESTADÍSTICAS FINALES — RED NEURONAL (MLP)")
print("="*60)
mlp_final = MLPClassifier(**mejor_mlp_params)
mlp_final.fit(X_train_scaled, y_train)

y_pred_mlp = mlp_final.predict(X_test_scaled)
acc_mlp = accuracy_score(y_test, y_pred_mlp)

print(f"Accuracy en Test: {acc_mlp:.4f}")
print("\nReporte de Clasificación:")
print(classification_report(y_test, y_pred_mlp, target_names=['Not Placed', 'Placed']))
print("Matriz de Confusión:")
print(confusion_matrix(y_test, y_pred_mlp))
print("="*60)

joblib.dump(mlp_final, 'mlp_model.pkl')
print("✅ ¡Archivo 'mlp_model.pkl' generado con éxito!")