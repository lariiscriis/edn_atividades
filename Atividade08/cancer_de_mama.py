# Calcular e comparar diferentes métricas de classificação (Precisão, Recall, F1-Score, AUC-ROC) 
# usando um modelo de aprendizado de máquina em Python.

from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score
from sklearn.model_selection import train_test_split

#Carregando os dados 

data = load_breast_cancer()

#Dividir os dados em conjuntos de treino e teste
x_train, x_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.3, random_state = 42)


#Criar e treinar o modelo
model = RandomForestClassifier()
model.fit(x_train,y_train)

#Prever com base nos dados de teste se o exame vai ser maligno ou benigno 
y_pred= model.predict(x_test)

y_pred_proba = model.predict_proba(x_test)[:,1]

#Avaliar o modelo 
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1score = f1_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_pred_proba)

#Exibir dados
print(f'Precisão: {precision:.2f}')
print(f'Recall: {recall:.2f}')
print(f'F1-Score: {f1score:.2f}')
print(f'AUC-ROC: {roc_auc:.2f}')

