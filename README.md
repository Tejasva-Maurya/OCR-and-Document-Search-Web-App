
# OCR and Document Search Web Application Prototype Using GOT-OCR 2.0

This repository contains a **Streamlit**-based web application that leverages the **GOT 2.0** OCR model for optical character recognition (OCR) and document search functionality. The application is deployed on Hugging Face Spaces, running on **CPU**, which may cause slightly slower processing times.

## Features

- **OCR:** Upload an image and extract text using the GOT 2.0 model.
- **Document Search:** Search for specific words or phrases in the extracted text.
- **Language Support:** Primarily supports English and Chinese, with limited accuracy for Hindi.
- **Deployment:** Hosted on Hugging Face Spaces and optimized for CPU-based execution.

## Table of Contents

- [Installation](#installation)
- [Running Locally](#running-locally)
- [Deployment](#deployment)
- [Usage](#usage)
- [GOT 2.0 Model Details](#got-20-model-details)
- [Limitations](#limitations)

## Installation

Follow these steps to set up the project environment:

### 1. Clone the Repository

```bash
git clone https://github.com/Tejasva-Maurya/OCR-and-Document-Search-Web-Application-Prototype-Using-GOT-OCR-2.0.git
cd OCR-and-Document-Search-Web-Application-Prototype-Using-GOT-OCR-2.0
```

### 2. Set up a Virtual Environment

Create a virtual environment to keep the project dependencies isolated.

For Python 3:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies

Install the required Python packages from `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Running Locally

To run the application locally, follow these steps:

### 1. Run the Streamlit App

```bash
streamlit run app.py
```

This will start a local server, and you can access the application in your browser at `http://localhost:8501`.

### 2. Upload Images and Perform OCR

Once the app is running, upload an image (e.g., JPG, PNG, JPEG), and the OCR model will extract the text. You can search for specific words or phrases within the extracted text.

### 3. Project Structure

- `app.py`: Main application file.
- `images/`: Directory where uploaded images are saved.

## Deployment

The application is deployed on **Hugging Face Spaces** using **Streamlit**. Due to **GPU-related complexities on Hugging Face**, the application runs on **CPU** by default. This might result in slower performance during OCR processing, but it avoids potential issues related to GPU execution.

### 1. Set up Hugging Face Spaces

- Create a new repository on [Hugging Face Spaces](https://huggingface.co/spaces).
- Select **Streamlit** as the framework for deployment.

### 2. Upload Your Code

Push your code to the Hugging Face Spaces repository you just created.

```bash
git add .
git commit -m "Initial commit"
git push origin main
```

### 3. Configure the `requirements.txt`

Ensure your `requirements.txt` is correctly set up for the Hugging Face environment to install the necessary dependencies.

### 4. Deploy

After pushing the code, Hugging Face Spaces will automatically build and deploy your app. You can access the app through the Hugging Face URL provided.

## GOT 2.0 Model Details

The GOT 2.0 model is an advanced OCR model initially developed to support **English** and **Chinese** languages. The model uses a combination of pre-trained transformers and optimized tokenization techniques to extract text from images efficiently.

- **Pre-trained on English and Chinese:** While the model performs well for these languages, it may exhibit reduced accuracy when used for other languages like Hindi.
- **CPU Performance:** The model is optimized for **GPU**, but this application runs it on **CPU** due to Hugging Face limitations. This results in slower inference times.
- **Hugging Face Model:** The application loads the model from the Hugging Face repository: `srimanth-d/GOT_CPU`.

## Limitations

### 1. **CPU Processing**
   - The application runs on CPU, which may result in longer processing times. GPU deployment is not feasible due to Hugging Face constraints on GPU support.
   
### 2. **Hindi Language Support**
   - The GOT 2.0 model was not specifically trained for Hindi, and the OCR accuracy for Hindi text is **limited**. It works best with **English** and **Chinese** images.
   
### 3. **Model Size and Performance**
   - The GOT 2.0 model is resource-intensive, and even on CPU, it may take additional time to process larger images or images with complex text.

## Usage

1. Open the app and upload an image to perform OCR.
2. After the text is extracted, use the search box to find specific words or phrases in the document.
3. The app will highlight the search terms in the extracted text and indicate whether the term was found.

---
