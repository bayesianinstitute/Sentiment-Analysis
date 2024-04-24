# Sentiment Analysis Model Fine-Tuning 


Application Link: https://huggingface.co/faizack/Fine_Tune_Roberta-base-sentiment
## Overview

This repository illustrates how to fine-tune the CardiffNLP Twitter RoBERTa Base model for sentiment analysis using your own dataset. The pre-trained model employed here is based on the RoBERTa architecture and has been specialized in sentiment analysis tasks using Twitter data.

## Setup and Prerequisites

Before proceeding, ensure you have the following dependencies installed:

- Python 3.12

Install Required Packages

```bash
pip install -r requirements.txt
```

## Notebook for Analysis and Fine-Tuning
Run analysis.ipynb

## Data Preparation

1. **Dataset Acquisition:** Obtain the Amazon Reviews dataset from Kaggle API and load in .env as shown .env.example.

2. **Data Extraction and Preparation:** Extract the compressed data files (`train.ft.txt.bz2` and `test.ft.txt.bz2`) and preprocess them into readable text files (`train.ft.txt` and `test.ft.txt`).

3. **Data Loading:** Load the preprocessed data into Pandas DataFrames for further processing.

## Model Fine-Tuning

1. **Tokenization:** Use the `AutoTokenizer` from Hugging Face's Transformers library to tokenize the text data.

2. **Model Initialization:** Initialize the pre-trained sentiment analysis model (`AutoModelForSequenceClassification`) from the CardiffNLP Twitter RoBERTa Base.

3. **Training:** Fine-tune the initialized model on the preprocessed dataset. Apply appropriate training parameters and evaluation metrics.

4. **Model Saving:** Save the fine-tuned model and tokenizer for future usage.

## Inference

1. **Model Loading:** Load the saved fine-tuned model and tokenizer.

2. **Prediction:** Tokenize the input text and perform sentiment analysis using the loaded model.

3. **Result Interpretation:** Interpret the model's output to determine the sentiment label and confidence score.

For running the Flask API and the Streamlit app, follow these simplified steps:

**Note** : **Before Running the Flask API make sure you run all step in Analysis**

1. **Flask API:**

   - Start the Flask API:

     ```bash
     cd server/;flask --app api.py run
     ```

2. **Streamlit App:**

   - Run the Streamlit app:

     ```bash
     streamlit run app.py
     ```