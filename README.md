# 🌿 AI-Powered Crop Disease Detection Using Deep Learning 🚀

Welcome to the **Crop Disease Detection Web App**, an AI-driven tool designed to help identify plant diseases directly from leaf images using deep learning. In an age where global food security is challenged by agricultural diseases, this project demonstrates how artificial intelligence can offer **fast, accurate, and scalable** plant disease diagnosis.

This system was developed as the core of a **Neural Networks course project** and earned a **Certificate of Appreciation** from Pharos University — proving both its technical and practical significance. 🍃📸

---

## 🌟 Key Features

- ✅ **Image Upload**: Detect disease from a photo of a plant leaf  
- ✅ **Plant Type & Disease Prediction**  
- ✅ **Confidence Score Visualization**  
- ✅ **Pre-trained Deep Learning Model (TensorFlow)**  
- ✅ **Intuitive Web Interface with Streamlit**  
- ✅ **Custom UI Styling & Modular Codebase**

---

## 🔍 What’s Under the Hood?

To develop the most accurate model, several CNN architectures and optimizers were explored:

| Architecture | Optimizer | Accuracy |
|--------------|-----------|----------|
| ✅ Xception   | Adam      | 🥇 **92.37%** |
| NASNet       | SGD       | 85.53%   |
| VGG16        | Adam      | 89.00%   |

🔧 These experiments highlight the importance of model architecture and optimizer pairing in deep learning performance.

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/asmaa-2ahmed/crop-disease-detection.git
cd PlantDisease
```

### 2️⃣ Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Required Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Streamlit app:

```bash
streamlit run app.py
```

This will launch the interface in your browser at: [http://localhost:8501](http://localhost:8501)

---

## 🖼 How to Use It

1. Launch the app using the command above  
2. Upload a **clear image** of a plant leaf  
3. View:
   - 🌱 The **predicted plant type**
   - 🦠 The **detected disease (if any)**
   - 📊 The **confidence score** of the prediction  

No code changes needed — just plug and play!

---

## 🧠 Model Details

- **Framework:** TensorFlow / Keras  
- **Model Format:** HDF5 (`model_weights.h5`)  
- **Architecture:** Xception (best performing)  
- **Training Set:** High-resolution images of diseased and healthy plant leaves  
- **Categories:** Multiple plant types with disease/no-disease labels  

📁 Model Location: `src/assets/model_weights.h5`

---

## 🌱 Dataset

The training and testing images are organized in:

```
src/assets/dataset/
```

Each folder represents a specific class (e.g., `Tomato___Early_blight`, `Corn___Healthy`).

Dataset used for training was sourced from a public agricultural image dataset.

---

## 📫 Contributing

Contributions are welcome and encouraged!

If you have ideas for improving:
- 🔍 Model performance  
- 🎨 User interface  
- 🧪 Testing  
- 📊 Visualization  

Feel free to **fork the repo** and submit a **pull request**. Let’s make agriculture smarter, together.

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](https://github.com/asmaa-2ahmed/crop-disease-detection/blob/main/LICENSE) file for details.

---

## 🙏 Acknowledgments

- Special thanks to my **professors and mentors** for their guidance.  
- Huge appreciation to **TensorFlow**, **Streamlit**, and open-source contributors.  
- Dataset creators who made this possible for academic research.

---

## 🔗 Links

- 🔍 **GitHub Repository**: [github.com/asmaa-2ahmed/crop-disease-detection](https://github.com/asmaa-2ahmed/crop-disease-detection)  
- 🎓 Featured in: Neural Networks Course Project  
- 🏅 Awarded: Certificate of Appreciation – Pharos University

---

## 💬 Have Suggestions?

If you’ve got ideas for improvements, feel free to:

- Open an [issue](https://github.com/asmaa-2ahmed/crop-disease-detection/issues)
- Contact me through LinkedIn or GitHub
- Submit a pull request!

Let’s build better tech for sustainable agriculture 🌾
