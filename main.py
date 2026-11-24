import os
import shutil
import numpy as np
from PIL import Image
import streamlit as st
import tensorflow as tf

# Import disease metadata
from disease_data import CLASS_NAMES, get_disease_info, DISEASE_DETAILS

# ==========================================
# PAGE CONFIGURATION & STYLING
# ==========================================
st.set_page_config(
    page_title="AI CropCare - Crop Disease Detection",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for agricultural theme
st.markdown("""
<style>
    .main-header {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1b5e20;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #4e6e58;
        margin-bottom: 1.5rem;
    }
    .metric-card {
        background: #f4fbf4;
        border: 1px solid #c8e6c9;
        border-radius: 12px;
        padding: 1.2rem;
        margin-bottom: 1rem;
    }
    .badge-healthy {
        background-color: #2e7d32;
        color: white;
        padding: 0.35rem 0.8rem;
        border-radius: 20px;
        font-weight: 600;
        display: inline-block;
    }
    .badge-diseased {
        background-color: #c62828;
        color: white;
        padding: 0.35rem 0.8rem;
        border-radius: 20px;
        font-weight: 600;
        display: inline-block;
    }
    .badge-pest {
        background-color: #ef6c00;
        color: white;
        padding: 0.35rem 0.8rem;
        border-radius: 20px;
        font-weight: 600;
        display: inline-block;
    }
    .status-box {
        padding: 0.75rem 1rem;
        border-radius: 8px;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)


# ==========================================
# MODEL LOADER & RESOLUTION
# ==========================================
@st.cache_resource(show_spinner="Loading deep learning model...")
def load_disease_model():
    """
    Locates and caches the trained Keras model.
    Handles filename variations and ensures .keras extension for Keras 3 compatibility.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    raw_model_path = os.path.join(base_dir, "Trained keras modal")
    keras_model_path = os.path.join(base_dir, "trained_model.keras")

    # If raw model exists without extension, make a .keras copy for Keras 3 compatibility
    if os.path.exists(raw_model_path) and not os.path.exists(keras_model_path):
        try:
            shutil.copyfile(raw_model_path, keras_model_path)
        except Exception:
            pass

    # Check candidates in order of preference
    candidates = [
        keras_model_path,
        raw_model_path,
        os.path.join(base_dir, "trained_model.h5"),
        os.path.join(base_dir, "model.keras"),
        os.path.join(base_dir, "model.h5")
    ]

    selected_path = None
    for path in candidates:
        if os.path.exists(path):
            selected_path = path
            break

    if not selected_path:
        return None, "Model file not found. Please ensure 'trained_model.keras' or 'Trained keras modal' is in the project folder."

    try:
        # Using compile=False prevents optimizer deserialization bugs across TF/Keras versions
        model = tf.keras.models.load_model(selected_path, compile=False)
        return model, None
    except Exception as e1:
        try:
            # Fallback without compile=False
            model = tf.keras.models.load_model(selected_path)
            return model, None
        except Exception as e2:
            return None, f"Failed to load model from {os.path.basename(selected_path)}: {str(e2)}"


def predict_crop_disease(image_file, model):
    """
    Preprocesses uploaded image and runs model inference.
    Returns predicted class, confidence, top 3 predictions, and full probability array.
    """
    # Rewind stream and open with PIL
    image_file.seek(0)
    img = Image.open(image_file).convert("RGB")

    # Resize to target dimension expected by model (128x128)
    img_resized = img.resize((128, 128), Image.Resampling.LANCZOS)
    img_arr = np.array(img_resized, dtype=np.float32)

    # Check if model already includes a Rescaling layer
    has_rescaling = any(
        "rescal" in layer.name.lower() or "rescal" in type(layer).__name__.lower()
        for layer in model.layers
    )

    if not has_rescaling and img_arr.max() > 1.0:
        # Scale to [0, 1] if model doesn't have an internal rescaling layer
        img_arr = img_arr / 255.0

    # Expand to batch dimension: shape (1, 128, 128, 3)
    input_arr = np.expand_dims(img_arr, axis=0)

    # Predict
    raw_preds = model.predict(input_arr, verbose=0)[0]

    # Convert logits to probabilities if necessary
    if abs(np.sum(raw_preds) - 1.0) > 0.05 or np.any(raw_preds < 0):
        probs = tf.nn.softmax(raw_preds).numpy()
    else:
        probs = raw_preds

    top_idx = int(np.argmax(probs))
    confidence = float(probs[top_idx]) * 100

    # Top 3 predictions
    top_3_indices = np.argsort(probs)[-3:][::-1]
    top_3 = []
    for idx in top_3_indices:
        c_name = CLASS_NAMES[idx]
        info = get_disease_info(c_name)
        top_3.append({
            'class_name': c_name,
            'crop': info['crop'],
            'disease': info['disease'],
            'prob': float(probs[idx]) * 100
        })

    return CLASS_NAMES[top_idx], confidence, top_3, probs


# ==========================================
# SIDEBAR
# ==========================================
with st.sidebar:
    st.image("home_page.png" if os.path.exists("home_page.png") else "🌱", width=80)
    st.title("AI CropCare")
    st.caption("Intelligent Plant Disease Detection System")
    st.markdown("---")

    app_mode = st.selectbox(
        "📌 Navigation",
        ["Home", "Disease Recognition", "Disease Encyclopedia", "About Project"]
    )

    st.markdown("---")
    st.markdown("### ⚙️ System Status")
    loaded_model, model_error = load_disease_model()

    if loaded_model is not None:
        st.success("🟢 Model Connected & Ready")
        st.caption("Deep Learning CNN Model (38 Classes)")
    else:
        st.error("🔴 Model Disconnected")
        st.caption(model_error)

    st.markdown("---")
    st.markdown("🌾 *Empowering farmers with instant AI-driven crop diagnostics.*")


# ==========================================
# PAGE 1: HOME
# ==========================================
if app_mode == "Home":
    st.markdown('<p class="main-header">🌱 AI CropCare Platform</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="sub-header">Multi-Crop Disease Detection & Agricultural Advisory System</p>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns([1.2, 1])

    with col1:
        if os.path.exists("home_page.png"):
            st.image("home_page.png", use_container_width=True, caption="Healthy Crops through AI-powered Diagnosis")

        st.markdown("""
        ### Why AI CropCare?
        Plant diseases reduce crop yield and quality, severely impacting food security and agricultural livelihoods. 
        **AI CropCare** uses advanced Deep Learning (Convolutional Neural Networks) to accurately detect plant diseases 
        from simple smartphone photos of crop leaves.

        #### Key Highlights:
        - ⚡ **Instant Diagnosis:** Get disease predictions in seconds.
        - 🩺 **38 Disease & Healthy Classes:** Detects common issues across 14 vital crop families.
        - 🧪 **Actionable Treatment Plans:** Verified organic, biological, and chemical management steps.
        - 📊 **Confidence Scoring:** High-transparency prediction metrics and top-3 alternative possibilities.
        """)

    with col2:
        st.markdown("### 🚜 Supported Crops")
        crops_supported = [
            ("🍎 Apple", "Scab, Black Rot, Cedar Apple Rust, Healthy"),
            ("🫐 Blueberry", "Healthy"),
            ("🍒 Cherry", "Powdery Mildew, Healthy"),
            ("🌽 Corn (Maize)", "Gray Leaf Spot, Common Rust, Northern Blight, Healthy"),
            ("🍇 Grape", "Black Rot, Esca, Leaf Blight, Healthy"),
            ("🍊 Orange / Citrus", "Citrus Greening (Huanglongbing)"),
            ("🍑 Peach", "Bacterial Spot, Healthy"),
            ("🫑 Bell Pepper", "Bacterial Spot, Healthy"),
            ("🥔 Potato", "Early Blight, Late Blight, Healthy"),
            ("🍓 Strawberry", "Leaf Scorch, Healthy"),
            ("🍅 Tomato", "Early Blight, Late Blight, Bacterial Spot, Leaf Mold, Mosaic Virus, etc.")
        ]

        for crop, conditions in crops_supported:
            with st.expander(f"{crop}"):
                st.write(f"**Conditions detected:** {conditions}")

        st.info("👉 Switch to **Disease Recognition** in the sidebar to upload a leaf photo and test the model!")


# ==========================================
# PAGE 2: DISEASE RECOGNITION
# ==========================================
elif app_mode == "Disease Recognition":
    st.markdown('<p class="main-header">🔬 Crop Disease Recognition</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="sub-header">Upload a clear leaf photograph to diagnose crop condition and get management recommendations.</p>',
        unsafe_allow_html=True
    )

    if loaded_model is None:
        st.error(f"⚠️ Cannot run prediction because the model is not loaded: {model_error}")
        st.stop()

    col_up, col_res = st.columns([1, 1.2], gap="large")

    with col_up:
        st.markdown("### 📤 Upload Leaf Photo")
        uploaded_file = st.file_uploader(
            "Choose an image file (JPG, JPEG, or PNG)",
            type=["jpg", "jpeg", "png"],
            help="For best results, photograph a single leaf against a neutral background."
        )

        if uploaded_file is not None:
            uploaded_img = Image.open(uploaded_file)
            st.image(uploaded_img, caption="Uploaded Leaf Image", use_container_width=True)

            img_w, img_h = uploaded_img.size
            st.caption(f"📐 Original Dimensions: {img_w}x{img_h}px | Format: {uploaded_img.format}")

            predict_btn = st.button("🔍 Diagnose Crop Disease", type="primary", use_container_width=True)
        else:
            st.info("👆 Please upload a photo to begin.")
            predict_btn = False

    with col_res:
        if uploaded_file is not None and predict_btn:
            with st.spinner("Analyzing leaf pathology with neural network..."):
                try:
                    pred_class, confidence, top_3, probs = predict_crop_disease(uploaded_file, loaded_model)
                    info = get_disease_info(pred_class)

                    st.markdown("### 📋 Diagnosis Result")

                    # Status badge
                    if info['status'] == 'Healthy':
                        badge_html = f'<span class="badge-healthy">✅ {info["status"].upper()}</span>'
                    elif 'Pest' in info['status']:
                        badge_html = f'<span class="badge-pest">⚠️ {info["status"].upper()}</span>'
                    else:
                        badge_html = f'<span class="badge-diseased">⚠️ {info["status"].upper()}</span>'

                    st.markdown(f"""
                    <div class="metric-card">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <h2>{info['crop']}</h2>
                            {badge_html}
                        </div>
                        <h4 style="color: #2e7d32; margin-top: 0;">Condition: {info['disease']}</h4>
                        <p><strong>Confidence:</strong> {confidence:.2f}%</p>
                    </div>
                    """, unsafe_allow_html=True)

                    # Confidence meter
                    st.progress(min(max(confidence / 100.0, 0.0), 1.0))

                    # Top alternative diagnoses
                    with st.expander("📊 Prediction Confidence Breakdown (Top 3)"):
                        for item in top_3:
                            st.write(f"**{item['crop']} - {item['disease']}:** {item['prob']:.2f}%")
                            st.progress(item['prob'] / 100.0)

                    # Diagnostic details tabs
                    tab1, tab2, tab3 = st.tabs(["🩺 Symptoms & Cause", "💊 Treatment Plan", "🛡️ Prevention Tips"])

                    with tab1:
                        st.markdown(f"**Pathogen / Cause:** {info['cause']}")
                        st.markdown(f"**Severity Level:** `{info['severity']}`")
                        st.markdown(f"**Observable Symptoms:**\n{info['symptoms']}")

                    with tab2:
                        st.markdown("### Recommended Agricultural Actions")
                        st.write(info['treatment'])

                    with tab3:
                        st.markdown("### Long-Term Crop Protection")
                        st.write(info['prevention'])

                except Exception as ex:
                    st.error(f"Error during disease diagnosis: {str(ex)}")

        elif uploaded_file is None:
            st.markdown("""
            ### How to Use:
            1. **Photograph:** Take a clear, focused photo of an affected leaf.
            2. **Upload:** Use the file picker on the left.
            3. **Diagnose:** Click **Diagnose Crop Disease** to run the AI model.
            4. **Review Treatment:** Follow the actionable organic and chemical advisory steps provided.
            """)


# ==========================================
# PAGE 3: DISEASE ENCYCLOPEDIA
# ==========================================
elif app_mode == "Disease Encyclopedia":
    st.markdown('<p class="main-header">📚 Crop Disease Encyclopedia</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="sub-header">Browse all 38 plant conditions, symptoms, and agricultural treatment guides.</p>',
        unsafe_allow_html=True
    )

    # Search & Filter
    search_query = st.text_input("🔍 Search by crop or disease name:", placeholder="e.g. Tomato, Blight, Rust, Apple...")

    filtered_classes = [
        cls for cls in CLASS_NAMES
        if search_query.lower() in cls.lower().replace('_', ' ')
    ]

    st.write(f"Showing **{len(filtered_classes)}** of **{len(CLASS_NAMES)}** conditions:")

    for cls in filtered_classes:
        info = get_disease_info(cls)
        status_icon = "🟢" if info['status'] == 'Healthy' else "🔴"

        with st.expander(f"{status_icon} {info['crop']} — {info['disease']} ({info['status']})"):
            c1, c2 = st.columns(2)
            with c1:
                st.markdown(f"**Cause:** {info['cause']}")
                st.markdown(f"**Severity:** {info['severity']}")
                st.markdown(f"**Symptoms:** {info['symptoms']}")
            with c2:
                st.markdown(f"**Treatment:**\n{info['treatment']}")
                st.markdown(f"**Prevention:**\n{info['prevention']}")


# ==========================================
# PAGE 4: ABOUT PROJECT
# ==========================================
elif app_mode == "About Project":
    st.markdown('<p class="main-header">ℹ️ About AI CropCare</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="sub-header">System Architecture and Deep Learning Pipeline</p>',
        unsafe_allow_html=True
    )

    c1, c2 = st.columns([1.2, 1])
    with c1:
        st.markdown("""
        ### Project Architecture
        **AI CropCare** is built to bridge artificial intelligence with day-to-day agricultural farming practices.
        
        - **Model Framework:** TensorFlow 2.x & Keras 3
        - **Model Architecture:** Deep Convolutional Neural Network (CNN)
        - **Input Dimensions:** `128 x 128 x 3` (RGB)
        - **Output Classes:** 38 Classes (covering Apple, Corn, Grape, Tomato, Potato, and more)
        - **Frontend Framework:** Streamlit
        - **Optimization:** Cached resource loading with `@st.cache_resource` for sub-second diagnosis.

        ### Verification Status
        - Model weights successfully integrated from local repository storage.
        - Streamlit caching active to eliminate memory leaks and loading latency.
        - Full agricultural treatment encyclopedia integrated for real-world farmer assistance.
        """)

    with c2:
        if os.path.exists("image-1.png"):
            st.image("image-1.png", caption="System Architecture & Goals", use_container_width=True)
