import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense

# Carga de datos
data = pd.read_csv("ejercicio 4\data_customer_classification 1.xlsx")

# Preprocesamiento

# Codificación del ID de cliente
le = LabelEncoder()
data["customer_id"] = le.fit_transform(data["customer_id"])

# Cálculo de características nuevas
data["trans_frequency"] = data.groupby("customer_id")["trans_date"].transform("size")
data["avg_spending"] = data["tran_amount"].groupby(data["customer_id"]).transform("sum") / data["trans_frequency"]
data["max_spending"] = data["tran_amount"].groupby(data["customer_id"]).transform("max")

# Eliminación de la columna ID
del data["customer_id"]

# Escalado de datos
scaler = MinMaxScaler()
data_num = data[["trans_frequency", "avg_spending", "max_spending"]]
data_num = scaler.fit_transform(data_num)
data[["trans_frequency", "avg_spending", "max_spending"]] = data_num

# División del dataset
X_train, X_test, y_train, y_test = train_test_split(data, data["customer_category"], test_size=0.3, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_test, y_test, test_size=0.5, random_state=42)

# Creación del modelo
model = Sequential()
model.add(Dense(128, activation="relu", input_shape=(3,)))  # 3 características
model.add(Dense(64, activation="relu"))
model.add(Dense(3, activation="softmax"))  # 3 categorías de clientes

# Compilación del modelo
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

# Entrenamiento del modelo
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_val, y_val))

# Evaluación del modelo
loss, accuracy = model.evaluate(X_test, y_test)
print("Test accuracy:", accuracy)

# Guardado del modelo
model.save("customer_model")