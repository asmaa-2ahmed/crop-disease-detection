from src.config import NUM_CLASSES, BATCH_SIZE, TRAIN_DIR, MODEL_WEIGHTS_PATH
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.applications import Xception
from tensorflow.keras import layers
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from PIL import Image
import streamlit as st

# Load and preprocess the data
def load_and_preprocess_data():
    train_datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)

    train_generator = train_datagen.flow_from_directory(
        TRAIN_DIR,
        target_size=(299, 299),
        batch_size=BATCH_SIZE,
        class_mode='categorical',
        subset='training',
    )

    validation_generator = train_datagen.flow_from_directory(
        TRAIN_DIR,
        target_size=(299, 299),
        batch_size=BATCH_SIZE,
        class_mode='categorical',
        subset='validation',
    )

    return train_generator, validation_generator

def load_compile_fit_model(train_generator, validation_generator):
    base_model = Xception(weights='imagenet', include_top=False, input_shape=(299, 299, 3))

    for layer in base_model.layers:
        layer.trainable = False

    model = Sequential()
    model.add(base_model)
    model.add(layers.GlobalAveragePooling2D())
    model.add(layers.Dense(256, activation='relu'))
    model.add(layers.Dropout(0.5))
    model.add(layers.Dense(NUM_CLASSES, activation='softmax'))

    model.compile(optimizer=tf.keras.optimizers.Adam(), loss=tf.keras.losses.CategoricalCrossentropy(), metrics=['accuracy'])

    model.fit(
        train_generator,
        steps_per_epoch=len(train_generator),
        epochs=5,
        validation_data=validation_generator,
        validation_steps=len(validation_generator)
    )

    return model

# Load and preprocess the data
train_generator, validation_generator = load_and_preprocess_data()

# Load, compile, and fit the model
model = load_compile_fit_model(train_generator, validation_generator)

# Save the trained model weights
model.save_weights(MODEL_WEIGHTS_PATH)

# Streamlit app
st.title("Crop Disease Detection App")

# Upload image through Streamlit file uploader
uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    # Load the uploaded image
    img = Image.open(uploaded_file)
    img = img.resize((299, 299))  # Resize image to match the model input size

    # Display the image
    st.image(img, caption="Uploaded Image", use_column_width=True)

    # Make prediction
    class_name, prediction = predict_image(model, img)

    # Display prediction result
    st.write(f'Predicted Class: {class_name} (Class Number: {np.argmax(prediction)})')

    # Plot the image with the predicted class
    st.image(img, caption=f'Predicted Class: {class_name}', use_column_width=True)