import streamlit as st
import os
import time
from PIL import Image
from src.inference import predict
from src.config import APP_NAME, APP_VERSION, APP_DESCRIPTION

def setup_page_config():
    """Configure page settings and custom CSS"""
    st.set_page_config(
        page_title= "Plant Disease Classifier" ,
        page_icon="🌿",
        layout="wide"
    )
    
    st.markdown("""
    <style>
        .header-style {
            font-size: 50px;
            font-weight: bold;
            color: #2e8b57;
            text-align: center;
            padding: 30px 0px;
            background: linear-gradient(90deg, #f8fff8 0%, #e6f7e6 100%);
            border-radius: 15px;
            margin-bottom: 30px;
        }
        .subheader-style {
            font-size: 20px;
            text-align: center;
            color: #5f5f5f;
            padding-bottom: 30px;
        }
        .result-box {
            border-radius: 10px;
            padding: 20px;
            margin: 20px 0px;
            box-shadow: 0 4px 8px 0 rgba(0,0,0,0.1);
        }
        .healthy {
            background-color: #f0fff0;
            border-left: 5px solid #2e8b57;
        }
        .diseased {
            background-color: #fff0f0;
            border-left: 5px solid #ff6b6b;
        }
        .file-uploader {
            border: 2px dashed #c8e6c9;
            border-radius: 10px;
            text-align: center;
            background-color: #f8fff8;
        }
        .sidebar-green {
            background-color: #f8fff8;
            padding: 5px;
            border-radius: 10px;
            border: 1px solid #e6f7e6;
        }
    </style>
    """, unsafe_allow_html=True)

def create_sidebar():
    """Create the sidebar content"""
    with st.sidebar:
        st.markdown('<div class="sidebar-green">', unsafe_allow_html=True)
        st.header("🌱 App Information")
        st.write(f"**Version:** {APP_VERSION}")
        st.markdown("""
        **🔍 How to use:**
        1. Upload an image of a plant leaf
        2. The model will analyze it
        3. View the disease diagnosis
        """)
        
        st.divider()
        st.header("🌿 Supported Plants")
        st.markdown("""
            - 🍏 Apple  
            - 🫐 Blueberry  
            - 🍒 Cherry (including sour)  
            - 🌽 Corn (maize)  
            - 🍇 Grape  
            - 🍊 Orange  
            - 🍑 Peach  
            - 🌶️ Pepper (bell)  
            - 🥔 Potato  
            - 🌱 Soybean  
            - 🎃 Squash  
            - 🍓 Strawberry  
            - 🍅 Tomato  
            """)
        st.markdown('</div>', unsafe_allow_html=True)

def show_main_content():
    """Display the main content area"""
    st.markdown(f'<div class="header-style">🌿 {APP_NAME} 🍃</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="subheader-style">{APP_DESCRIPTION}</div>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="file-uploader">', unsafe_allow_html=True)
        uploader_key = st.session_state.get("uploader_key", "initial")

        uploaded_file = st.file_uploader(
            "📤 Drag & drop or click to upload a plant image", 
            type=["jpg", "jpeg", "png"],
            key=uploader_key,
            label_visibility="collapsed"
        )



        st.markdown('</div>', unsafe_allow_html=True)

    if uploaded_file is not None:
        process_uploaded_file(uploaded_file)

def process_uploaded_file(uploaded_file):
    """Handle the uploaded file and display results"""
    with st.expander("🌿 Uploaded Image", expanded=True):
        image = Image.open(uploaded_file)
        st.image(image, caption="Your plant image", width=350)
    
    with st.spinner("🔍 Analyzing plant health..."):
        temp_path = f"temp_{uploaded_file.name}"
        with open(temp_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        result = predict(temp_path)
        os.remove(temp_path)
        time.sleep(0.5)
    
    display_results(result)

def display_results(result):
    """Display the analysis results"""
    st.subheader("📊 Analysis Results")

    # Ensure the result contains valid keys for 'fruit' and 'disease'
    fruit = result.get('fruit', 'Unknown').title()
    disease = result.get('disease', 'Unknown').title()
    confidence = result.get('confidence', 0.0)

    is_healthy = disease.lower() == "healthy"
    result_class = "healthy" if is_healthy else "diseased"

    st.markdown(f"**🌱 Plant:** {fruit}")

    disease_emoji = "🌿✅" if is_healthy else "⚠️🍂"
    st.markdown(f"**{disease_emoji} Condition:** {disease}")

    st.write(f"**🎯 Confidence:** {confidence:.2%}")
    st.markdown(f"""
    <div style="width: 100%; background-color: #f0f0f0; border-radius: 10px; margin: 10px 0;">
        <div style="width: {confidence*100}%; height: 20px; border-radius: 10px; 
            background-color: {'#4CAF50' if is_healthy else '#F44336'};"></div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    show_recommendations(is_healthy)

def show_recommendations(is_healthy):
    """Display recommendations based on plant health"""
    st.subheader("💡 Recommendations")
    if is_healthy:
        st.success("""
        🌟 This plant appears healthy! Keep up the good work!
        
        **Maintenance Tips:**
        - 💧 Continue regular watering schedule
        - ☀️ Ensure proper sunlight exposure
        - 🌱 Monitor for any changes in leaf color or texture
        """)
    else:
        st.warning("""
        🚨 This plant shows signs of disease. Take action:
        
        **Immediate Steps:**
        - 🚧 Isolate the plant to prevent spread
        - ✂️ Remove affected leaves carefully
        - 🌿 Apply appropriate organic treatment
        - 📞 Consult with a local agricultural expert
        """)
        
        if st.button("🔍 Learn more about this disease"):
            st.info("""
            📚 We're compiling detailed treatment guides for each disease.
            Check back soon for specific recommendations for this condition!
            """)
    
    st.divider()
    if st.button("🔄 Analyze another plant"):
        # Generate a new uploader key to force widget to reset
        st.session_state.uploader_key = str(time.time())
        st.rerun()



def run_streamlit_app():
    """Main function to run the Streamlit app"""
    setup_page_config()
    create_sidebar()
    show_main_content()

if __name__ == "__main__":
    run_streamlit_app()