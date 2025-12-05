
import streamlit as st
import joblib
import pandas as pd

# Load the trained model
# The model was saved as 'final_spam_model.joblib' in the Colab environment.
# If you saved it to Google Drive, you would need to mount Drive and adjust the path.

try:
    model = joblib.load('final_spam_model.joblib')
except FileNotFoundError:
    st.error("Error: 'final_spam_model.joblib' not found. Make sure the model was saved in the current directory.")
    st.stop()

st.title('Spam Detector')
st.write('Enter a message below to check if it is spam or ham.')

# Text input from user
user_input = st.text_area('Enter your message here:', '')

if st.button('Predict'):
    if user_input:
        # Make prediction
        prediction = model.predict([user_input])
        prediction_proba = model.predict_proba([user_input])

        # Display result
        if prediction[0] == 1: # Assuming 1 is spam and 0 is ham
            st.error(f"This message is SPAM! (Confidence: {prediction_proba[0][1]*100:.2f}%)")
        else:
            st.success(f"This message is HAM. (Confidence: {prediction_proba[0][0]*100:.2f}%)")
    else:
        st.warning('Please enter a message to predict.')

# Optional: Display some model info
st.sidebar.header("About the Model")
st.sidebar.write("This is a RandomForestClassifier model trained for spam detection.")
