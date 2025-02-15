import keras
from keras import layers
from sklearn.model_selection import train_test_split
import numpy as np

PACKET_SIZE = 10  # Количество временных шагов в окне
SENSORS = 8       # Количество входных признаков (5 данных с датчиков изгиба на пальцах + 3 данных с акселерометра)


# Создание модели CNN
model = keras.Sequential([
    layers.Conv1D(32, kernel_size=3, activation='relu', input_shape=(PACKET_SIZE, SENSORS)),
    layers.MaxPooling1D(2),
    layers.Conv1D(64, kernel_size=3, activation='relu'),
    layers.GlobalAveragePooling1D(),
    layers.Dense(33, activation='softmax')  # 33 класса (33 буквы)
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])


### ПРИМЕР ОБУЧЕНИЯ МОДЕЛИ ###


# Генерация случайных данных (10 000 записей, 8 сенсоров)
data = np.random.randint(0, 99, size=(10000, SENSORS))

# Метки классов от 0 до 32 (всего 33 класса, 33 буквы)
labels = np.random.randint(0, 32, size=(10000,))

X, y = [], []

for i in range(len(data) - PACKET_SIZE):
    X.append(data[i:i+PACKET_SIZE])
    y.append(labels[i+PACKET_SIZE])

X, y = np.array(X), np.array(y)

print(f"Форма X: {X.shape}, Форма y: {y.shape}")

# Разделение на train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Обучение модели
model.fit(X_train, y_train, epochs=20, batch_size=32, validation_data=(X_test, y_test))
