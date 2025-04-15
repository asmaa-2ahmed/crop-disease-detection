import numpy as np
from tensorflow.keras.utils import load_img, img_to_array # type: ignore
from src.utils import load_saved_model, get_class_labels_and_mapping, clean_text

# Load model only once
model = load_saved_model()

def predict(image_path):
    # Generate class labels and the index-to-label mapping.
    class_labels, index_mapping = get_class_labels_and_mapping()
    
    # Preprocess image
    img = load_img(image_path, target_size=(299, 299))
    img_array = img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    
    # Run the prediction
    predictions = model.predict(img_array)
    confidence = np.max(predictions)
    predicted_index = np.argmax(predictions)
    
    # Retrieve the mapping based on the predicted index.
    if predicted_index in index_mapping:
        fruit = clean_text(index_mapping[predicted_index]["fruit"])
        disease = clean_text(index_mapping[predicted_index]["disease"])
    else:
        fruit = "Unknown"
        disease = "Unknown"
    
    return {
        "confidence": confidence,
        "predicted_index": predicted_index,
        "fruit": fruit,
        "disease": disease
    }
