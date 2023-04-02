# 1. Importa las bibliotecas necesarias: Numpy, Pandas, Matplotlib, Scikit-learn y TensorFlow.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
from tensorflow import keras
from sklearn.metrics import confusion_matrix

# Carga los datos
iris_data = pd.read_csv('flores/iris.csv', header=None, names=[
                        'sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'], delimiter=',')

# Reemplazar los valores de cadena con números
iris_data['species'].replace(
    ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'], [0, 1, 2], inplace=True)

# Convertir la columna "species" en una columna de números enteros
iris_data['species'] = iris_data['species'].astype(int)

# Separa las características y las etiquetas
X = iris_data.drop('species', axis=1).values
y = iris_data['species'].values


# Divide los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Normaliza los datos de entrada
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# Crea el modelo de red neuronal
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(16, activation='relu', input_shape=(4,)),
    tf.keras.layers.Dense(3, activation='softmax')
])

# Compila el modelo
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Entrena el modelo
model.fit(X_train, y_train, epochs=50, batch_size=8, verbose=1)

y_pred = model.predict(X_test)
y_pred = np.argmax(y_pred, axis=1)
confusion_matrix(y_test, y_pred)

new_flowers = [
    [5.1, 3.5, 1.4, 0.2],  # Características de la primera flor
    [7.7, 3.0, 6.1, 2.3],  # Características de la segunda flor
    [6.3, 2.9, 5.6, 1.8]   # Características de la tercera flor
]
# Convertir la lista de listas en un array de NumPy
new_flowers = np.array(new_flowers)

# Normalizar los datos de entrada de las nuevas flores
new_flowers = scaler.transform(new_flowers)

# Realizar la predicción de las clases de las nuevas flores
y_pred = model.predict(new_flowers)

# Obtener la clase predicha para cada flor
predicted_classes = np.argmax(y_pred, axis=1)


# Define el mapeo de clases
class_mapping = {
    0: 'Iris-setosa',
    1: 'Iris-versicolor',
    2: 'Iris-virginica'
}

# Crea una lista de nombres de clase en base al mapeo
class_names = [class_mapping[label] for label in range(len(class_mapping))]

# Convertir las clases numéricas en nombres de clase
predicted_class_names = [class_names[i] for i in predicted_classes]

# Imprimir los nombres de clase predichos para las nuevas flores
print("Las nuevas flores son:", predicted_class_names)
