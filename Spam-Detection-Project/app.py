import streamlit as st
import pickle
import os

st.set_page_config(page_title="Spam Detection System", page_icon=" ", layout="centered")

# Get current script path to find pkl files easily
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, 'spam_model.pkl')
vectorizer_path = os.path.join(BASE_DIR, 'vectorizer.pkl')

@st.cache_resource
def load_models():
    with open(model_path, 'rb') as f_model:
        model = pickle.load(f_model)
    with open(vectorizer_path, 'rb') as f_vec:
        vectorizer = pickle.load(f_vec)
    return model, vectorizer

try:
    model, vectorizer = load_models()
    
    st.title("Email / SMS Spam Detector")
    st.write("Enter your message below to analyze whether it is **Spam** or **Safe (Ham)**.")
    st.divider()

    user_input = st.text_area("Message Content:", placeholder="Type or paste your message here...", height=150)

    if st.button("Predict Status", type="primary"):
        if user_input.strip() != "":
            transformed_input = vectorizer.transform([user_input])
            prediction = model.predict(transformed_input)[0]
            
            st.subheader("Analysis Result:")
            if str(prediction).lower() in ['1', 'spam']:
                st.error("**SPAM DETECTED**")
                st.warning("High Risk: This message shows patterns associated with spam/phishing.")
            else:
                st.success("**SAFE / HAM MESSAGE**")
                st.info("This message appears legitimate.")
        else:
            st.warning("Please enter a message to evaluate.")

except Exception as e:
    st.error(f"Error loading files: {e}")
    st.info("Make sure 'spam_model.pkl' and 'vectorizer.pkl' are placed inside the 'Spam-Detection-Project' folder.")