# Beer quality dection

Team name: ift3395_trung_nguyen  
Team members: Trung Nguyen - 20238006

This repository contains a complete pipeline for training a model to assess the severity of diabetic retinopathy from retinal fundus photographs. The model is trained to classify the severity from 0-4.

## Overview

The pipeline consists of several key components:

- **Data Preprocessing**: Apply preprocessing techniques on the data
- **Train/Validation Split**: Split the data into train and val set
- **Model Training**: Trains a Multi-Layer Perceptron model
- **Evaluate Models**: Evaluate models using training and validation results
- **Generate Prediction**: Using the model to predict on unseen data

## Project Structure

```
3395-competition2/
├── notebook.ipynb                      # Notebook file for the training pipeline            
├── README.md                           # This file
├── requirements.txt                    # Required libraries to run the notebook
├── submission.csv/                     # Prediction output
├── data/          
│   ├── test_data.pkl/                       # Unseen test data
│   └── train_data.pkl/                      # Training data
```

## Prerequisites

### Required Python Packages

Install the required packages:

```bash
# Create a virtual environment
python3 -m venv .venv

# Activate the environment
# On Linux/macOS:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate

# Install requirements
pip install -r requirements.txt
```

## Step-by-Step Training Process

### Step 1: Data Preprocessing

- Flatten images and normalize pixel values to [0, 1]
- Oversampling + Numeric Augmentation

### Step 2: Train/Validation Split

- Split the dataset into train and val set while keeping both sets proportionated to each other

### Step 3: Model Training

- Pass training data into the model and update weights with backpropagation

### Step 4: Evaluate Model

- Evalute model using the result from train and val set
- Evaluation by accuracy and confusion matrix

### Step 5: Generate Prediction

- Flatten the images of the test set
- Pass the processed test data onto the model for prediction
- Output is a csv file formatted according to the ```sample_submission.csv```
