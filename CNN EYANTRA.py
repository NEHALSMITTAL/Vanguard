import tensorflow as tf
from tensorflow import keras
from keras import layers, models
from keras.preprocessing.image import ImageDataGenerator
import os

# Set your dataset path
dataset_path = "C:\\Nehal\\HP\\Downloads\\training-20231227T151810Z-001\\training"

# Define classes
classes = ["combat", "human_aid_rehabilitation", "military_vehicles", "fire", "destroyed_buildings"]

# Image dimensions and batch size
img_width, img_height = 224, 224
batch_size = 32

# Create data generator without validation split
datagen = ImageDataGenerator(rescale=1./255)

# Load and augment training data
train_generator = datagen.flow_from_directory(
    dataset_path,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    classes=classes,
    class_mode='categorical'
)

# Build CNN model
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(img_width, img_height, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Flatten())
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(len(classes), activation='softmax'))

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit(
    train_generator,
    steps_per_epoch=train_generator.samples // batch_size,
    epochs=20
)

# Save the model
model.save('image_classification_model.h5')