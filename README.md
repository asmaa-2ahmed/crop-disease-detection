# Plant Disease Detection

This project is a web application for detecting plant diseases using deep learning. It allows users to upload an image of a plant leaf and predicts the type of plant, the disease affecting it (if any), and the confidence level of the prediction.

## Features
- Upload an image of a plant leaf.
- Predict the plant type and disease.
- Display the confidence level of the prediction.
- Built with TensorFlow for deep learning and Streamlit for the web interface.

## Project Structure
```
PlantDisease/
├── app.py                # Main Streamlit application
├── requirements.txt      # Python dependencies
├── src/                  # Source code
│   ├── config.py         # Configuration settings
│   ├── inference.py      # Prediction logic
│   ├── schemas.py        # Data schemas
│   ├── utils.py          # Utility functions
│   └── assets/           # Model weights and datasets
│       ├── model_weights.h5  # Pre-trained model weights
│       └── dataset/      # Dataset for training and testing
└── notebooks/            # Jupyter notebooks for experiments
```

## Installation

1. Clone the repository:
   ```bash
   git clone <[repository-url](https://github.com/asmaa-2ahmed/crop-disease-detection)>
   cd PlantDisease
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

2. Open the application in your browser at `http://localhost:8501`.

3. Upload an image of a plant leaf and view the prediction results.


## Model
The application uses a pre-trained deep learning model stored in `src/assets/model_weights.h5`. The model was trained on a dataset of plant leaf images categorized by plant type and disease.

## Dataset
The dataset is organized into training and testing sets under `src/assets/dataset/`. Each category corresponds to a specific plant type and disease.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- The dataset used for training the model.
- TensorFlow and Streamlit for their powerful tools.
