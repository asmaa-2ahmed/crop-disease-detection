import os
import re
from tensorflow.keras.applications.xception import Xception # type: ignore
from tensorflow.keras import layers, models # type: ignore
from src.config import NUM_CLASSES, MODEL_PATH, INPUT_SHAPE, TRAIN_DATASET_PATH

def load_saved_model():
    # Create model architecture using Xception as base, which is the best model.
    base_model = Xception(weights='imagenet', include_top=False, input_shape=INPUT_SHAPE)
    for layer in base_model.layers:
        layer.trainable = False
        
    model = models.Sequential([
        base_model,
        layers.GlobalAveragePooling2D(),
        layers.Dense(256, activation='relu'),
        layers.Dropout(0.5),
        layers.Dense(NUM_CLASSES, activation='softmax')
    ])
    
    # Load weights (ensure MODEL_PATH exists!)
    model.load_weights(MODEL_PATH)
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    
    return model

def clean_text(text):
    cleaned = re.sub(r'[^a-zA-Z0-9 ]', ' ', text).replace('  ', ' ').strip()
    return cleaned.title()



def get_class_labels_and_mapping():
    labels = []
    index_mapping = {}
    idx = 0

    # List folder names in the training dataset directory.
    if not os.path.isdir(TRAIN_DATASET_PATH):
        raise FileNotFoundError(f"Train dataset path not found: {TRAIN_DATASET_PATH}")

    # Only consider directories
    folder_names = [folder for folder in os.listdir(TRAIN_DATASET_PATH)
                    if os.path.isdir(os.path.join(TRAIN_DATASET_PATH, folder))]
    
    # Sort alphabetically to have a deterministic order
    folder_names.sort()
    
    for folder in folder_names:
        # Assume folder names are something like: "Apple___Apple_scab"
        if "___" in folder:
            parts = folder.split("___")
            fruit = parts[0].replace("_", " ").strip()
            # For disease, join all subsequent parts with a space.
            disease = " ".join(parts[1:]).replace("_", " ").strip()
        else:
            # If the separator "___" isn't present, use a simple split.
            parts = folder.split("_")
            fruit = parts[0].replace("_", " ").strip()
            disease = " ".join(parts[1:]).replace("_", " ").strip() if len(parts) > 1 else "Unknown"
            
        # For the purposes of the model, the raw folder name is used as the unique class label.
        labels.append(folder)
        index_mapping[idx] = {"fruit": fruit, "disease": disease}
        idx += 1
    
    return labels, index_mapping
