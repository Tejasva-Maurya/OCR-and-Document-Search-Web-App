import os
import re
import streamlit as st
from transformers import AutoModel, AutoTokenizer

# Set up page configuration for wide layout
st.set_page_config(
    page_title="OCR and Document Search Web Application Prototype Using GOT-OCR 2.0",
    layout="wide",
)


# Function to initialize model and tokenizer
@st.cache_resource
def init_model():
    tokenizer = AutoTokenizer.from_pretrained(
        "srimanth-d/GOT_CPU", trust_remote_code=True
    )
    model = AutoModel.from_pretrained(
        "srimanth-d/GOT_CPU",
        trust_remote_code=True,
        use_safetensors=True,
        pad_token_id=tokenizer.eos_token_id,
    )
    return model.eval(), tokenizer


# Function to extract text from the image using OCR model
@st.cache_data
def extract_text(image_file, _model, _tokenizer):
    res = _model.chat(_tokenizer, image_file, ocr_type="ocr")
    return res


# Function to highlight search term in extracted text
def highlight_text(text, search_term):
    if not search_term:
        return text
    pattern = re.compile(re.escape(search_term), re.IGNORECASE)
    return pattern.sub(
        lambda m: f'<span style="background-color: #FFFF00; font-weight: bold;">{m.group()}</span>',
        text,
    )


# Streamlit UI components
st.title("OCR and Document Search Web Application Prototype Using GOT-OCR 2.0")
st.write("Upload an image for OCR")

# Initialize model and tokenizer
model, tokenizer = init_model()

# Create columns for layout
col1, col2 = st.columns([1, 2])  # Adjust proportions as needed

with col1:
    # File uploader for images
    uploaded_image = st.file_uploader(
        "Upload Image", type=["jpg", "png", "jpeg"], key="image_upload"
    )

    # If an image is uploaded
    if uploaded_image:
        # Save the uploaded image to a local directory
        if not os.path.exists("images"):
            os.makedirs("images")
        image_path = os.path.join("images", uploaded_image.name)
        with open(image_path, "wb") as f:
            f.write(uploaded_image.getbuffer())

        # Create buttons for viewing the full image and clearing the image
        col1a, col1b = st.columns([0.5, 0.5])
        with col1a:
            if st.button("View Full Image"):
                # Show full image on demand
                st.image(image_path, caption="Full Size Image", use_column_width=True)

    else:
        st.info("Please upload an image to perform OCR.")

    # Fallback text in case no image is uploaded
    extracted_text = ""

    # Once the image is uploaded, extract the text
    if uploaded_image:
        extracted_text = extract_text(image_path, model, tokenizer)

with col2:
    # Input field for keyword search
    search_term = st.text_input("Enter a word or phrase to search:")

    # Highlight search term in extracted text
    highlighted_text = highlight_text(extracted_text, search_term)

    # Display search results
    if search_term:
        if search_term.lower() in highlighted_text.lower():
            st.success(f"Word **'{search_term}'** found in the text!")
        else:
            st.error(f"Word **'{search_term}'** not found.")

    # Show the extracted text with highlighted search terms
    st.markdown(highlighted_text, unsafe_allow_html=True)
